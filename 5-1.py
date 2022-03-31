def dec2bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

def dec2dac(x):
    GPIO.output(dac, dec2bin(x))

def adc():
    for i in range(256):
        dec2dac(i)
        time.sleep(0.001)
        comp_out = GPIO.input(comp)
        if not comp_out:
            return i

    


import RPi.GPIO as GPIO
import time

dac = [26,19,13,6,5,11,9,10]
bits = len(dac)
levels = 2**bits
max_volt = 3.3
comp = 4
troy = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(troy, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)


try:
    while True:
        x = adc()
        v = x*3.3/256
        print('Digital value: {} , Analog value: {:.2f}'.format(x, v))


        
        

except ValueError:
    print('Error')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
    print('GPIO cleanup completed')