import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
n = 8
number = [0] * n

for i in range(n):
    number[i] = random.randint(0, 1)

GPIO.output(dac, number)
print(number)
time.sleep(20)

GPIO.output(dac, 0)
GPIO.cleanup()


    

