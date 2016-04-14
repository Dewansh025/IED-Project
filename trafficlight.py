import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
red = 14
yellow = 15
green = 18
button = 23
buzzer = 25
GPIO.setup(red,GPIO.OUT)
GPIO.setup(yellow,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(button,GPIO.IN,PULL_up_down=GPIO.PUD_UP)
try:
    while True:
        GPIO.output(green,1)
        print("Green Lights vars in motion")
        sleep(0.2)
        if GPIO.input(button)== False:
            GPIO.output(green,0)
            GPIO.output(yellow,1)
            sleep(3)
            GPIO.output(yellow,0)
            GPIO.output(red,1)
            for i in range(10):
                print("W A L K")
                GPIO.output(green,1)
                GPIO.output(buzzer,1)
                sleep(0.2)
