import time
import RPi.GPIO as GPIO

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

# set GPIO Pins
GPIO_TRIGGER = 16
GPIO_ECHO = 18
LED_PIN = 11

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

# Blink LED n times with given interval between blinks
def blink_led(times, interval):
    for i in range(times):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(interval / 2)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(interval / 2)

# Function to get the distance from the ultrasonic sensor
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

# Measure distance continuously for a given duration
def read_ultrasonic_sensor(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        dist = distance()
        print("Measured Distance = %.1f cm" % dist)
        time.sleep(0.1)

# Main loop
try:
    while True:
        blink_led(4, 0.5)
        read_ultrasonic_sensor(5)
        blink_led(10, 0.2)
finally:
    GPIO.cleanup()  # Clean up on program exit or interruption
