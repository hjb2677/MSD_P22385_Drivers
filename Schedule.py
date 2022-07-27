"""
MSD P22385
Themed Entertainment Model Display
File    : Scheduler.py
Author  : Harrison Barnes
Date    : 04/05/2022
Purpose : Contains defines for the scheduling of the display
"""

# Invalid Days - days of the week (0 = mon, 6 = sun) where the ride will not run
# Set as : saturday & sunday
INVALID_DATES_ARRAY = [5, 6]

# Open and Close times:
# minutes (0-59)
# hours (0-23)
OPEN_HR = 7
OPEN_MN = 30
CLOSE_HR = 20
CLOSE_MN = 30

# Fetch Period - time (s) between fetching timestamp in Scheduler
#      Currently set to 5 min = 300 s
FETCH_TIMESTAMP_DELAY_S = 300

# Fetch Period TEST - time (s) between fetching timestamp in scheduler
#      when performing the scheduler test
#      Set to 5 seconds (5 s)
TEST_FETCH_TIMESTAMP_DELAY_S = 5


# Scheduler Validation codes

# Valid Time - given time of day is within operating time
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

# Invalid Code - Initialization of Scheduler
INIT_CODE = -99
