"""
MSD P22385
Themed Entertainment Model Display
File    : Test_HM.py
Author  : Harrison Barnes
Date    : 11/09/2022
Purpose : Tests the Hall Monitor System routine
"""

# Includes
import HallHeader
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1x15 import Mode

def main():
    voltage_threshold = 1.72

    # HMFRG holds the values for the hall monitors
    HMFRG = [0, 0, 0, 0, 0]

    # Initialize the i2c protocol to interface with the boards
    i2c = busio.I2C(board.SCL, board.SDA)

    # Initialize the ADC in continuous mode
    ads = ADS.ADS1015(i2c)
    ads.mode = Mode.CONTINUOUS

    # Read the channel values and store them into the corresponding HMFRG bit
    while(True):
        HMFRG[0] = AnalogIn(ads, ADS.P0).voltage
        HMFRG[1] = AnalogIn(ads, ADS.P1).voltage
        HMFRG[2] = AnalogIn(ads, ADS.P2).voltage
        HMFRG[3] = AnalogIn(ads, ADS.P3).voltage

        if(HMFRG[0] > voltage_threshold or HMFRG[2] > voltage_threshold or
                HMFRG[2] > voltage_threshold or HMFRG[3] > voltage_threshold):
            print("HMFRG: " + str(HMFRG[0]) + " " + str(HMFRG[1]) + " " + str(HMFRG[2]) + " " + str(HMFRG[3]))


if __name__ == '__main__':
    main()