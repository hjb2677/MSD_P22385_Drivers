"""
MSD P22385
Themed Entertainment Model Display
File    : HallMonitor.py
Author  : Harrison Barnes
Date    : 12/07/2022
Purpose : Driver program for the Hall Monitor and Activator. Replaces
deprecated HallMonitor.py and Activator.py
"""

# Import headers and relevant libraries
import HallHeader
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1x15 import Mode
import Activate
import RPi.GPIO as GPIO
import time
import ErrorCodes

"""
Function : RunDisplayDriver
Inputs   : none
Outputs  : ReturnCode specifying if the train completed the full loop and came to a stop

Performs peripheral set up (ADC and PWM pins) and then begins launch sequence, monitoring, and braking.
This function is as optimized as possible in Python due to the required speed of the algorithm. This means
loop unrolling, less function calls, etc.


HES to Pin Map

HES0 = ADS1 P3 - Between brake and launch
HES1 = ADS1 P0 - Top of rollercoaster right after launch
HES2 = ADS2 P0 - Valley point 0
HES3 = ADS2 P3 - Valley point 1
HES4 = ADS1 P1 - Right before brake run

HES's are listed in order they appear on the track

"""
def RunDisplayDriver():
    # HMFRG holds the values for the hall monitors
    HMFRG = [0, 0, 0, 0, 0]

    # Set up peripheral: ADCs
    # Initialize the i2c protocol to interface with the boards
    i2c = busio.I2C(board.SCL, board.SDA)
    
    # Initialize the ADC in continuous mode
    # ads = ADS.ADS1015(i2c)
    ads1 = ADS.ADS1015(i2c, address=0x48)
    ads2 = ADS.ADS1015(i2c, address=0x49)
    ads1.mode = Mode.CONTINUOUS
    ads2.mode = Mode.CONTINUOUS
    
    # ADC ready to read. Now set up PWMs for motors
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Activate.ACTIVATOR_BRAKE_PWM_PIN, GPIO.OUT)
    GPIO.setup(Activate.ACTIVATOR_LAUNCH_PWM_PIN, GPIO.OUT)
    # Set GPIO PWM to designated value
    brakeTireMotor = GPIO.PWM(Activate.ACTIVATOR_BRAKE_PWM_PIN, Activate.ACTIVATOR_BRAKE_PWM_VAL)
    launchTireMotor = GPIO.PWM(Activate.ACTIVATOR_LAUNCH_PWM_PIN, Activate.ACTIVATOR_LAUNCH_PWM_VAL)
    # Fix duty cycle to 50% DO NOT ALTER
    brakeTireMotor.ChangeDutyCycle(Activate.ACTIVATOR_DUTY_CYCLE)
    launchTireMotor.ChangeDutyCycle(Activate.ACTIVATOR_DUTY_CYCLE)
    
    # All peripherals are set up, release train from brake run
    brakeTireMotor.start(0)
    
    # NOTE: Polling is done as a fail safe to prevent a broken sensor from stopping the display run.
    # A spike in an HES will break the poll sequence. Other wise, continue
    
    # HES0 = ADS1 P3 - Between brake and launch
    # Poll for a spike in HES0 using a low pass filter (4 point average).
    for poll in range(HallHeader.HALL_MONITOR_HES0_POLLS):
        # Reset rolling avg to zero, removing previous poll's data
        rollingAvg = 0
        
        # Add the four passes' voltages together, shift right by 2 to divide by 4
        rollingAvg += AnalogIn(ads1, ADS.P3).voltage
        rollingAvg += AnalogIn(ads1, ADS.P3).voltage
        rollingAvg += AnalogIn(ads1, ADS.P3).voltage
        rollingAvg += AnalogIn(ads1, ADS.P3).voltage
        rollingAvg = rollingAvg >> 2
    
        # If rollingAvg matches or surpasses the HES threshold, set the corresponding HMFRG flag high
        HMFRG[0] = HMFRG[0] or (rollingAvg > HallHeader.HALL_MONITOR_HES0_THRESHOLD)
        
        if HMFRG[0] == 1:  # HES0 spiked, train is through, go on to next segment, no need to poll
            break
        
    # Train is through the brake run, kill brake motor
    brakeTireMotor.stop()
    
    # Begin launch run, start motor
    launchTireMotor.start(0)
        
    # HES1 = ADS1 P0 - Top of rollercoaster right after launch
    # Poll for a spike in HES1 using a low pass filter (4 point average).
    for poll in range(HallHeader.HALL_MONITOR_HES1_POLLS):
        # Reset rolling avg to zero, removing previous poll's data
        rollingAvg = 0
        
        # Add the four passes' voltages together, shift right by 2 to divide by 4
        rollingAvg += AnalogIn(ads1, ADS.P0).voltage
        rollingAvg += AnalogIn(ads1, ADS.P0).voltage
        rollingAvg += AnalogIn(ads1, ADS.P0).voltage
        rollingAvg += AnalogIn(ads1, ADS.P0).voltage
        rollingAvg = rollingAvg >> 2
    
        # If rollingAvg matches or surpasses the HES threshold, set the corresponding HMFRG flag high
        HMFRG[1] = HMFRG[1] or (rollingAvg > HallHeader.HALL_MONITOR_HES1_THRESHOLD)
        
        if HMFRG[1] == 1:  # HES1 spiked, train is through, go on to next segment, no need to poll
            break
        
    # Train reached top of track, wait 0.5 seconds to ensure it wont get caught on the tires
    time.sleep(HallHeader.POST_LAUNCH_WAIT)
    launchTireMotor.stop()
    
    # Train is now going through the track, poll both valley points and check to make sure it didnt valley
    # HES2 = ADS2 P0 - Valley point 0
    # Poll for a spike in HES1 using a low pass filter (4 point average).
    for poll in range(HallHeader.HALL_MONITOR_HES2_POLLS):
        # Reset rolling avg to zero, removing previous poll's data
        rollingAvg = 0
        
        # Add the four passes' voltages together, shift right by 2 to divide by 4
        rollingAvg += AnalogIn(ads2, ADS.P0).voltage
        rollingAvg += AnalogIn(ads2, ADS.P0).voltage
        rollingAvg += AnalogIn(ads2, ADS.P0).voltage
        rollingAvg += AnalogIn(ads2, ADS.P0).voltage
        rollingAvg = rollingAvg >> 2
    
        # If rollingAvg matches or surpasses the HES threshold, set the corresponding HMFRG flag high
        HMFRG[2] = HMFRG[2] or (rollingAvg > HallHeader.HALL_MONITOR_HES2_THRESHOLD)
        
        if HMFRG[2] == 1:  # HES2 spiked, train is through, go on to next segment, no need to poll
            break
    # HES3 = ADS2 P3 - Valley point 1
    # Poll for a spike in HES3 using a low pass filter (4 point average).
    for poll in range(HallHeader.HALL_MONITOR_HES3_POLLS):
        # Reset rolling avg to zero, removing previous poll's data
        rollingAvg = 0
        
        # Add the four passes' voltages together, shift right by 2 to divide by 4
        rollingAvg += AnalogIn(ads2, ADS.P3).voltage
        rollingAvg += AnalogIn(ads2, ADS.P3).voltage
        rollingAvg += AnalogIn(ads2, ADS.P3).voltage
        rollingAvg += AnalogIn(ads2, ADS.P3).voltage
        rollingAvg = rollingAvg >> 2
    
        # If rollingAvg matches or surpasses the HES threshold, set the corresponding HMFRG flag high
        HMFRG[3] = HMFRG[3] or (rollingAvg > HallHeader.HALL_MONITOR_HES3_THRESHOLD)
        
        if HMFRG[3] == 1:  # HES3 spiked, train is through, go on to next segment, no need to poll
            break
        
    # Valley points crossed, wait to approach brake run
    # HES4 = ADS1 P1 - Right before brake run
    # Poll for a spike in HES4 using a low pass filter (4 point average).
    for poll in range(HallHeader.HALL_MONITOR_HES3_POLLS):
        # Reset rolling avg to zero, removing previous poll's data
        rollingAvg = 0
        
        # Add the four passes' voltages together, shift right by 2 to divide by 4
        rollingAvg += AnalogIn(ads1, ADS.P1).voltage
        rollingAvg += AnalogIn(ads1, ADS.P1).voltage
        rollingAvg += AnalogIn(ads1, ADS.P1).voltage
        rollingAvg += AnalogIn(ads1, ADS.P1).voltage
        rollingAvg = rollingAvg >> 2
    
        # If rollingAvg matches or surpasses the HES threshold, set the corresponding HMFRG flag high
        HMFRG[4] = HMFRG[4] or (rollingAvg > HallHeader.HALL_MONITOR_HES4THRESHOLD)
        
        if HMFRG[4] == 1:  # HES4 spiked, train is through, go on to next segment, no need to poll
            break
    
    # Roll forward for 0.5 sections to move onto brake run safely
    # Begin launch run, start motor
    brakeTireMotor.start(0)
    time.sleep(HallHeader.POST_BRAKE_WAIT)
    brakeTireMotor.stop()
    
    # Handle HMFRG
    if HMFRG[4] == 0 and (HMFRG[3] == 0 or HMFRG[2] == 0) and HMFRG[1] == 1 and HMFRG[0] == 1:
        # Pre-brake run and a valley point did not trigger. Valley detected. Stop ride
        return ErrorCodes.FATAL_VALLEY
    if HMFRG[4] == 0 and (HMFRG[3] == 0 or HMFRG[2] == 0) and HMFRG[1] == 0 and HMFRG[0] == 1:
        # No activity detected after launch. Launch failed.
        return ErrorCodes.FATAL_BAD_LAUNCH
    if HMFRG[4] == 0 and (HMFRG[3] == 0 or HMFRG[2] == 0) and HMFRG[1] == 0 and HMFRG[0] == 0:
        # No activity detected at all. Brake run failed
        return ErrorCodes.FATAL_NO_BRAKE_RELEASE    
    return HallHeader.HALL_MONITOR_ALL_GOOD

