"""
DEPRECATED FILE. MOVED TO RunDisplay.py

MSD P22385
Themed Entertainment Model Display
File    : Activator.py
Author  : Harrison Barnes
Date    : 07/25/2022
Purpose : Driver program for the Activator subroutine
"""

# Includes
import Activate
import RPi.GPIO as GPIO
import time

"""
Function : ActivatorDriver
Inputs   : None
Outputs  : Return code based on user IO status or time out

Performs GPIO signal output to activate the magnetic launch.
"""
def ActivatorDriver():
    # Initialize GPIO pins for PWM output
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Activate.ACTIVATOR_BRAKE_PWM_PIN, GPIO.OUT)
    GPIO.setup(Activate.ACTIVATOR_LAUNCH_PWM_PIN, GPIO.OUT)
    
    # Initialize PWM pins with PWM widths specified in Activate.py
    brake = GPIO.PWM(Activate.ACTIVATOR_BRAKE_PWM_PIN, Activate.ACTIVATOR_BRAKE_PWM_VAL)
    launch = GPIO.PWM(Activate.ACTIVATOR_LAUNCH_PWM_PIN, Activate.ACTIVATOR_LAUNCH_PWM_VAL)
    
    # Move brake tires forward to send train to launch segment
    brake.start(0)
    brake.ChangeDutyCycle(Activate.ACTIVATOR_DUTY_CYCLE)
    time.sleep(Activate.ACTIVATOR_BRAKE_MOTOR_RUNTIME)
    brake.stop()
    
    # Activate launch tires to launch train up the track
    launch.start(0)
    launch.ChangeDutyCycle(Activate.ACTIVATOR_DUTY_CYCLE)
    time.sleep(Activate.ACTIVATOR_LAUNCH_MOTOR_RUNTIME)
    launch.stop()
    
    # Clean up GPIO pins
    GPIO.cleanup()
    
    return Activate.ACTIVATOR_LAUNCH_COMPLETED

