import RPi.GPIO as GPIO
import time
import adc_plot
import mcp3021_driver

dynamic_range = 3.2

mcp = mcp3021_driver.MCP3021(dynamic_range)

voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.time()

    while time.time()-duration<start_time:
        voltage = mcp.get_voltage()
        if voltage > 0:
            voltage_values.append(voltage)
            time_values.append(time.time()-start_time)
    
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
    adc_plot.plot_sampling_period(time_values)

finally:
    mcp.deinit()