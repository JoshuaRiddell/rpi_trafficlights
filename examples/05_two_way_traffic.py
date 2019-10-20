#!/usr/bin/env python

from Workshop import Ultrasonic, TrafficLight
import time

# distance threshold for how close a car has to be to trigger the light
# (centimetres)
DISTANCE_THRESHOLD_CM = 20
 
def main():
    # make objects for ultrasonic sensors
    # parameters are pin numbers for trigger then echo
    us1 = Ultrasonic(2, 3)
    us2 = Ultrasonic(10, 9)

    # make objects for traffic lights
    # parameters are pin numbers of red, orange, green lights in order
    tl1 = TrafficLight(26, 19, 13)
    tl2 = TrafficLight(16, 20, 21)

    # both routes are stopped by default
    # turn route 1 on first
    tl1.go()

    print("Traffic light 1 is active")

    while True:
        # wait for the signal that we should switch to route 2
        while not should_exit(us1, us2):
            time.sleep(0.05)

        print("Switching to traffic light 2")

        # stop route 1, then after some delay start route 2
        tl1.stop()
        time.sleep(3)
        tl2.go()

        # wait for signal to switch back to route 1
        while not should_exit(us2, us1):
            time.sleep(0.05)

        print("Switching to traffic light 1")

        # stop route 2 and swtich back to route 1
        tl2.stop()
        time.sleep(3)
        tl1.go()


def should_exit(current_ultrasonic, other_ultrasonic):
    "Decides if we should exit the current route and switch to the other route."

    # get sensor readings
    current_reading = current_ultrasonic.read_cm()
    other_reading = other_ultrasonic.read_cm()

    print("{:5.5}cm, {:5.5}cm".format(str(current_reading), str(other_reading)))

    # check if there is a car on our route or the other route
    car_on_my_route = current_reading is not None and current_reading < DISTANCE_THRESHOLD_CM
    car_on_other_route = other_reading is not None and other_reading < DISTANCE_THRESHOLD_CM

    # if no car on my route, and car on other route, we should change
    if not car_on_my_route and car_on_other_route:
        return True
    # otherwise we should stick with the current route
    return False

if __name__ == '__main__':
    main()
