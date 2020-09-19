from matplotlib import pyplot as plt
from matplotlib import style

import mysignals as sigs

style.use('ggplot')
style.use('dark_background')

f, plt_arr = plt.subplots(2, sharex=True)
f.suptitle('Input Sıgnal and Impulse Response', fontsize=12, color = 'red')

plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz, color = 'blue')
plt_arr[1].plot(sigs.Impulse_response, color = 'red')


if __name__ == '__main__':
    plt.show()
    print('Complete!')