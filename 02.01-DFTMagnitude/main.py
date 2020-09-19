import mysignals as sigs
from matplotlib import pyplot as plt
from matplotlib import style
import math

def DFT(inputSignal):
    lenInput = int(len(inputSignal))
    halfLenInput = int(lenInput / 2)
    imgOutput = [0] * halfLenInput
    reOutput = [0] * halfLenInput
    magOutput = [0] * halfLenInput

    for k in range(halfLenInput):
        for i in range(lenInput):
            reOutput[k] = reOutput[k] + inputSignal[i] * math.cos(2 * math.pi * k * i / lenInput)
            imgOutput[k] = imgOutput[k] - inputSignal[i] * math.sin(2 * math.pi * k * i / lenInput)
    
    for x in range(halfLenInput):
        magOutput[x] = math.sqrt(math.pow(reOutput[x],2) + math.pow(imgOutput[x], 2))

    output = [imgOutput, reOutput, magOutput]
    return output


if __name__ == '__main__':
    outputSignal = DFT(sigs.InputSignal_1kHz_15kHz)

    #General Configuration for plots    
    style.use('ggplot')
    style.use('dark_background')
    
    f,plt_arr = plt.subplots(4, sharex= True)
    f.canvas.set_window_title('DFT - DSP')
    f.suptitle('DFT', color = 'red')

    #input plot
    plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz, color = 'yellow')
    plt_arr[0].set_title('Input Signal', color = 'yellow')

    #im output plot
    plt_arr[1].plot(outputSignal[0], color = 'blue')
    plt_arr[1].set_title('Frequency Domain (Imaginary Part)', color = 'blue')

    #re output plot
    plt_arr[2].plot(outputSignal[1], color = 'green')
    plt_arr[2].set_title('Frequency Domain (Real Part)', color = 'green')

    #magnotude plot
    plt_arr[3].plot(outputSignal[2], color = 'cyan')
    plt_arr[3].set_title('Frequency Domain (Magnitude)', color = 'cyan')

    plt.show()
    

    print('Done!')
