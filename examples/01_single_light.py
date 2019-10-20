# import the GPIO module
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set which pin number we used for the light
light_red = 26

# setup the pin as an output
GPIO.setup(light_red, GPIO.OUT)

# turn the light on
GPIO.output(light_red, True)

# wait for 3 seconds
time.sleep(3)

# turn the light off
GPIO.output(light_red, False)
