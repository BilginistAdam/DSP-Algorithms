from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import mysignals as sigs

style.use('ggplot')
style.use('dark_background')

corrOutput = signal.correlate(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response, mode = 'same')
convOutput = signal.convolve(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response, mode = 'same')

f, pltArr = plt.subplots(4, sharex=True)
f.suptitle('Convolution', color = 'purple')

pltArr[0].plot(sigs.InputSignal_1kHz_15kHz, color = 'red')
pltArr[0].set_title('Input', color = 'red')

pltArr[1].plot(sigs.Impulse_response, color = 'blue')
pltArr[1].set_title('Impulse Response', color = 'blue')

pltArr[2].plot(convOutput, color = 'cyan')
pltArr[2].set_title('Convolution')

pltArr[3].plot(corrOutput, color = 'green')
pltArr[3].set_title('Correlation')

if __name__ == '__main__':
    plt.show()
    print('Done!')

