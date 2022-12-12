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
import Activate
import ErrorReporter
import HallMonitor
import HallHeader
import Schedule
import Scheduler
import SchedulingInterface
import DriverFlowCodes
import ErrorCodes
import RunDisplay

"""
Function : main
Inputs   : none
Outputs  : none

The main driver routine of the ride system. Performs a POST, then follows the program
control flow based on the results of various subroutines.
"""
def main():
    # =============================================
    #                   Initialization
    # =============================================
    
    # Initialize variable to track previous error. If two of the same errors occur in a row, exit program
    previousError = 0
    
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

    # CSV handling
    errorCode = SchedulingInterface.InitializeSchedule()
    if errorCode != Schedule.CSV_SUCCESS:  # If CSV encountered an error
        # Print notice, TOD, date, and handle statement
        print("\nCSV Validation error occurred. Check syntax and manual\n");
        Scheduler.PrintTimeOfDay()
        Scheduler.PrintDate()
        print("Exiting driver control loop...\n")
        return -1

    print("CSV Validation finished. Starting program...\n")

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
                
            # Wait set time before fetching
            time.sleep(Schedule.FETCH_TIMESTAMP_DELAY_S)

            # returnCode stores the validation code, representing the
            # validity of the current time within the scheduler
            returnCode = Scheduler.SchedulerDriver()
            print(returnCode)
            # Send driver to correct control block based on validity of current time
            if returnCode == Schedule.VALID_RUN_TIME:
                # Time is valid, begin the ride
                # controlCode = DriverFlowCodes.DRIVER_ENTRY_RUN
                print("Testing, RUN at time :")
                Scheduler.PrintTimeOfDay()
                print("\n")
            elif returnCode == Schedule.INVALID_MINUTE or returnCode == Schedule.INVALID_HOUR \
                    or returnCode == Schedule.INVALID_DOW or returnCode == Schedule.INVALID_DATE \
                    or Schedule.INVALID_MONTH or Schedule.INVALID_WEEK:
                # Invalid time occurred within Scheduler control block, wait before polling timestamp again
                controlCode = DriverFlowCodes.DRIVER_ENTRY_SCHEDULER
                print("Testing, INVALID at time: ")
                Scheduler.PrintTimeOfDay()
                print("\n")
            else:
                # Error detected within Scheduler control block
                controlCode = DriverFlowCodes.DRIVER_ENTRY_ERROR_REPORTER
                errorCode = ErrorCodes.WARN_SCHEDULER_ERROR_OCCURRED
                
        elif controlCode == DriverFlowCodes.DRIVER_ENTRY_ACTIVATOR:
            # =============================================
            #                   Activator
            # =============================================
            
            # ACTIVATOR IS DEPRECATED. SEE RunDisplay.py
            # If Activator code is recieved, exit program
            errorCode = ErrorCodes.FATAL_DEPRECATED_ENTRY_DETECTED
            
            # The Activator and Hall Monitor are time sensitive processes.
            # Due to this, there is no error checking for the Activator.
            # It is assumed that the HES can detect Activator errors
            controlCode = DriverFlowCodes.DRIVER_ENTRY_ERROR_REPORTER
            
        elif controlCode == DriverFlowCodes.DRIVER_ENTRY_HALL_MONITOR:
            # =============================================
            #                 Hall Monitor
            # =============================================
            # HALL MONITOR IS DEPRECATED. SEE RunDisplay.py
            # If Hall Monitor code is recieved, exit program
            errorCode = ErrorCodes.FATAL_DEPRECATED_ENTRY_DETECTED
            controlCode = DriverFlowCodes.DRIVER_ENTRY_ERROR_REPORTER
        elif controlCode == DriverFlowCodes.DRIVER_ENTRY_RUN:
            # =============================================
            #                 Run Display
            # =============================================
            # HRunDisplay replaces the deprecated Activator
            # and Hall Monitor by combining them and interweaving
            # them. Not that their respective headers Activate.py
            # and HallHeader.py are still used
            returnCode = RunDisplay.RunDisplayDriver()
            if returnCode == HallMonitor.HALL_MONITOR_ALL_GOOD:
                # Successful trip around track, go back to Scheduler
                controlCode = DriverFlowCodes.DRIVER_ENTRY_SCHEDULER
            else:
                # Error occured, report to ErrorReporter
                errorCode = returnCode
                controCode = DriverFlowCodes.DRIVER_ENTRY_ERROR_REPORTER
        elif controlCode == DriverFlowCodes.DRIVER_ENTRY_ERROR_REPORTER:
            # =============================================
            #                Error Reporter
            # =============================================
            returnCode = ErrorReporter.ErrorReporterDriver(errorCode, previousError)
            previousError = errorCode
            if returnCode == ErrorReport.ERROR_REPORTER_CONTINUE_DRIVER:
                # Error is not fatal, continue loop
                controlCode = DriverFlowCodes.DRIVER_ENTRY_SCHEDULER
            else:
                # Error is fatal, exit loop
                controlCode = DriverFlowCodes.DRIVER_EXIT_FATAL
                
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
            print("\nReturning to Scheduler")
        
            # Send driver to error reporting
            controlCode = DriverFlowCodes.DRIVER_ENTRY_SCHEDULER
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


"""
This section is required for the program to enter the main subroutine.
"""
if __name__ == "__main__":
    main()
