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

    while subroutineID != EXIT_PROGRAM:
        print("\nUnit Test Program\nEnter one of the following subroutine choices in ALL CAPS")
        print("Selection choices...\n\tScheduler = SCH\n\tIdler = IDL\n\tActivator = ACT")
        print("\tHall Monitor = HMT\n\tError Reporter = ERR\n\tAll Subroutines = ALL\n\tExit Program = EXT")
        subroutineID = input("SubroutineID Selection: ")

        if subroutineID == TEST_SCHEDULER:
            print("\nTesting Scheduler...")
        elif subroutineID == TEST_IDLER:
            print("\nTesting Idler...")
        elif subroutineID == TEST_ACTIVATOR:
            print("\nTesting Activator...")
        elif subroutineID == TEST_HALL_MONITOR:
            print("\nTesting Hall Monitor...")
        elif subroutineID == TEST_ERROR_REPORTER:
            print("\nTesting Error Reporter...")
        elif subroutineID == TEST_ALL_SUBROUTINES:
            print("\nTesting all subroutines...")
        elif subroutineID == EXIT_PROGRAM:
            print("\nExiting program...")
        else:
            print("\nInvalid ID detected")
    print("Program concluded")


if __name__ == '__main__':
    mainUnitTest()

