# import the GPIO module
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set a value for the speed of sound
speed_of_sound = 34300  # cm/s

# set which pin number we used for the light
trigger = 2
echo = 3

# setup the pin as an output
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

# send pulse
GPIO.output(trigger, True)
time.sleep(0.0001)
GPIO.output(trigger, False)

# wait for 3 seconds
while GPIO.input(echo) == 0:
    start = time.time()
while GPIO.input(echo) == 1:
    end = time.time()

# calculate distance
pulse_length = end - start
dist = (pulse_length * speed_of_sound) / 2

print("Pulse length was", pulse_length, "seconds")
print("Distance was", dist, "cm")
