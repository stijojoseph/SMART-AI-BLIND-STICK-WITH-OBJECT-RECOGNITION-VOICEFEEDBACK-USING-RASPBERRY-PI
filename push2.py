import RPi.GPIO as GPIO
from time import sleep
#Set warnings off (optional)
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
#Set Button and LED pins
Button = 10
LED = 24
#Setup Button and LED

#flag = 0
GPIO.cleanup()
while True:
    
   
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED,GPIO.OUT)
    button_state = GPIO.input(Button)
    print(button_state)
    if button_state == 0:
        GPIO.output(LED,GPIO.HIGH)
        print("press")
    else:
        GPIO.setmode(GPIO.BCM)
        GPIO.output(LED,GPIO.LOW)
        print("not")
    sleep(1)
    