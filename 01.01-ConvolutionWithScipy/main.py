from matplotlib import pyplot as plt
from matplotlib import style
from scipy import signal

import mysignals as sigs

#Scipy Convolution
output_signal = signal.convolve(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response, mode = 'same')

#PLT Stype Configuration
style.use('ggplot')
style.use('dark_background')

#Sup plot config
f, plt_arr = plt.subplots(3, sharex=True)
f.suptitle('Convolution', fontsize=14, color = 'red')

#Input Signal Configuration
plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz, color = 'blue')
plt_arr[0].set_title('Input Signal')
plt_arr[0].set_ylabel('Value')

#Impulse Response Configuration
plt_arr[1].plot(sigs.Impulse_response, color = 'yellow')
plt_arr[1].set_title('Impulse Response')
plt_arr[1].set_ylabel('Value')

#Output Signal Configuration
plt_arr[2].plot(output_signal, color = 'cyan')
plt_arr[2].set_title('Output Signal')
plt_arr[2].set_ylabel('Value')

if __name__ == '__main__':
    plt.grid(True)
    plt.show()
    print('Complete!')