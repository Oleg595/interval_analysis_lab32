from copy import deepcopy

from tolsolvty import tolsolvty
import numpy as np
import plot_data as pd

inf_A = np.array([[0.5, 2],
         [1, -3],
         [2, 0]], dtype=float)

sup_A = np.array([[3.5, 5],
         [1, -1],
         [6, 0]], dtype=float)

inf_b = np.array([[2], [0], [1.2]], dtype=float)

sup_b = np.array([[4], [0], [2]], dtype=float)

[tolmax, argmax, envs, ccode] = tolsolvty(inf_A, sup_A, inf_b, sup_b)

print(tolmax)

def new_A(inf_A, sup_A):
    for index in range(len(inf_A)):
        rad1 = (sup_A[index][0] - inf_A[index][0]) / 4
        rad2 = (sup_A[index][1] - inf_A[index][1]) / 4
        mid1 = (sup_A[index][0] + inf_A[index][0]) / 2
        mid2 = (sup_A[index][1] + inf_A[index][1]) / 2
        inf_A[index][0] = mid1 - rad1
        sup_A[index][0] = mid1 + rad1
        inf_A[index][1] = mid2 - rad2
        sup_A[index][1] = mid2 + rad2
    return inf_A, sup_A

def matrixCorrection(inf_A1, sup_A1, inf_b1, sup_b1):
    inf_A = deepcopy(inf_A1)
    sup_A = deepcopy(sup_A1)
    inf_b = deepcopy(inf_b1)
    sup_b = deepcopy(sup_b1)
    [tolmax, argmax, envs, ccode] = tolsolvty(inf_A, sup_A, inf_b, sup_b)
    iterations = [tolmax]
    positions = [[argmax[0][0], argmax[1][0]]]
    for i in range(10):
        inf_A, sup_A = new_A(inf_A, sup_A)
        if len(inf_A) == 0:
            return [], [], []
        [tolmax, argmax, envs, ccode] = tolsolvty(inf_A, sup_A, inf_b, sup_b)
        iterations.append(tolmax)
        positions.append([argmax[0][0], argmax[1][0]])
    print(positions)
    pd.plot_argmax(positions, "Коррекция матрицы в целом")
    return inf_A, sup_A, argmax

def equal(line1, line2):
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            return False
    return True

def matrixLineCorrection(inf_A1, sup_A1, inf_b1, sup_b1, index):
    inf_A = deepcopy(inf_A1)
    sup_A = deepcopy(sup_A1)
    inf_b = deepcopy(inf_b1)
    sup_b = deepcopy(sup_b1)
    [tolmax, argmax, envs, ccode] = tolsolvty(inf_A, sup_A, inf_b, sup_b)
    positions = [[argmax[0][0], argmax[1][0]]]
    for i in range(10):
        for j in range(len(inf_A[index])):
            new_rad = (sup_A[index][j] - inf_A[index][j]) / 4
            mid = (sup_A[index][j] + inf_A[index][j]) / 2
            inf_A[index][j] = mid - new_rad
            sup_A[index][j] = mid + new_rad
        [tolmax, argmax, envs, ccode] = tolsolvty(inf_A, sup_A, inf_b, sup_b)
        positions.append([argmax[0][0], argmax[1][0]])
    print(positions)
    pd.plot_argmax(positions, "Построчная коррекция матрицы")

matrixCorrection(inf_A, sup_A, inf_b, sup_b)
matrixLineCorrection(inf_A, sup_A, inf_b, sup_b, 0)
matrixLineCorrection(inf_A, sup_A, inf_b, sup_b, 2)
