"""
MSD P22385
Themed Entertainment Model Display
File    : UnitTest.py
Author  : Harrison Barnes
Date    : 08/13/2022
Purpose : Unit Test File - performs individual tests on the subroutines.
          Must pass tests for display to run correctly
"""

# Imports
import Scheduler
import datetime

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

    # Check that fetch time and fetch date function correctly
    # Note - ignores seconds when testing. Can fail is tested close to the change of a minute or hour due to latency
    assert datetime.datetime.now().time().minute == Scheduler.FetchTime().minute, "FetchTime() incorrect - min"
    assert datetime.datetime.now().time().hour == Scheduler.FetchTime().hour, "FetchTime() incorrect - hour "
    assert datetime.date.today() == Scheduler.FetchDate(), "FetchDate() incorrect"

    # Initialize test arrays - holds sets of dates and times to validate with
    test_dates = [datetime.date.fromisoformat("2022-08-15"),    # Valid date, valid time
                  datetime.date.fromisoformat("2022-08-15"),    # Valid date, invalid hour
                  datetime.date.fromisoformat("2022-08-19"),    # Valid date, invalid minute
                  datetime.date.fromisoformat("2022-08-20"),    # Invalid date, valid time
                  datetime.date.fromisoformat("2023-08-21"),    # Invalid date, invalid time
                  datetime.date.fromisoformat("2024-02-29"),    # Leap date, valid time
                  datetime.date.fromisoformat("2024-02-29"),    # Leap date, invalid time
                  datetime.date.fromisoformat("2000-01-01")]    # Invalid date

    test_times = [datetime.time.fromisoformat("12:00:00"),      # Valid date, valid time
                  datetime.time.fromisoformat("00:00:00"),      # Valid date, invalid hour
                  datetime.time.fromisoformat("07:15:00"),      # Valid date, invalid minute
                  datetime.time.fromisoformat("12:00:00"),      # Invalid date, valid time
                  datetime.time.fromisoformat("03:00:00"),      # Invalid date, invalid time
                  datetime.time.fromisoformat("12:00:00"),      # Leap date, valid time
                  datetime.time.fromisoformat("04:00:00"),      # Leap date, invalid hour
                  datetime.time.fromisoformat("09:00:00")]      # Invalid date

    # Initialize validation answer array - holds the expected validation values
    test_validation = [0, -2, -1, -3, -2, 0, -2, -4]

    # Loop through all test cases and assert validation status
    for index in range(len(test_validation)):
        print("\t\tExamining test case : ", index)
        assert test_validation[index] == Scheduler.ValidateTime(test_times[index], test_dates[index]), \
            "Validation incorrect"

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

