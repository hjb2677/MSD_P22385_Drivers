"""
MSD P22385
Themed Entertainment Model Display
File    : Idle.py
Author  : Harrison Barnes
Date    : 07/23/2022
Purpose : Header for the Idler. Holds related constants
"""

# Time out code - returned to the idler if a timer out is reached
IDLER_TIME_OUT_DETECTED = 2469

# Voltage switch detected - the GPIO voltage has switched from logic 0 to 1, or vice versa
IDLER_GPIO_SWITCH_DETECTED = 2470

# User IO detected - GPIO voltage state held, user IO is detected
IDLER_GPIO_IO_DETECTED = 2471

# Time out limit - time elapsed from Idler start to time out of Idler (sec)
IDLER_TIME_BEFORE_TIME_OUT = 300

# State stability check - time from switch detected to determining if the state is stable (ms)
#   Set based upon the switching characteristics of the hardware
IDLER_STATE_IS_STABLE = 150

