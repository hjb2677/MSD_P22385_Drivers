"""
MSD P22385
Themed Entertainment Model Display
File    : DriverFlowCodes.py
Author  : Harrison Barnes
Date    : 07/11/2022
Purpose : Contains control codes to switch between which driver section should run
"""

# Scheduler entry code
DRIVER_ENTRY_SCHEDULER = 1000

# Idler entry code
DRIVER_ENTRY_IDLER = 2000

# Activator entry code
DRIVER_ENTRY_ACTIVATOR = 3000

# HALL Monitor entry code
DRIVER_ENTRY_HALL_MONITOR = 4000

# Error Report entry code
DRIVER_ENTRY_ERROR_REPORTER = 5000

# Exit Loop Code- Fatal Error
DRIVER_EXIT_FATAL = -9999

# Exit Loop Code - Normal End
DRIVER_EXIT_NORMAL = -8888

