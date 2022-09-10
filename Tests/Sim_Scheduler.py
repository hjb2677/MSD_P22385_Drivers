"""
MSD P22385
Themed Entertainment Model Display
File    : Sim_Scheduler.py
Author  : Harrison Barnes
Date    : 09/09/2022
Purpose : Simulates two years worth of time: Jan-01-2023 -> Jan-01-2025
Calls the scheduler each day and prints data to a text file. The text file
is formatted every month in order day. Does not test time validation, only date.
All times are set to noon
"""

import Scheduler
import Schedule
import datetime


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

    # Close file. This ends write mode and frees device memory. DO NOT REMOVE
    sim_file.close()


if __name__ == '__main__':
    mainSimSchedule()
