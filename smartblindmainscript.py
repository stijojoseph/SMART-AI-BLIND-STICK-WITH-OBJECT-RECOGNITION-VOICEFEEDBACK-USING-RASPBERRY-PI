import RPi.GPIO as GPIO
import blind1 as b
import time
import speak as s
import gyro2 as gy
import led as l
GPIO.setmode(GPIO.BCM)
TRIG = 23
i=0
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
while True:
 print ("Waiting For Sensor To Settle")

 time.sleep(0.1)

 GPIO.output(TRIG, True)

 time.sleep(0.00001)

 GPIO.output(TRIG, False)


 while GPIO.input(ECHO)==0:

  pulse_start = time.time()
 while GPIO.input(ECHO)==1:

  pulse_end = time.time()
  
 pulse_duration = pulse_end - pulse_start

 distance = pulse_duration*17150

 distance = round(distance, 2)
 if distance <40:
     l.high()
     b.blinds()
     l.low()
 print ("Distance:",distance,"cm")
 i=gy.scope(i)
GPIO.cleanup()