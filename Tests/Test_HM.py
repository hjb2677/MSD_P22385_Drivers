"""
MSD P22385
Themed Entertainment Model Display
File    : Test_HM.py
Author  : Harrison Barnes
Date    : 11/09/2022
Purpose : Tests the Hall Monitor System routine
"""

# Includes
# import HallHeader
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1x15 import Mode
import time

"""
HES to Pin Map

HES0 = ADS1 P3
HES1 = ADS1 P0
HES2 = ADS2 P0
HES3 = ADS2 P3
HES4 = ADS1 P1

HES's are listed in order they appear on the track
"""
def main():
    volt_thresh = 0.0

    # HMFRG holds the values for the hall monitors
    HMFRG = [0, 0, 0, 0, 0]

    # Initialize the i2c protocol to interface with the boards
    i2c = busio.I2C(board.SCL, board.SDA)

    # Initialize the ADC in continuous mode
    # ads = ADS.ADS1015(i2c)
    ads1 = ADS.ADS1015(i2c, address=0x48)
    ads2 = ADS.ADS1015(i2c, address=0x49)
    ads1.mode = Mode.CONTINUOUS
    ads2.mode = Mode.CONTINUOUS



    while(True):
        # Read the channel values and store them into the corresponding HMFRG bit
        HMFRG[0] = AnalogIn(ads1, ADS.P3).voltage
        HMFRG[1] = AnalogIn(ads1, ADS.P0).voltage
        HMFRG[2] = AnalogIn(ads2, ADS.P0).voltage
        HMFRG[3] = AnalogIn(ads2, ADS.P3).voltage
        HMFRG[4] = AnalogIn(ads1, ADS.P3).voltage
        if(HMFRG[0] > volt_thresh or HMFRG[1] > volt_thresh or HMFRG[2] > volt_thresh or HMFRG[3] > volt_thresh or HMFRG[4] > volt_thresh):
            print("HMFRG 0\tHMFRG 1\tHMFRG 2\tHMFRG 3\tHMFRG 4")
            print(str(HMFRG[0]) + " " + str(HMFRG[1]) + " " + str(HMFRG[2]) + " " + str(HMFRG[3]) + " " + str(HMFRG[4]))
        time.sleep(1)

if __name__ == '__main__':
    main()
