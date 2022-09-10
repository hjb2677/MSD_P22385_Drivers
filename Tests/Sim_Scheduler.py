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

# Calendar years to simulate. Must include ALL year in between start and end
YEARS_TO_SIM = [2022]

# Array consisting of the number of days within a (leap) year
DAYS_IN_MON = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP_DAYS_IN_MON = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

"""
Function : mainSimSchedule
Inputs   : none
Outputs  : none

Simulates a period of time and checks scheduler. Prints validation code to a text file
"""
def mainSimSchedule():
    # Open the simulation results file in write mode to prepare for sim output
    sim_file = open("Sim_Scheduler_Results.txt", "w")

    # Write a header to the output file
    headerLines = ["Sim_Scheduler.py Output File\n", "By: Harrison Barnes\n",
                   "Prints validation code based on the date. Listed by month\n\n"]
    sim_file.writelines(headerLines)

    for year in YEARS_TO_SIM:  # Iterate through all desired years
        sim_file.write("\nNEW YEAR HERE\n")
        for month in range(1, 12):  # Iterate through the 12 months in the year
            sim_file.write("\nNEW MONTH HERE\n")
            # Iterate through all the days within the month
            # DAYS_IN_MONTH stores the amount of days within the respective month.
            # "month-1" offset aligns month with correct index
            # "+1" lets the loop terminate correctly
            for day in range(1, DAYS_IN_MON[month-1]+1):
                sim_file.write(datetime.date(year, month, day).strftime("%y-%m-%d\n"))

    # Close file. This ends write mode and frees device memory. DO NOT REMOVE
    sim_file.close()


if __name__ == '__main__':
    mainSimSchedule()
