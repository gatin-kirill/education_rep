import RPi.GPIO as GPIO
import time
import adc_plot
import r2r_adc

dynamic_range = 3.2
compare_time = 0.0001

r2r = r2r_adc.R2R_ADC(dynamic_range, compare_time)

voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.time()

    while time.time()-duration<start_time:
        voltage = r2r.get_sar_voltage()
        if voltage > 0:
            voltage_values.append(voltage)
            time_values.append(time.time()-start_time)
    
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
    adc_plot.plot_sampling_period(time_values)

finally:
    r2r.deinit()