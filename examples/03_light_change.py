# import the GPIO module
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set which pin number we used for the light
light_red = 26
light_yellow = 19
light_green = 13

# setup the pin as an output
GPIO.setup(light_red, GPIO.OUT)
GPIO.setup(light_yellow, GPIO.OUT)
GPIO.setup(light_green, GPIO.OUT)

# turn the light on
GPIO.output(light_red, False)
GPIO.output(light_yellow, False)
GPIO.output(light_green, True)

# wait for 5 seconds
time.sleep(3)

# switch to amber light
GPIO.output(light_red, False)
GPIO.output(light_yellow, True)
GPIO.output(light_green, False)

# wait for 2 seconds
time.sleep(3)

# turn the light off
GPIO.output(light_red, True)
GPIO.output(light_yellow, False)
GPIO.output(light_green, False)

time.sleep(5)
