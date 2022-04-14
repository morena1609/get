import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt


def dec2bin(num): # перевод десятичного числа в двоичное
    return [int(e) for e in bin(num)[2:].zfill(8)]


def dec2dac(num): # вывод десятичного числа на ЦАП
    GPIO.output(dac, dec2bin(num))
    return (dec2bin(num))


def bin2dec(y): # перевод двоечного числа в десятичное
    x = list(map(str, y))
    return int(''.join(x), base=2)

def dec2leds(num): # вывод десятичного числа на компоненту платы leds 
    GPIO.output(leds, dec2bin(num))
    return (dec2bin(num))


def adc():  # измеряет напряжение на АЦП
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


dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
bits = len(dac)
levels = 2**bits
max_volt = 3.3
comp = 4
troy = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troy, GPIO.OUT)

GPIO.output(troy, GPIO.HIGH)

try:
    start = time.time()
    data = []
    value = 0
    GPIO.output(troy, GPIO.HIGH)

    while value <= 0.97 * 255: # измерение напряжения на кондесаторе по мере его зарядки 
        value = adc()
        print(value)
        dec2leds(value)
        data.append(value)
    
    GPIO.output(troy, GPIO.LOW)

    while value > 0.02 * 255: # измерение напряжения на кондесаторе по мере его разрядки
        value = adc()
        dec2leds(value)
        print(value)
        data.append(value)

    end = time.time()
    dur_time = end - start # время выполнения эксперимента
    frequency = dur_time / (len(data) - 1)

    data_str = list(map(str, data)) 

    with open('/home/b01-106/get/data.txt', 'w') as f_data: # запись в файл полученных результатов измерения
        f_data.write('\n'.join(data_str))

    with open('/home/b01-106/get/settings.txt', 'w') as set: # запись в файл основных параметров измерения
        set.write(f"Average frequency: {frequency} s \nDiscretization: {max_volt/levels} V\n")     
        

    print(f"Experiment lasted: {dur_time} s ")
    print(f"Quantization step: {frequency} s ") 
    print(f"Discretization is {max_volt/levels} V ")

    plt.plot(data)
    plt.show()



finally:

    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup(leds)
    print('GPIO cleanup completed')