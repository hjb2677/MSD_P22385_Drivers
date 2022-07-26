"""
MSD P22385
Themed Entertainment Model Display
File    : Scheduler.py
Author  : Harrison Barnes
Date    : 04/05/2022
Purpose : Contains defines for the scheduling of the display

CRITICAL NOTE - CHECK ISO FORMAT BEFORE ADJUSTING
"""

# Invalid DOWs - ISO standard days of the week (1 = mon, 7 = sun) where the ride will not run
INVALID_DOW_ARRAY = []

# Invalid Dates - ISO formatted dates "YYYY-MM-DD" that the display will not run for. This overrides all other functions
INVALID_DATE_ARRAY = []

# Valid Override Dates - ISO formatted dates "YYYY-MM-DD" that the display will run for regardless of the month,
# date, DOW, etc. Overrides all date-based checks. Useful for things like Imagine RIT or events that fall on invalid
# DOWs or months
VALID_OVERRIDE_DATE_ARRAY = []

# Invalid Weeks - Datetime library week numbers that the ride is not supposed to run during
# Stored as 1-52 or 53 for the 52/53 weeks a year, along with their respective year.
# See documentation for ISO format
INVALID_WEEK_ARRAY = []

# Invalid Months - Datetime library month numbers that the ride is not supposed to run during
INVALID_MONTH_ARRAY = []

# Open and Close times:
# minutes (0-59)
# hours (0-23)
OPEN_HR = 0
OPEN_MN = 0
CLOSE_HR = 0
CLOSE_MN = 0

# Fetch Period - time (s) between fetching timestamp in Scheduler
#      Currently set to 5 min = 300 s
FETCH_TIMESTAMP_DELAY_S = 3

# Fetch Period TEST - time (s) between fetching timestamp in scheduler
#      when performing the scheduler test
#      Set to 5 seconds (5 s)
TEST_FETCH_TIMESTAMP_DELAY_S = 5


# Scheduler Validation codes

# Valid Time - given time of day is within operating time - DEPRECATED
VALID_TIME = 0

# Valid Time - Coaster should be running at this time, as scheduled by TPE
VALID_RUN_TIME = 1

# Invalid Minutes - hour is an operating hour, minutes are not
INVALID_MINUTE = -1

# Invalid Hours - hour is not an operating hour.
INVALID_HOUR = -2

# Invalid DOW - Day of Week is scheduled to have no operations. Overrides hour and minute validations
INVALID_DOW = -3

# Invalid Date - Specific date is specified as a non-operating date. Overrides all other validations
INVALID_DATE = -4

# Invalid Week - Specific week is specified as a non-operating week. Overrides all other validations
INVALID_WEEK = -5

# Invalid Month - Specific month is specified as a non-operating month. Overrides all other validations
INVALID_MONTH = -6

# Invalid Code - Initialization of Scheduler
INIT_CODE = -99

# CSV Return Codes
CSV_SUCCESS = 0

CSV_INIT_CODE = -1000

CSV_DATA_VALID = 1

CSV_DATA_INVALID = -1
