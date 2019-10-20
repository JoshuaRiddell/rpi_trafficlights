#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# threshold for when a car is considered present in front of the sensor
THRESH = 20
 
def main():
    # setup rpi gpio global settings
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # make objects for ultrasonic sensors
    # parameters are pin numbers for trigger and echo
    us1 = Ultrasonic(2, 3)
    us2 = Ultrasonic(10, 9)

    # make objects for traffic lights
    # parameters are pin numbers of red, orange, green lights respecively
    tl1 = TrafficLight(26, 19, 13)
    tl2 = TrafficLight(16, 20, 21)

    # turn route 1 on first
    tl1.go()

    print("Traffic light 1 is active")

    while True:
        # wait for the signal that we should switch to route 2
        while not should_exit(us1, us2):
            time.sleep(0.05)

        print("Switching to tl2")

        # stop route 1, then after some delay start route 2
        tl1.stop()
        time.sleep(3)
        tl2.go()

        # wait for signal to switch back to route 1
        while not should_exit(us2, us1):
            time.sleep(0.05)

        print("Switching to tl1")

        # stop route 2 and swtich back to route 1
        tl2.stop()
        time.sleep(3)
        tl1.go()


def should_exit(my_us, their_us):
    "Decides if we should exit the current route and switch to the other route."

    # get sensor readings
    my_reading = my_us.read_cm()
    their_reading = their_us.read_cm()

    print("{}, {}".format(my_reading, their_reading))

    # compare with thresholds
    # this logic says: if there is no car on my route, and there
    #   is a car on the other route, switch
    if (my_reading is None or \
        my_reading > THRESH) and \
        their_reading is not None and \
        their_reading < THRESH:
            return True
    return False


class TrafficLight(object):
    """A traffic light consisting of a red, orange and green light controlled
    by GPIOs."""
    def __init__(self, red, orange, green):
        "Set pin modes and initial state of light (stopped)."
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
        "Change lights to indicate 'go' on this route."
        GPIO.output(self.red, False)
        GPIO.output(self.green, True)

    def stop(self):
        "Change lights to indicate stop on this route."
        GPIO.output(self.green, False)
        GPIO.output(self.orange, True)
        time.sleep(3)
        GPIO.output(self.orange, False)
        GPIO.output(self.red, True)


class Ultrasonic(object):
    speed_of_sound = 34300  # cm/s

    def __init__(self, trigger, echo):
        "Set pin modes."
        self.trigger = trigger
        self.echo = echo

        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def read_cm(self):
        """Send a pulse down the trigger line. Busywait for a pulse coming
        back on the echo line. Based on that pulse length, calculate sensor
        distance reading. If reading is out of reasonable bounds, return None.
        """

        # send pulse
        GPIO.output(self.trigger, True)
        time.sleep(0.0001)
        GPIO.output(self.trigger, False)

        start = 0
        stop = 0

        # measure return pulse
        while GPIO.input(self.echo) == 0:
            start = time.time()
        while GPIO.input(self.echo) == 1:
            stop = time.time()

        # calculate distance
        diff = stop - start
        dist = (diff * self.speed_of_sound) / 2

        # basic error checking on distance value
        if dist < 5 or dist > 100:
            dist = None

        return dist

if __name__ == '__main__':
    main()

