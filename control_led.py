import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
from time import sleep  # Import the sleep function from the time module

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BCM)  # Use physical pin numbering
GPIO.setup(
    17, GPIO.OUT, initial=GPIO.LOW
)  # Set pin 8 to be an output pin and set initial value to low (off)
while True:  # Run forever
    GPIO.output(1, GPIO.HIGH)  # Turn on
    sleep(300)  # Sleep for 1 second
    GPIO.output(1, GPIO.LOW)  # Turn off
    sleep(300)  # Sleep for 1 second
