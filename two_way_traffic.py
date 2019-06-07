#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

THRESH = 20
 
def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    us1 = Ultrasonic(3, 2)
    us2 = Ultrasonic(10, 9)

    tl1 = TrafficLight(27, 17, 4)
    tl2 = TrafficLight(13, 6, 5)

    while True:
        tl1.go()

        while not should_exit(us1, us2):
            time.sleep(0.05)

        print("Switching to tl2")

        tl1.stop()
        time.sleep(3)
        tl2.go()

        while not should_exit(us2, us1):
            time.sleep(0.05)

        print("Switching to tl1")

        tl2.stop()
        time.sleep(3)

def should_exit(my_us, their_us):
    my_reading = my_us.read()
    their_reading = their_us.read()

    print("{}, {}".format(my_reading, their_reading))

    if (my_reading is None or \
        my_reading > THRESH) and \
        their_reading is not None and \
        their_reading < THRESH:
            return True
    return False


class TrafficLight(object):
    def __init__(self, red, orange, green):
        self.red = red
        self.orange = orange
        self.green = green

        GPIO.setup(self.red, GPIO.OUT)
        GPIO.setup(self.orange, GPIO.OUT)
        GPIO.setup(self.green, GPIO.OUT)

        GPIO.output(self.red, True)
        GPIO.output(self.orange, False)
        GPIO.output(self.green, False)

    def go(self):
        GPIO.output(self.red, False)
        GPIO.output(self.green, True)

    def stop(self):
        GPIO.output(self.green, False)
        GPIO.output(self.orange, True)
        time.sleep(3)
        GPIO.output(self.orange, False)
        GPIO.output(self.red, True)


class Ultrasonic(object):
    speed_of_sound = 34300  # cmd/s

    def __init__(self, trigger, echo):
        self.trigger = trigger
        self.echo = echo

        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def read(self):
        GPIO.output(self.trigger, True)
        time.sleep(0.0001)
        GPIO.output(self.trigger, False)

        start = 0
        stop = 0

        while GPIO.input(self.echo) == 0:
            start = time.time()
        while GPIO.input(self.echo) == 1:
            stop = time.time()

        diff = stop - start
        dist = (diff * self.speed_of_sound) / 2

        if dist < 5 or dist > 100:
            # this was a glitch
            dist = None

        return dist

if __name__ == '__main__':
    main()

