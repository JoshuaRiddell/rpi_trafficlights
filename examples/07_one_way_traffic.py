#!/usr/bin/env python

from Workshop import Ultrasonic, TrafficLight
import time

# distance threshold for how close a car has to be to trigger the light
# (centimetres)
DISTANCE_THRESHOLD_CM = 20
 
def main():
    # make objects for ultrasonic sensors
    # parameters are pin numbers for trigger then echo
    us = Ultrasonic(2, 3)

    # make objects for traffic lights
    # parameters are pin numbers of red, orange, green lights in order
    tl = TrafficLight(26, 19, 13)

    # both routes are stopped by default

    print("Traffic light 1 is stopped")

    while True:

        while True:
            distance = us.read_cm()

            print("Ultrasonic distance:", distance, "cm")
            
            if distance is not None \
                    and distance < DISTANCE_THRESHOLD_CM:
                break

            time.sleep(0.05)

        
        print("Traffic light 1 starting")

        # stop route 1, then after some delay start route 2
        time.sleep(2)
        tl.go()
        time.sleep(3)
        tl.stop()

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
