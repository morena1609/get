import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    
     return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

k = GPIO.PWM(22, 2000)
k.start(100)
k.ChangeDutyCycle(100)
input("Press return to stop")
GPIO.output(21, 0)

try:
    while True:
        print("Введите duty cycle")
        dc = float(input())
        k.ChangeDutyCycle(dc)
        print("Примерное напряжение на выходе:", 3.3 * dc/100)     
finally:
    GPIO.output(dac, 0)
    GPIO.output(2, 0)
    GPIO.cleanup()
