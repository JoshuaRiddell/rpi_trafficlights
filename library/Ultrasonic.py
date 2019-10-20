import RPi.GPIO as GPIO


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