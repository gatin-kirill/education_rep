import numpy as np
import time

def get_sin_wave_amplitude(freq, tm):
    return 0.5*(1+float(np.sin(2*np.pi*freq*tm)))

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)
    return None