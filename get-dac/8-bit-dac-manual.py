import RPi.GPIO as GPIO

pins = [16, 20, 21, 25, 26, 17, 27, 22]

GPIO.setmode(GPIO.BCM)
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

dynamic_range = 3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапозон ЦАП (0.00 - {dynamic_range:.2f} В")
        print("Устанавливаем 0.0 В")
        return 0
    
    return int(voltage/dynamic_range * 255)

def number_to_dac(number):
    #print(number)
    if number>2**len(pins)-1:
        print("Число вышло за допустимый диапозон")
        return 0

    for pin in pins:
        GPIO.output(pin, 0)
    
    bin_num = ''
    while number != 0:
        bin_num=str(number%2)+bin_num
        number = number//2

    #print(bin_num)

    for i in range(len(bin_num)):
        GPIO.output(pins[8-len(bin_num)+i], int(bin_num[i]))
    
    return 0

try:
    while True:
        try:
            voltage = float(input("ВВедите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()