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
from enum import Enum, unique

"""
Class : DataKind - Enumerate Type (ENUM)

DataKind represents the kind of data taken from the CSV file. Used to select validation bounds
and make other informed decisions based upon the kind of data.

Marked as @unique to ensure no indices overlap when accessing the boundary arrays
"""
@unique
class DataKind(Enum):
    DAY = 0
    DOW = 1
    WEEK = 2
    MONTH = 3
    YEAR = 4
    HOUR = 5
    MINUTE = 6


"""
Integer validation arrays hold the lower and upper boundaries allowed by the CSV validator.
Indices are accessed using the DataKind enumerated type. 
Arrays are constants to save memory access time. Although not critical for this section, it is nice to have
Listed in order with explanation:
    DAY    - ISO is 1-28,29,30,31 based on Month. Use 1-31 for all inclusive
    DOW    - ISO is 1-7 for Monday through Sunday
    WEEK   - ISO is 1-52,53 based on Year, Use 1-53 for all inclusive
    MONTH  - ISO is 1-12 for January through December
    YEAR   - 2022 is the starting year, use as lower. 2040 is well beyond expected life, use as upper
    HOUR   - ISO is 0-23 from midnight to 11 pm. 0 is lower bound, 23 is upper bound
    MINUTE - ISO is 0-59 for every minute in an hour, use this as bounds
"""
LOWER_BOUNDS = [1,  1, 1,  1,  2022, 0,  0]
UPPER_BOUNDS = [31, 7, 53, 12, 2040, 23, 59]

"""
Function : ValidateIntegerData
Inputs   : integerData - an integer (int) representing a single piece of data, whether a day, year, month, etc.
           kindOfData  - ENUM - the kinda of data (year, month, DOW, etc) being validated. Determines bounds
Outputs  : return code - returns an error code or success code based upon the CSV data validity

Examines integer data from a CSV file and validates it within provided bounds. Returns whether the data lies
within the desires range.
"""
def ValidateIntegerData(integerData, kind):
    # Evaluated whether the integer lies within [lower, upper] and returns a valid or invalid code. Ternary operator.
    # Uses kind (DataKind ENUM) to get the index of the boundaries within the constant boundary arrays
    return Schedule.CSV_DATA_VALID \
        if LOWER_BOUNDS[kind.value] <= integerData <= UPPER_BOUNDS[kind.value] \
        else Schedule.CSV_DATA_INVALID


"""
Function : ValidateDateData
Inputs   : year, month, day - the ISO calendar year, month, and day numbers, respectively
Outputs  : return code - returns an error code or success code based upon the CSV data validity
           kind - the DataKind enum value representing which, if any, ISO date part failed

Examines integer data from a CSV file and validates it within provided bounds. Returns whether the data lies
within the desires range. Calls ValidateIntegerData() for the year, month, and date
"""
def ValidateDateData(year, month, day):
    if ValidateIntegerData(year, DataKind.YEAR) == Schedule.CSV_DATA_INVALID:  # If year is invalid
        return Schedule.CSV_DATA_INVALID, DataKind.YEAR  # Return invalid code, indicate year is wrong
    elif ValidateIntegerData(month, DataKind.MONTH) == Schedule.CSV_DATA_INVALID:  # If month is invalid
        return Schedule.CSV_DATA_INVALID, DataKind.MONTH  # Return invalid code, indicate month is wrong
    elif ValidateIntegerData(day, DataKind.DAY) == Schedule.CSV_DATA_INVALID:  # If day is invalid
        return Schedule.CSV_DATA_INVALID, DataKind.DAY  # Return invalid code, indicate day is wrong
    else:  # No invalid codes detected, given date is ISO valid
        return Schedule.CSV_DATA_VALID, None  # Return valid code, indicate that nothing was wrong


"""
Function : InitializeSchedule
Inputs   : simcode - defaults to false. Used by the schedule simulator to edit the CSV file path
Outputs  : return code - returns an error code or success code based upon the CSV reader status

Reads in CSV schedule files and fills in various arrays to store the schedule in Schedule.py
Returns a success or error code
"""
def PrintTerminalValidationError(errorCode, lineNumber, filename, kind):
    print("\nError occurred when scanning CSV file:\n\t"+filename + " line number [" + str(lineNumber) +
          "]\n\twith error code " + str(errorCode) + "\n\tDataKind: " + kind.name + "\n\n")


