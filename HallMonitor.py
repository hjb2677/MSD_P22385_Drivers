"""
DEPRECATED FILE. MOVED TO RunDisplay.py

MSD P22385
Themed Entertainment Model Display
File    : HallMonitor.py
Author  : Harrison Barnes
Date    : 07/26/2022
Purpose : Driver program for the Hall Monitor
"""

# Includes
import HallHeader
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1x15 import Mode

"""
HES to Pin Map

HES0 = ADS1 P3
HES1 = ADS1 P0
HES2 = ADS2 P0
HES3 = ADS2 P3
HES4 = ADS1 P1

HES's are listed in order they appear on the track
"""
def HallMonitorDriver():
    # Initialize the Hall Monitor Flag Register (HMFRG) to zeros.
    # HMFRG flags go high when their corresponding HES detects a spike during polling time
    HMFRG = [0, 0, 0, 0, 0]
    
    # Initialize the i2c protocol to interface with the boards
    i2c = busio.I2C(board.SCL, board.SDA)

    # Initialize the ADC in continuous mode
    ads = ADS.ADS1015(i2c)
    ads.mode = Mode.CONTINUOUS

    # Initialize the rolling average for the HES LPF
    rollingAvg = 0

    # Poll for a spike in HES0 using a low pass filter (4 point average).
    for poll in range(HallHeader.HALL_MONITOR_HES0_POLLS):
        # Reset rolling avg to zero, removing previous poll's data
        rollingAvg = 0
        
        # Add the four passes' voltages together, shift right by 2 to divide by 4
        rollingAvg += AnalogIn(ads, ADS.P0).voltage
        rollingAvg += AnalogIn(ads, ADS.P0).voltage
        rollingAvg += AnalogIn(ads, ADS.P0).voltage
        rollingAvg += AnalogIn(ads, ADS.P0).voltage
        rollingAvg = rollingAvg >> 2
    
        # If rollingAvg matches or surpasses the HES threshold, set the corresponding HMFRG flag high
        HMFRG[0] = HMFRG[0] or (rollingAvg > HallHeader.HALL_MONITOR_HES0_THRESHOLD)
        
    # Now repeat this process for the other 4 HES
    
    # Poll for a spike in HES1 using a low pass filter (4 point average).
    for poll in range(HallHeader.HALL_MONITOR_HES1_POLLS):
        # Reset rolling avg to zero, removing previous poll's data
        rollingAvg = 0
        
        # Add the four passes' voltages together, shift right by 2 to divide by 4
        rollingAvg += AnalogIn(ads, ADS.P1).voltage
        rollingAvg += AnalogIn(ads, ADS.P1).voltage
        rollingAvg += AnalogIn(ads, ADS.P1).voltage
        rollingAvg += AnalogIn(ads, ADS.P1).voltage
        rollingAvg = rollingAvg >> 2
    
        # If rollingAvg matches or surpasses the HES threshold, set the corresponding HMFRG flag high
        HMFRG[1] = HMFRG[1] or (rollingAvg > HallHeader.HALL_MONITOR_HES1_THRESHOLD)
        
    # Poll for a spike in HES2 using a low pass filter (4 point average).
    for poll in range(HallHeader.HALL_MONITOR_HES2_POLLS):
        # Reset rolling avg to zero, removing previous poll's data
        rollingAvg = 0
        
        # Add the four passes' voltages together, shift right by 2 to divide by 4
        rollingAvg += AnalogIn(ads, ADS.P2).voltage
        rollingAvg += AnalogIn(ads, ADS.P2).voltage
        rollingAvg += AnalogIn(ads, ADS.P2).voltage
        rollingAvg += AnalogIn(ads, ADS.P2).voltage
        rollingAvg = rollingAvg >> 2
    
        # If rollingAvg matches or surpasses the HES threshold, set the corresponding HMFRG flag high
        HMFRG[2] = HMFRG[2] or (rollingAvg > HallHeader.HALL_MONITOR_HES2_THRESHOLD)
    
    # Poll for a spike in HES3 using a low pass filter (4 point average).
    for poll in range(HallHeader.HALL_MONITOR_HES3_POLLS):
        # Reset rolling avg to zero, removing previous poll's data
        rollingAvg = 0
        
        # Add the four passes' voltages together, shift right by 2 to divide by 4
        rollingAvg += AnalogIn(ads, ADS.P3).voltage
        rollingAvg += AnalogIn(ads, ADS.P3).voltage
        rollingAvg += AnalogIn(ads, ADS.P3).voltage
        rollingAvg += AnalogIn(ads, ADS.P3).voltage
        rollingAvg = rollingAvg >> 2
    
        # If rollingAvg matches or surpasses the HES threshold, set the corresponding HMFRG flag high
        HMFRG[3] = HMFRG[3] or (rollingAvg > HallHeader.HALL_MONITOR_HES3_THRESHOLD)
    
    # TODO: HES4 requires testing the second ADC module.

    # TODO: Add HES4 here into if statement
    if HMFRG[0] and HMFRG[1] and HMFRG[2] and HMFRG[3]:
        return HallHeader.HALL_MONITOR_ALL_GOOD
    # TODO: Handle acceptable HES missed thresholds
    return HallHeader.HALL_MONITOR_NOT_GOOD
