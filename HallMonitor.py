"""
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

def HallMonitorDriver():
    # Initialize the i2c protocol to interface with the boards
    i2c = busio.I2C(board.SCL, board.SDA)

    # Initialize the ADC in continuous mode
    ads = ADS.ADS1015(i2c)
    ads.mode = Mode.CONTINUOUS

    # Read the channel P0 value and print to the terminal
    chan = AnalogIn(ads, ADS.P0)
    print(chan.value, chan.voltage)

    return HallHeader.HALL_MONITOR_ALL_GOOD
