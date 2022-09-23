"""
MSD P22385
Themed Entertainment Model Display
File    : SchedulingInterface.py
Author  : Harrison Barnes
Date    : 09/23/2022
Purpose : Interfaces the CSV user files and the Scheduler backend. Also handles CSV data validation
"""

# Includes
import csv
import datetime
import Schedule

"""
Function : InitializeSchedule
Inputs   : simcode - defaults to false. Used by the schedule simulator to edit the CSV file pathS
Outputs  : return code - returns an error code or success code based upon the CSV reader status

Reads in CSV schedule files and fills in various arrays to store the schedule in Schedule.py
Returns a success or error code
"""
def InitializeSchedule(simcode=False):
    # Sim_Scheduler.py requires a different path than the driver. This handles the simulation code to set the path
    # correctly
    if simcode:  # Adjusted path for simulator
        csvPath = "../Scheduler_CSV/"
    else:  # Default path for driver
        csvPath = "Scheduler_CSV/"

    # Read Invalid_Dates.csv into INVALID_DATE_ARRAY
    with open(csvPath + "Invalid_Dates.csv", newline="") as csvFile:  # Open csv file with invalid dates
        # Initialize the reader and skip column header line (first line)
        reader = csv.reader(csvFile)
        next(reader)

        for row in reader:  # Iterate through all rows with data and store the data into the correct array
            Schedule.INVALID_DATE_ARRAY.append(row[0] + "-" + row[1] + "-" + row[2])
    # Close csv file to free up memory
    csvFile.close()

    # Read Override_Dates.csv into VALID_OVERRIDE_DATE_ARRAY
    with open(csvPath + "Override_Dates.csv", newline="") as csvFile:  # Open csv file with valid override dates
        # Initialize the reader and skip column header line (first line)
        reader = csv.reader(csvFile)
        next(reader)

        for row in reader:  # Iterate through all rows with data and store the data into the correct array
            Schedule.VALID_OVERRIDE_DATE_ARRAY.append(row[0] + "-" + row[1] + "-" + row[2])
    # Close csv file to free up memory
    csvFile.close()

    # Read Invalid_Weeks.csv into INVALID_WEEK_ARRAY
    with open(csvPath + "Invalid_Weeks.csv", newline="") as csvFile:  # Open csv file with invalid weeks
        # Initialize the reader and skip column header line (first line)
        reader = csv.reader(csvFile)
        next(reader)

        for row in reader:  # Iterate through all rows with data and store the data into the correct array
            Schedule.INVALID_WEEK_ARRAY.append((int(row[0]), int(row[1])))
    # Close csv file to free up memory
    csvFile.close()

    # Read Invalid_Months.csv into INVALID_MONTH_ARRAY
    with open(csvPath + "Invalid_Months.csv", newline="") as csvFile:  # Open csv file with invalid months
        # Initialize the reader and skip column header line (first line)
        reader = csv.reader(csvFile)
        next(reader)

        for row in reader:  # Iterate through all rows with data and store the data into the correct array
            Schedule.INVALID_MONTH_ARRAY.append(int(row[0]))
    # Close csv file to free up memory
    csvFile.close()

    # Read Invalid_DOW.csv into INVALID_DOW_ARRAY
    with open(csvPath + "Invalid_DOW.csv", newline="") as csvFile:  # Open csv file with invalid days of week
        # Initialize the reader and skip column header line (first line)
        reader = csv.reader(csvFile)
        next(reader)

        for row in reader:  # Iterate through all rows with data and store the data into the correct array
            Schedule.INVALID_DOW_ARRAY.append(int(row[0]))
    # Close csv file to free up memory
    csvFile.close()

    # Read Daily_Schedule.csv into open and close time
    with open(csvPath + "Daily_Schedule.csv", newline="") as csvFile:  # Open csv file with daily open and close times
        # Initialize the reader and skip column header line (first line)
        reader = csv.reader(csvFile)
        next(reader)

        # Read opening times
        row = next(reader)  # Move to open times
        Schedule.OPEN_HR = int(row[0])
        Schedule.OPEN_MN = int(row[1])

        # Read closing times
        row = next(reader)  # Move to close times
        Schedule.CLOSE_HR = int(row[0])
        Schedule.CLOSE_MN = int(row[1])
    # Close csv file to free up memory
    csvFile.close()

    return Schedule.CSV_SUCCESS

