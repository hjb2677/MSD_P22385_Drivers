"""
MSD P22385
Themed Entertainment Model Display
File    : ErrorCodes.py
Author  : Harrison Barnes
Date    : 07/11/2022
Purpose : Contains error codes for all errors
"""

# Nominal Status - zero error code denotes the program is in normal state
NOMINAL_STATE = 0

# Unknown Control Code - identifies if a control code is not assigned to a control driver
WARN_UNKNOWN_CTRL_CODE = 80

# Scheduler encountered random error when validating and fetching
WARN_SCHEDULER_ERROR_OCCURRED = 1999

# Repeated nominal error, fatal exit
FATAL_REPEATED_BACK2BACK_NOM_ERR = -1010

# Critical HES did not trigger
FATAL_HMFRG_HES_CRIT_MISS = -8080

# Deprecated Section Entered
FATAL_DEPRECATED_ENTRY_DETECTED = -4000

# Errors related to HMFRG in the HallMonitor (RunDisplay.py)
FATAL_VALLEY = -1984
FATAL_BAD_LAUNCH = -1985
FATAL_NO_BRAKE_RELEASE = -1986