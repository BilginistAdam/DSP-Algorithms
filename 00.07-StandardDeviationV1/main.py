import mysignals as sigs
import numpy as np

standard_deviation = np.std(sigs.InputSignal_1kHz_15kHz)

if __name__ == '__main__':
    print('Standard Deviation is :', standard_deviation)
    print('complete!')