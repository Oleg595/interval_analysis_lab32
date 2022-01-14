import math

import matplotlib.pyplot as plt

def plot_argmax(positions, text):
    x1 = [elem[0] for elem in positions]
    x2 = [elem[1] for elem in positions]
    col = ['blue', 'yellow', 'green', 'white', 'red', 'purple', 'black', 'orange', 'pink', 'magenta', 'brown']

    for i in range(len(x1)):
        # plotting the corresponding x with y
        # and respective color
        plt.scatter(x1[i], x2[i], c=col[i], s=10,
                    linewidth=0)

    plt.title(text)
    plt.show()
