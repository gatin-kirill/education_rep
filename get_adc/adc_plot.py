import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title('График зависимости напряжения на входе АЦП от времени')
    plt.xlabel('Времяб с')
    plt.ylabel('Напряжение, В')
    plt.xlim(max(time))
    plt.ylim(max_voltage)
    plt.grid(True)
    plt.show()