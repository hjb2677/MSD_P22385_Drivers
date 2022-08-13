"""
MSD P22385
Themed Entertainment Model Display
File    : UnitTest.py
Author  : Harrison Barnes
Date    : 08/13/2022
Purpose : Unit Test File - performs individual tests on the subroutines.
          Must pass tests for display to run correctly
"""

# Subroutine defines - selects the correct subroutine to examine
TEST_SCHEDULER = "SCH"
TEST_IDLER = "IDL"
TEST_ACTIVATOR = "ACT"
TEST_HALL_MONITOR = "HMT"
TEST_ERROR_REPORTER = "ERR"
TEST_ALL_SUBROUTINES = "ALL"
EXIT_PROGRAM = "EXT"

"""
Function : mainUnitTest
Inputs   : SubroutineID - user IO at start of program that matches subroutine define constant
Outputs  : none

Tests the individual components of a specific subroutine to ensure that edits to the code to not result in
incorrect functionality
"""
def mainUnitTest():

    # Set subroutineID to initial string to bypass while loop check
    subroutineID = "init"

    # Loop through tests until user requests termination
    while subroutineID != EXIT_PROGRAM:

        # Print prompt and selection information, allowing user to select their subroutine
        print("\nUnit Test Program\nEnter one of the following subroutine choices in ALL CAPS")
        print("Selection choices...\n\tScheduler = SCH\n\tIdler = IDL\n\tActivator = ACT")
        print("\tHall Monitor = HMT\n\tError Reporter = ERR\n\tAll Subroutines = ALL\n\tExit Program = EXT")

        # Retrieve subroutineID from the terminal
        subroutineID = input("SubroutineID Selection: ")

        # Based on subroutineID, select the subroutine to test
        if subroutineID == TEST_SCHEDULER:
            testScheduler()  # Perform all Scheduler unit tests, then re-prompt
        elif subroutineID == TEST_IDLER:
            testIdler()  # Perform all Idler unit tests, then re-prompt
        elif subroutineID == TEST_ACTIVATOR:
            testActivator()  # Perform all Activator unit tests, then re-prompt
        elif subroutineID == TEST_HALL_MONITOR:
            testHallMonitor()  # Perform all Hall Monitor unit tests, then re-prompt
        elif subroutineID == TEST_ERROR_REPORTER:
            testErrorReporter()  # Perform all Error Reporter unit tests, then re-prompt
        elif subroutineID == TEST_ALL_SUBROUTINES:
            testAllSubroutines()  # Perform all unit tests, then re-prompt
        elif subroutineID == EXIT_PROGRAM:
            # User requests program exit. End loop
            print("\nExiting program...")
        else:
            # User did not put in a correct ID, re-prompt user
            print("\nInvalid ID detected")
    print("Program concluded")


"""
Function : testScheduler
Inputs   : none
Outputs  : none

Tests the individual components of the Scheduler subroutine
"""
def testScheduler():
    print("\n\tTesting Scheduler...")
    print("\tDone testing Scheduler!")


"""
Function : testIdler
Inputs   : none
Outputs  : none

Tests the individual components of the Idler subroutine
"""
def testIdler():
    print("\n\tTesting Idler...")
    print("\tDone testing Idler!")


"""
Function : testActivator
Inputs   : none
Outputs  : none

Tests the individual components of the Activator subroutine
"""
def testActivator():
    print("\n\tTesting Activator...")
    print("\tDone testing Activator!")


"""
Function : testHallMonitor
Inputs   : none
Outputs  : none

Tests the individual components of the Hall Monitor subroutine
"""
def testHallMonitor():
    print("\n\tTesting Hall Monitor...")
    print("\tDone testing Hall Monitor!")


"""
Function : testErrorReporter
Inputs   : none
Outputs  : none

Tests the individual components of the Error Reporter subroutine
"""
def testErrorReporter():
    print("\n\tTesting Error Reporter...")
    print("\tDone testing Error Reporter!")


"""
Function : testAllSubroutines
Inputs   : none
Outputs  : none

Tests the individual components of the all subroutines. Calls each subroutine's unit test function
"""
def testAllSubroutines():
    print("\n\tTesting all subroutines...")
    testScheduler()
    testIdler()
    testActivator()
    testHallMonitor()
    testErrorReporter()
    print("\n\tDone testing all subroutines!")


if __name__ == '__main__':
    mainUnitTest()

