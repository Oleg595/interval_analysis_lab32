import math

import matplotlib.pyplot as plt

def plot_tolmax_iterations(iterations, text):
    num_iter = [i for i in range(len(iterations))]
    iterations = [math.fabs(elem) for elem in iterations]
    plt.title(text)
    plt.semilogy(num_iter, iterations)
    plt.xlabel("Номер итерации")
    plt.ylabel("Значение tolmax")
    plt.show()

def error_position_argmax(positions, text):
    correct_answer = [0.8, 0.4]
    rad = [math.sqrt((elem[0] - correct_answer[0]) ** 2 + (elem[1] - correct_answer[1]) ** 2) for elem in positions]
    num_iter = [i for i in range(len(positions))]
    plt.title(text)
    plt.plot(num_iter, rad)
    plt.xlabel("Номер итерации")
    plt.ylabel("Расстояние до верного ответа")
    plt.show()
