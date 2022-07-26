"""
MSD P22385
Themed Entertainment Model Display
File    : Activator.py
Author  : Harrison Barnes
Date    : 07/25/2022
Purpose : Driver program for the Activator subroutine
"""

# Includes
import Activate

"""
Function : ActivatorDriver
Inputs   : None
Outputs  : Return code based on user IO status or time out

Performs GPIO signal output to activate the magnetic launch.
"""
def ActivatorDriver():
    return Activate.ACTIVATOR_LAUNCH_COMPLETED

