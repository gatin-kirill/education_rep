import matplotlib.pyplot as plt
import numpy as np
import math

data = np.loadtxt('data.csv', delimiter=',', skiprows=1, encoding='utf-8')
time = data[:, 0].astype(float)
voltage = data[:, 1].astype(float)
v0 = 2.955

plt.figure(figsize=(10,6))
plt.plot(time, voltage)
plt.title('График зависимости напряжения на конденсаторе от времени')
plt.xlabel('Время, с')
plt.ylabel('Напряжение, В')
plt.grid(True)
plt.savefig('rc-plot.png', dpi=300)

plt.close()

plt.figure(figsize=(10,6))
plt.plot([math.log(v0/(v0-v)) for v in voltage], time)
plt.title('Линеаризованный рафик зависимости напряжения на конденсаторе от времени')
plt.ylabel('Время, с')
plt.xlabel('ln(U0/U)')
plt.grid(True)
plt.savefig('rc-plot-lin.png', dpi=300)