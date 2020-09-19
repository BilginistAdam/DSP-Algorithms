from matplotlib import pyplot as plt
from matplotlib import style

x = [1,2,3,4,5,6]
y = [7,5,6,7,8,9]

x2 = [1,2,3,4,5,6]
y2 = [3,6,5,7,8,6]

style.use('dark_background')

plt.plot(x,y, label = 'Line One')
plt.plot(x2,y2, label = 'Line Two')

plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.title('Simple Chart')

if __name__ == '__main__':

    plt.legend()
    plt.show()

    print("This Worked...")