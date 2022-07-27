"""
MSD P22385
Themed Entertainment Model Display
File    : DisplayDriver.py
Author  : Harrison Barnes
Date    : 05/03/2022
Purpose : Driver program for the entire display
"""

# Imports - Libraries
import time

# Imports - Files
import Activator
import ErrorReporter
import HallMonitor
import Schedule
import Scheduler
import Idle
import Idler
import DriverFlowCodes
import ErrorCodes


def main():
    # =============================================
    #                   Initialization
    # =============================================

    # Output boot message to terminal with credits, msg, and date/time
    print("\nBeginning Display Driver - created by P22385")
    print("System Driver booting up at:")
    Scheduler.PrintTimeOfDay()
    Scheduler.PrintDate()

    # Init control code to enter the Scheduler on first loop. Stores next control driver to activate
    controlCode = DriverFlowCodes.DRIVER_ENTRY_SCHEDULER

    # Init error code to zero (no error detected). Stores errors from error reporter
    errorCode = ErrorCodes.NOMINAL_STATE

    # Init return code to zero. Stores return codes (validates, etc.) from control blocks
    returnCode = 0

    # Init loop exit flag - 0 = loop, 1 = exit loop
    loopExitFlag = 0

    # =============================================
    #                   POST
    # =============================================

    # POST CODE HERE

    # MAIN LOOP
    # Loops through a switch statement that enters each
    # driver control system as directed by the previous
    # system
    while not loopExitFlag:
        # SWITCH STATEMENT - switch on controlCode variable
        if controlCode == DriverFlowCodes.DRIVER_ENTRY_SCHEDULER:
            # =============================================
            #                   Scheduler
            # =============================================

            # returnCode stores the validation code, representing the
            # validity of the current time within the scheduler
            returnCode = Scheduler.SchedulerDriver()

            # Send driver to correct control block based on validity of current time
            if returnCode == Schedule.VALID_RUN_TIME:
                # Time is valid, begin the ride without waiting for user input
                controlCode = DriverFlowCodes.DRIVER_ENTRY_ACTIVATOR
            elif returnCode == Schedule.VALID_TIME:
                # Time is valid, wait for user input to begin ride
                controlCode = DriverFlowCodes.DRIVER_ENTRY_IDLER
            elif returnCode == Schedule.INVALID_MINUTE or returnCode == Schedule.INVALID_HOUR \
                    or returnCode == Schedule.INVALID_DOW or returnCode == Schedule.INVALID_DATE:
                # Invalid time occurred within Scheduler control block, wait before polling timestamp again
                time.sleep(Schedule.FETCH_TIMESTAMP_DELAY_S)
                controlCode = DriverFlowCodes.DRIVER_ENTRY_SCHEDULER
            else:
                # Error detected within Scheduler control block
                controlCode = DriverFlowCodes.DRIVER_ENTRY_ERROR_REPORTER
        elif controlCode == DriverFlowCodes.DRIVER_ENTRY_IDLER:
            # =============================================
            #                     Idler
            # =============================================

            # returnCode stores the Idler code, which holds the results of the
            # Idler polling, either IO detected, time out, or error
            returnCode = Idler.IdlerDriver()

            # Send driver to correct control block based on Idler status
            if returnCode == Idle.IDLER_GPIO_IO_DETECTED:
                # User IO detected, send to Activator to begin ride sequence
                controlCode = DriverFlowCodes.DRIVER_ENTRY_ACTIVATOR
            elif returnCode == Idle.IDLER_TIME_OUT_DETECTED:
                # User IO not detected, Idler timed out. Return to scheduler
                # to re-validate time
                controlCode = DriverFlowCodes.DRIVER_ENTRY_SCHEDULER
            else:
                # Error detected within Idler control block
                controlCode = DriverFlowCodes.DRIVER_ENTRY_ERROR_REPORTER
        elif controlCode == DriverFlowCodes.DRIVER_ENTRY_ACTIVATOR:
            # =============================================
            #                   Activator
            # =============================================
            returnCode = Activator.ActivatorDriver()
        elif controlCode == DriverFlowCodes.DRIVER_ENTRY_HALL_MONITOR:
            # =============================================
            #                 Hall Monitor
            # =============================================
            returnCode = HallMonitor.HallMonitorDriver()
        elif controlCode == DriverFlowCodes.DRIVER_ENTRY_ERROR_REPORTER:
            # =============================================
            #                Error Reporter
            # =============================================
            returnCode = ErrorReporter.ErrorReporterDriver()
        elif controlCode == DriverFlowCodes.DRIVER_EXIT_NORMAL:
            # =============================================
            #             NOMINAL EXIT HANDLING
            # =============================================
            # Print notice, TOD, date, and handle statement
            print("\nDriver received nominal exit control code :", controlCode)
            print("Driver detected nominal exit code: ", returnCode, " at: ")
            Scheduler.PrintTimeOfDay()
            Scheduler.PrintDate()
            print("Exiting driver control loop...\n")

            # Raise exit flag to end loop
            loopExitFlag = 1
        elif controlCode == DriverFlowCodes.DRIVER_EXIT_FATAL:
            # =============================================
            #               FATAL ERROR HANDLING
            # =============================================

            # Print notice, TOD, date, and handle statement
            print("\nDriver received fatal control code :", controlCode)
            print("Driver detected fatal error code: ", errorCode, " at: ")
            Scheduler.PrintTimeOfDay()
            Scheduler.PrintDate()
            print("Exiting driver control loop...\n")

            # Raise exit flag to end loop
            loopExitFlag = 1
        else:
            # =============================================
            #           UNKNOWN CONTROL CODE DETECTED
            # =============================================

            # Print notice, TOD, date, and handle statement
            print("\nDriver switch statement detected an unknown control code of ", controlCode, " at: ")
            Scheduler.PrintTimeOfDay()
            Scheduler.PrintDate()
            print("Heading to error reporting control software...\n")

            # Send driver to error reporting
            controlCode = DriverFlowCodes.DRIVER_ENTRY_ERROR_REPORTER

            # Assign error code, designating an unknown control code occurred
            errorCode = ErrorCodes.WARN_UNKNOWN_CTRL_CODE
    # ========================================================================
    # end of while loop - exits when exit condition is reached (fatal/nominal)
    # and flag is set high
    # ========================================================================

    # =============================================
    #                   Shut Down
    # =============================================

    # Print Exit message
    print("\n\nExiting Display Driver - created by P22385\nRequires manual restart")
    print("Exit conditions:")
    print("Control Code : ", controlCode)
    print("Return Code  : ", returnCode)
    print("Error Code   : ", errorCode)
    print("Exit Flag    : ", loopExitFlag)
    print("\nSystem Driver exiting at:")
    Scheduler.PrintTimeOfDay()
    Scheduler.PrintDate()


if __name__ == "__main__":
    main()
