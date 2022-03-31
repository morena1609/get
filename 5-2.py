def dec2bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

def bin2dec(y):
    x = list(map(str, y))
    return int(''.join(x), base = 2 )

def adc():
    out = [0]*8
    for i in range(8):
        out[i] = 1
        GPIO.output(dac, out)
        time.sleep(0.002)
        com_out = GPIO.input(comp)
        if not com_out:
            out[i] = 0
    dv = bin2dec(out)
    return dv


import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
max_volt = 3.3
comp = 4
troy = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troy, GPIO.OUT)

GPIO.output(troy, GPIO.HIGH)
#
try:
    while True:
        
        x = adc()
        volt = x * max_volt/levels
        print('Digital value: {} , Analog value: {:.2f}'.format(x, volt))
        
        
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print('GPIO cleanup completed') #