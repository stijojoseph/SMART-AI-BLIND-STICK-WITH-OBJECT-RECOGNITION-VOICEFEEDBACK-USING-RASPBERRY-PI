import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
def high(): # Run forever
 GPIO.output(18, GPIO.HIGH) # Turn on
  # Sleep for 1 second
# Sleep for 1 second
def low():
  GPIO.output(18, GPIO.LOW)
