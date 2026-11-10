import RPi.GPIO as GPIO
import time
import mcp3021_driver
import numpy as np

dynamic_range = 3.2

mcp = mcp3021_driver.MCP3021(dynamic_range)

voltage_values = []
time_values = []
duration = 30.0

try:
    start_time = time.time()

    while time.time()-duration<start_time:
        voltage = mcp.get_voltage()
        if voltage > 0:
            voltage_values.append(voltage)
            time_values.append(time.time()-start_time)
    

finally:
    mcp.deinit()

data = np.column_stack((time_values, voltage_values))

np.savetxt('data.csv', data, delimiter=',', fmt='%.4f', header='Время[c],Напряжение[В]', comments='', encoding='utf-8')
