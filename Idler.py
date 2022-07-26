"""
MSD P22385
Themed Entertainment Model Display
File    : Idler.py
Author  : Harrison Barnes
Date    : 07/23/2022
Purpose : Driver program for the Idler subroutine
"""


# Includes
import Idle

# Temp Includes for keyboard io
import sys, select

"""
Function : IdlerDriver
Inputs   : None
Outputs  : Return code based on user IO status or time out

Waits for user input via polling. Returns a time out code after some time has passed without input
"""
def IdlerDriver():
    # Thread into two pieces:
    # - Timer that handles time out calls
    # - Poller that handles waiting for GPIO pin until time out or detection of input
    print("\nThe Idler is a WIP. Returning a GPIO Detected code...\n")
    return Idle.IDLER_GPIO_IO_DETECTED


"""
Function : TimeOutHandler
Inputs   : None
Outputs  : Time out code

Waits for a specified amount of time before returning a time out code. Used to ensure that the
driver does not get stuck in the Idler due to lack of users
"""
def TimeOutHandler():
    pass


"""
Function : PollerGPIO
Inputs   : None
Outputs  : Input code

Polls for GPIO pin input of the RPi. Returns a code if valid input is detected.
Input is detected if a voltage change is detected, and the new state is held for so many iterations
"""
def PollerGPIO():
    pass

