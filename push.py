import RPi.GPIO as GPIO
import time

button = 15
led    = 18



GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)



              button_state = GPIO.input(button)
              if  button_state == False:
                  
                  print('Button Pressed...')
              elif  button_state== True:
                    time.sleep(0.2)
                    print("not press")
                    
             


setup()
loop()

