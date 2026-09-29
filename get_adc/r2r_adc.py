import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, num):

        if num>=2**len(self.bits_gpio):
            num = 2**len(self.bits_gpio)-1
        if num<0:
            num = 0
        
        num_bin = dec2bin(num)
        num_bin = [0]*(len(self.bits_gpio)-len(num_bin))+num_bin

        GPIO.output(self.bits_gpio, num_bin)

    def sequential_counting_adc(self):
        num = 0
        self.number_to_dac(num)
        while not(GPIO.input(self.comp_gpio)) and num<=2**len(self.bits_gpio):
            self.number_to_dac(num)
            time.sleep(self.compare_time)
            num+=1
        return num
    
    def get_sc_voltage(self):
        num = self.sequential_counting_adc()
        return self.dynamic_range*num/(2**len(self.bits_gpio))

if __name__ == '__main__':
    try:
        r2r = R2R_ADC(3.3)

        while True:
            voltage = r2r.get_sc_voltage()
            if voltage != 0:
                print(voltage)
            
    finally:
        r2r.deinit()