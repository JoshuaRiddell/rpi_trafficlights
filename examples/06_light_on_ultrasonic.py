# import the GPIO module
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set a value for the speed of sound
speed_of_sound = 34300  # cm/s

# set which pin number we used for the ultrasonic pins
trigger = 2
echo = 3
light_red = 26

# setup the pin as an output
GPIO.setup(light_red, GPIO.OUT)

# setup the pins to their modes
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)


def light_on():
    # turn the light on
    GPIO.output(light_red, True)

def light_off():
    # turn the light off
    GPIO.output(light_red, False)

def read_cm():
    # send a pulse to trigger the ultrasonic ping
    GPIO.output(trigger, True)
    time.sleep(0.0001)
    GPIO.output(trigger, False)

    # measure the pulse length of the reply
    start = time.time()
    end = time.time()

    while GPIO.input(echo) == 0:
        start = time.time()
    while GPIO.input(echo) == 1:
        end = time.time()

    # calculate the distance of the object using the speed of sound
    pulse_length = end - start
    dist = (pulse_length * speed_of_sound) / 2
    
    return dist


while True:
    dist = read_cm()
    print(dist)
    if dist < 20:
        light_on()
    else:
        light_off()

    time.sleep(0.05)
