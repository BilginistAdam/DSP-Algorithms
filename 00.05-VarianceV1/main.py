import numpy as np
import mysignals as sigs

variance = np.var(sigs.InputSignal_1kHz_15kHz)

if __name__ == '__main__':
    print('Variance is :', variance)
    print('Complete!!')