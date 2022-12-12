"""
Test file for PWM
"""

import RPi.GPIO as GPIO
import time

def main():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT) 
    # p = GPIO.PWM(12, 300)
    p = GPIO.PWM(12, 350)
    q = GPIO.PWM(33, 500)
    p.start(0)
    p.ChangeDutyCycle(50)
    #time.sleep(5)
    q.start(0)
    q.ChangeDutyCycle(50)
    time.sleep(1)
    p.stop()
    time.sleep(9)
    q.stop()
    GPIO.cleanup()


if __name__ == "__main__":
    main()
