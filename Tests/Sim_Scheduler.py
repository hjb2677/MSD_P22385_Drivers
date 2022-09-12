"""
MSD P22385
Themed Entertainment Model Display
File    : Sim_Scheduler.py
Author  : Harrison Barnes
Date    : 09/09/2022
Purpose : Simulates two years worth of time: Week 1 of 2023 to Week 1 of 2025
Calls the scheduler each day and prints data to a text file. The text file
is formatted every month in order day. Does not test time validation, only date.
All times are set to noon
"""

# Imports
import Scheduler
import Schedule
import datetime

# Defines

# Time of day constant - noon
TEST_TIME_SIM = "12:00:00"

# Holds string representation of DOW
DOW_STR = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

# Calendar years to simulate. Must include ALL year in between start and end
YEARS_TO_SIM = [2023, 2024]

# Array consisting of the number of days within a (leap) year
DAYS_IN_MON = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP_DAYS_IN_MON = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Array contains month strings to print to output file
MON_STR = ["\nJanuary\n", "\nFebruary\n", "\nMarch\n", "\nApril\n", "\nMay\n", "\nJune\n", "\nJuly\n", "\nAugust\n",
           "\nSeptember\n", "\nOctober\n", "\nNovember\n", "\nDecember\n"]

"""
Function : mainSimSchedule
Inputs   : none
Outputs  : none

Simulates a period of time and checks scheduler. Prints validation code to a text file
"""
def mainSimSchedule():
    # Print start message to terminal
    print("Beginning sim")

    # Open the simulation results file in write mode to prepare for sim output
    sim_file = open("Sim_Scheduler_Results.txt", "w")

    # Write a header to the output file
    headerLines = ["Sim_Scheduler.py Output File\n", "By: Harrison Barnes\n",
                   "Prints validation code based on the date. Listed by month\n\n"]
    sim_file.writelines(headerLines)

    for year in YEARS_TO_SIM:  # Iterate through all desired years
        sim_file.write("\n\n")
        sim_file.write(str(year))
        sim_file.write("\n")
        if IsLeapYear(year):
            for month in range(1, 13):  # Iterate through the 12 months in the year
                sim_file.write(MON_STR[month-1])
                # Iterate through all the days within the month
                # DAYS_IN_MONTH stores the amount of days within the respective month.
                # "month-1" offset aligns month with correct index
                # "+1" lets the loop terminate correctly
                for day in range(1, LEAP_DAYS_IN_MON[month-1]+1):
                    sim_file.writelines([datetime.date(year, month, day).strftime("%y-%m-%d: "),
                                         DowToStr(datetime.date(year, month, day)),
                                         " = ",
                                         str(Scheduler.ValidateTime(datetime.time.fromisoformat(TEST_TIME_SIM),
                                                                    datetime.date(year, month, day))), "\n"])
                    sim_file.write("\n")
        else:
            for month in range(1, 13):  # Iterate through the 12 months in the year
                sim_file.write(MON_STR[month-1])
                # Iterate through all the days within the month
                # DAYS_IN_MONTH stores the amount of days within the respective month.
                # "month-1" offset aligns month with correct index
                # "+1" lets the loop terminate correctly
                for day in range(1, DAYS_IN_MON[month-1]+1):
                    sim_file.writelines([datetime.date(year, month, day).strftime("%y-%m-%d: "),
                                        DowToStr(datetime.date(year, month, day)),
                                        " = ",
                                        str(Scheduler.ValidateTime(datetime.time.fromisoformat(TEST_TIME_SIM),
                                                                    datetime.date(year, month, day))), "\n"])
                    sim_file.write("\n")

    # Close file. This ends write mode and frees device memory. DO NOT REMOVE
    sim_file.close()

    # Print end sim message to terminal
    print("Sim finished")


"""
Function : IsLeapYear
Inputs   : year - an integer representation of the specified year
Outputs  : boolean value - true if leap year, false otherwise

Returns a boolean value that represents whether a year is a leap year in the Gregorian calendar system
NOTE - Simplifies the gregorian calendar leap year rules to include every fourth year. Years like 2100, 2200, etc.
are not leap years, but will be treated as such here. This is a non-issue since the display will not last 80 years
"""
def IsLeapYear(year):
    return year % 4 == 0


"""
Function : DowToStr
Inputs   : currDate - current date examined by the simulator
Outputs  : string representation of the day (3 letters)

Returns a DOW str representation for use to sim file output
"""
def DowToStr(currDate):
    return DOW_STR[currDate.isocalendar()[2] - 1]


if __name__ == '__main__':
    mainSimSchedule()
