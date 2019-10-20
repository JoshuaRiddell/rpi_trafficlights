import RPi.GPIO as GPIO

def setup():
    # setup rpi gpio global settings
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
