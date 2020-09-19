from matplotlib import pyplot as plt
from matplotlib import style
import mysignals as sigs

def runningSum(inputSignal):
    lenInput = len(inputSignal)
    outputSignal = [0] * lenInput

    for num in range(lenInput):
        outputSignal[num] =  outputSignal[num-1] + inputSignal[num]

    return outputSignal

output = runningSum(sigs.InputSignal_1kHz_15kHz)

style.use('ggplot')
style.use('dark_background')

f, pltArr = plt.subplots(2, sharex=True)
f.suptitle('Running Sum Algorithm', color = 'red')

pltArr[0].plot(sigs.InputSignal_1kHz_15kHz, color = 'blue')
pltArr[0].set_title('Input Signal', color = 'blue')

pltArr[1].plot(output, color = 'green')
pltArr[1].set_title('Output Signal', color = 'green')

if __name__ == '__main__':
    plt.show()

    print('done!')