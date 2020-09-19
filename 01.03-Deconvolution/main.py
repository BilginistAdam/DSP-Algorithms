from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

sig = np.array([0,0,0,0,1,1,1,1])
filter = np.array([1,1,0])

conv_result = signal.convolve(sig, filter)
deconv_result = signal.deconvolve(conv_result, filter)

if __name__ == '__main__':
    print('-' * 50)
    print('Signal : ', sig)
    print('Filter : ', filter)
    print('-' * 50)
    print('Convolution Result : ', conv_result)
    print('-' * 50)
    print('Deconvolution Result : ',deconv_result)
    print('-' * 50)
    print('Completed!')