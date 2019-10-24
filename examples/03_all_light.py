# import the GPIO module
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set which pin number we used for the lights
light_red = 26
light_yellow = 19
light_green = 13

# setup the pins as an output
GPIO.setup(light_red, GPIO.OUT)
GPIO.setup(light_yellow, GPIO.OUT)
GPIO.setup(light_green, GPIO.OUT)

def red_light_on():
    # turn the light on
    GPIO.output(light_red, True)

def red_light_off():
    # turn the light off
    GPIO.output(light_red, False)

def yellow_light_on():
    # turn the light on
    GPIO.output(light_yellow, True)

def yellow_light_off():
    # turn the light off
    GPIO.output(light_yellow, False)

def green_light_on():
    # turn the light on
    GPIO.output(light_green, True)

def green_light_off():
    # turn the light off
    GPIO.output(light_green, False)

# turn all the lights on
red_light_on()
green_light_on()
yellow_light_on()

# wait for 3 seconds
time.sleep(3)

# turn all the lights off
red_light_off()
green_light_off()
yellow_light_off()
