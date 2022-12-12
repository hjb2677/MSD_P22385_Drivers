"""
MSD P22385
Themed Entertainment Model Display
File    : HallHeader.py
Author  : Harrison Barnes
Date    : 07/26/2022
Purpose : Header file for the Hall Monitor, holding return codes and constants
"""

# Hall Effect Sensor (HES) thresholds (V)
HALL_MONITOR_HES0_THRESHOLD = 1.7
HALL_MONITOR_HES1_THRESHOLD = 1.7
HALL_MONITOR_HES2_THRESHOLD = 1.7
HALL_MONITOR_HES3_THRESHOLD = 1.7
HALL_MONITOR_HES4_THRESHOLD = 1.7

# Hall Effect Sensor Poll Iterations
HALL_MONITOR_HES0_POLLS = 100
HALL_MONITOR_HES1_POLLS = 100
HALL_MONITOR_HES2_POLLS = 100
HALL_MONITOR_HES3_POLLS = 100
HALL_MONITOR_HES4_POLLS = 100

# Post-launch wait time (s)
POST_LAUNCH_WAIT = 0.5
POST_BRAKE_WAIT = 0.5

# All Good - Hall Monitor detects no issues, train assumed to be at rest in the brake bay
HALL_MONITOR_ALL_GOOD = 4100

# Not Good - Hall Monitor had at least one HES not trigger
HALL_MONITOR_NOT_GOOD = 4200

