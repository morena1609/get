import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
n = 8
number = [0] * n

number[7] = 1
number[6] = 1

GPIO.output(dac, number)
time.sleep(5)
GPIO.output(dac, 0)

M = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]]
for i in range(6):
    GPIO.output(dac, M[i])
    time.sleep(10)
    GPIO.output(dac, 0)
    
GPIO.cleanup()

