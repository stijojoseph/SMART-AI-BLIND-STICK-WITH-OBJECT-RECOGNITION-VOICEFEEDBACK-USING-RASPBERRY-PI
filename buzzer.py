import RPi.GPIO as GPIO
from time import sleep
import time
#Disable warnings (optional)
GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM  
GPIO.setup(25, GPIO.OUT)# set GPIO 25 as an output. You can use any GPIO port  
p = GPIO.PWM(25, 50)    # create an object p for PWM on port 25 at 50 Hertz  
def buz():
 p.start(70)             # start the PWM on 70 percent duty cycle  

 p.ChangeFrequency(800)
 time.sleep(1)  
  # change the frequency to x Hz (
def buztop():
    p.stop()
                # stop the PWM output  

