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


def IDFT(reInput, imgInput):
    lenInputs = int(len(reInput))
    output = [0] * (lenInputs * 2)

    for x in range(lenInputs):
        reInput[x] = reInput[x] / lenInputs
        imgInput[x] = imgInput[x] / lenInputs
    
    for k in range(lenInputs):
        for i in range(lenInputs * 2):
            output[i] = output[i] + reInput[k] * math.cos(2 * math.pi * k * i / (lenInputs * 2))
            output[i] = output[i] - imgInput[k] * math.sin(2 * math.pi * k * i / (lenInputs * 2))

    return output


if __name__ == '__main__':
    outputDFTSignal = DFT(sigs.InputSignal_1kHz_15kHz)
    outputIDFTSignal = IDFT(outputDFTSignal[1], outputDFTSignal[0])
    
    #General Configuration for plots    
    style.use('ggplot')
    style.use('dark_background')
    
    f,plt_arr = plt.subplots(4, 2,  sharex= True)
    f.canvas.set_window_title('IDFT - DSP')
    f.suptitle('DFT - IDFT', color = 'red')

    #DFT
    #input plot
    plt_arr[0,0].plot(sigs.InputSignal_1kHz_15kHz, color = 'yellow')
    plt_arr[0,0].set_title('DFT Time Domain Input Signal', color = 'yellow')

    #im output plot
    plt_arr[1,0].plot(outputDFTSignal[0], color = 'blue')
    plt_arr[1,0].set_title('Frequency Domain Output(Imaginary Part)', color = 'blue')

    #re output plot
    plt_arr[2,0].plot(outputDFTSignal[1], color = 'green')
    plt_arr[2,0].set_title('Frequency Domain Output(Real Part)', color = 'green')

    #magnotude plot
    plt_arr[3,0].plot(outputDFTSignal[2], color = 'cyan')
    plt_arr[3,0].set_title('Frequency Domain Output(Magnitude)', color = 'cyan')

    #IDFT
    #Original Signal plot
    plt_arr[0,1].plot(sigs.InputSignal_1kHz_15kHz, color = 'yellow')
    plt_arr[0,1].set_title('Original Signal', color = 'yellow')

    #IDFT Algorithm Result plot
    plt_arr[1,1].plot(outputIDFTSignal, color = 'red')
    plt_arr[1,1].set_title('IDFT Algorithm Result', color = 'red')

    #img part input plot
    plt_arr[2,1].plot(outputDFTSignal[0], color = 'blue')
    plt_arr[2,1].set_title('IDFT Input Signal Imaginary Part', color = 'blue')

    #real part input plot
    plt_arr[3,1].plot(outputDFTSignal[1], color = 'green')
    plt_arr[3,1].set_title('IDFT Input Signal Real Part', color = 'green')   

    plt.show()
    
    print('Done!')