"""
Function : InitializeSchedule
Inputs   : simcode - defaults to false. Used by the schedule simulator to edit the CSV file path
Outputs  : return code - returns an error code or success code based upon the CSV reader status

Reads in CSV schedule files and fills in various arrays to store the schedule in Schedule.py
Returns a success or error code
"""
def InitializeSchedule(simcode=False):
    lineNumber = 2  # Represents the current line of the file. 1 indexed. Initialized to 2, since line 1 is headers
    returnCode = Schedule.CSV_INIT_CODE  # Represents the return value CSV data validation
    errorKind = None  # Holds which kind of data was incorrect in the CSV. Use only for dates.

    # Sim_Scheduler.py requires a different path than the driver. This handles the simulation code to set the path
    # correctly
    if simcode:  # Adjusted path for simulator
        csvPath = "../Scheduler_CSV/"
    else:  # Default path for driver
        csvPath = "Scheduler_CSV/"

    # Read Invalid_Dates.csv into INVALID_DATE_ARRAY
    with open(csvPath + "Invalid_Dates.csv", newline="") as csvFile:  # Open csv file with invalid dates
        # Initialize the reader, skip column header line (first line), and reset line count to 1
        reader = csv.reader(csvFile)
        next(reader)
        lineNumber = 1

        for row in reader:  # Iterate through all rows with data and store the data into the correct array
            lineNumber += 1  # Increment line number to current line
            # Validate date entry on this row
            (returnCode, errorKind) = ValidateDateData(int(row[0]), int(row[1]), int(row[2]))
            if returnCode != Schedule.CSV_DATA_VALID:  # If bad date, throw an error message and exit
                PrintTerminalValidationError(returnCode, lineNumber, "Invalid_Dates.csv", errorKind)
                return returnCode
            Schedule.INVALID_DATE_ARRAY.append(row[0] + "-" + row[1] + "-" + row[2])
    # Close csv file to free up memory
    csvFile.close()

    # Read Override_Dates.csv into VALID_OVERRIDE_DATE_ARRAY
    with open(csvPath + "Override_Dates.csv", newline="") as csvFile:  # Open csv file with valid override dates
        # Initialize the reader, skip column header line (first line), and reset line count to 1
        reader = csv.reader(csvFile)
        next(reader)
        lineNumber = 1

        for row in reader:  # Iterate through all rows with data and store the data into the correct array
            lineNumber += 1  # Increment line number to current line
            # Validate date entry on this row
            (returnCode, errorKind) = ValidateDateData(int(row[0]), int(row[1]), int(row[2]))
            if returnCode != Schedule.CSV_DATA_VALID:  # If bad date, throw an error message and exit
                PrintTerminalValidationError(returnCode, lineNumber, "Override_Dates.csv", errorKind)
                return returnCode
            Schedule.VALID_OVERRIDE_DATE_ARRAY.append(row[0] + "-" + row[1] + "-" + row[2])
    # Close csv file to free up memory
    csvFile.close()

    # Read Invalid_Weeks.csv into INVALID_WEEK_ARRAY
    with open(csvPath + "Invalid_Weeks.csv", newline="") as csvFile:  # Open csv file with invalid weeks
        # Initialize the reader, skip column header line (first line), and reset line count to 1
        reader = csv.reader(csvFile)
        next(reader)
        lineNumber = 1

        for row in reader:  # Iterate through all rows with data and store the data into the correct array
            lineNumber += 1  # Increment line number to current line
            # Validate the year entry on this row
            returnCode = ValidateIntegerData(int(row[0]), DataKind.YEAR)
            if returnCode != Schedule.CSV_DATA_VALID:  # If bad year, throw an error message and exit
                PrintTerminalValidationError(returnCode, lineNumber, "Invalid_Weeks.csv", DataKind.YEAR)
                return returnCode
            # Validate the ISO week entry on this row
            returnCode = ValidateIntegerData(int(row[1]), DataKind.WEEK)
            if returnCode != Schedule.CSV_DATA_VALID:  # If bad ISO week, throw an error message and exit
                PrintTerminalValidationError(returnCode, lineNumber, "Invalid_Weeks.csv", DataKind.WEEK)
                return returnCode
            Schedule.INVALID_WEEK_ARRAY.append((int(row[0]), int(row[1])))
    # Close csv file to free up memory
    csvFile.close()

    # Read Invalid_Months.csv into INVALID_MONTH_ARRAY
    with open(csvPath + "Invalid_Months.csv", newline="") as csvFile:  # Open csv file with invalid months
        # Initialize the reader, skip column header line (first line), and reset line count to 1
        reader = csv.reader(csvFile)
        next(reader)
        lineNumber = 1

        for row in reader:  # Iterate through all rows with data and store the data into the correct array
            lineNumber += 1  # Increment line number to match current line
            # Validate the ISO month entry on this row
            returnCode = ValidateIntegerData(int(row[0]), DataKind.MONTH)
            if returnCode != Schedule.CSV_DATA_VALID:  # If bad ISO week, throw an error message and exit
                PrintTerminalValidationError(returnCode, lineNumber, "Invalid_Months.csv", DataKind.MONTH)
                return returnCode
            Schedule.INVALID_MONTH_ARRAY.append(int(row[0]))
    # Close csv file to free up memory
    csvFile.close()

    # Read Invalid_DOW.csv into INVALID_DOW_ARRAY
    with open(csvPath + "Invalid_DOW.csv", newline="") as csvFile:  # Open csv file with invalid days of week
        # Initialize the reader, skip column header line (first line), and reset line count to 1
        reader = csv.reader(csvFile)
        next(reader)
        lineNumber =1

        for row in reader:  # Iterate through all rows with data and store the data into the correct array
            lineNumber += 1  # Increment line number to match current line
            # Validate the ISO DOW entry on this row
            returnCode = ValidateIntegerData(int(row[0]), DataKind.DOW)
            if returnCode != Schedule.CSV_DATA_VALID:  # If bad ISO DOW, throw an error message and exit
                PrintTerminalValidationError(returnCode, lineNumber, "Invalid_DOW.csv", DataKind.DOW)
                return returnCode
            Schedule.INVALID_DOW_ARRAY.append(int(row[0]))
    # Close csv file to free up memory
    csvFile.close()

    # Read Daily_Schedule.csv into open and close time
    with open(csvPath + "Daily_Schedule.csv", newline="") as csvFile:  # Open csv file with daily open and close times
        # Initialize the reader and skip column header line (first line)
        # Note - line numbers are hard coded here due to the CSV format needing only 2 data lines
        reader = csv.reader(csvFile)
        next(reader)

        # Read opening times
        row = next(reader)  # Move to open times
        Schedule.OPEN_HR = int(row[0])
        # Validate the hour entry on this row
        returnCode = ValidateIntegerData(int(row[0]), DataKind.HOUR)
        if returnCode != Schedule.CSV_DATA_VALID:  # If bad hour, throw an error message and exit
            PrintTerminalValidationError(returnCode, 2, "Daily_Schedule.csv", DataKind.HOUR)
            return returnCode
        Schedule.OPEN_MN = int(row[1])
        # Validate the minute entry on this row
        returnCode = ValidateIntegerData(int(row[1]), DataKind.MINUTE)
        if returnCode != Schedule.CSV_DATA_VALID:  # If bad minute, throw an error message and exit
            PrintTerminalValidationError(returnCode, 2, "Daily_Schedule.csv", DataKind.MINUTE)
            return returnCode

        # Read closing times
        row = next(reader)  # Move to close times
        Schedule.CLOSE_HR = int(row[0])
        # Validate the hour entry on this row
        returnCode = ValidateIntegerData(int(row[0]), DataKind.HOUR)
        if returnCode != Schedule.CSV_DATA_VALID:  # If bad hour, throw an error message and exit
            PrintTerminalValidationError(returnCode, 3, "Daily_Schedule.csv", DataKind.HOUR)
            return returnCode
        Schedule.CLOSE_MN = int(row[1])
        # Validate the minute entry on this row
        returnCode = ValidateIntegerData(int(row[1]), DataKind.MINUTE)
        if returnCode != Schedule.CSV_DATA_VALID:  # If bad minute, throw an error message and exit
            PrintTerminalValidationError(returnCode, 3, "Daily_Schedule.csv", DataKind.MINUTE)
            return returnCode
    # Close csv file to free up memory
    csvFile.close()

    return Schedule.CSV_SUCCESS

