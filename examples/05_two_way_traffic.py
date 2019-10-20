#!/usr/bin/env python

from Workshop import Ultrasonic, TrafficLight
import time

# threshold for when a car is considered present in front of the sensor
THRESH = 20
 
def main():
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

if __name__ == '__main__':
    main()
