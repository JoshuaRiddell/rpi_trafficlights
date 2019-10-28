# import the GPIO module
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# define some functions to be used later
def red_light_on():
    # turn the light on
    GPIO.output(light_red, True)

def red_light_off():
    # turn the light off
    GPIO.output(light_red, False)

# setup the light pin
light_red = 26
GPIO.setup(light_red, GPIO.OUT)

# use our functions
red_light_on()
time.sleep(3)
red_light_off()
