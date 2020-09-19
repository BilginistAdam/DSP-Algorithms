from matplotlib import pyplot as plt
from matplotlib import style
import csv

import mysignals as sigs

def convolution(inputSignal, impulseResponse):
    sizeValue = len(inputSignal) + len(impulseResponse)
    outputSignal = [None] *sizeValue

    for k in range(sizeValue):
        outputSignal[k] = 0

    for signalSampleNum in range(len(inputSignal)):
        for impulseSampleNum in range(len(impulseResponse)):
            outputSignal[signalSampleNum + impulseSampleNum] = outputSignal[signalSampleNum + impulseSampleNum] + (inputSignal[signalSampleNum] * impulseResponse[impulseSampleNum])
        
    return outputSignal

def writeCSCV(data, fileName = 'data'):
    with open(fileName + '.csv', 'w+') as dataFile:
        writer = csv.writer(dataFile, lineterminator = ',')
        for x in data:
            writer.writerow([x])



if __name__ == '__main__':
    outputSignal = convolution(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response)
    
    style.use('ggplot')
    style.use('dark_background')

    f, plt_arr =  plt.subplots(3, sharex=True)
    f.canvas.set_window_title('Convolution - DSP')
    f.suptitle('convolution', color = 'red')

    plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz, color = 'red')
    plt_arr[0].set_title('Input signal', color = 'red')

    plt_arr[1].plot(sigs.Impulse_response, color = 'blue')
    plt_arr[1].set_title('Impulse Response', color = 'blue')

    plt_arr[2].plot(outputSignal, color = 'cyan')
    plt_arr[2].set_title('Outpur Signal', color = 'cyan')

    plt.show()
    writeCSCV(outputSignal, 'outputSignalData')
    print('Complete!')