import RPi.GPIO as GPIO

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
