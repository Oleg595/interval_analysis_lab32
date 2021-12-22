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

inf_b = np.array([[2], [0], [2.4]], dtype=float)

sup_b = np.array([[4], [0], [4]], dtype=float)

[tolmax, argmax, envs, ccode] = tolsolvty(inf_A, sup_A, inf_b, sup_b)

print(tolmax)

def new_A(inf_A, sup_A, tolmax):
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
    positions = [argmax]
    while tolmax < -10 ** (-13):
        inf_A, sup_A = new_A(inf_A, sup_A, tolmax)
        if len(inf_A) == 0:
            return [], [], []
        [tolmax, argmax, envs, ccode] = tolsolvty(inf_A, sup_A, inf_b, sup_b)
        iterations.append(tolmax)
        positions.append(argmax)
    print(tolmax)
    print(argmax)
    pd.plot_tolmax_iterations(iterations, "Коррекция матрицы в целом")
    pd.error_position_argmax(positions, "Коррекция матрицы в целом")
    return inf_A, sup_A, argmax

def equal(line1, line2):
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            return False
    return True

def matrixLineCorrection(inf_A1, sup_A1, inf_b1, sup_b1):
    inf_A = deepcopy(inf_A1)
    sup_A = deepcopy(sup_A1)
    inf_b = deepcopy(inf_b1)
    sup_b = deepcopy(sup_b1)
    [tolmax, argmax, envs, ccode] = tolsolvty(inf_A, sup_A, inf_b, sup_b)
    iterations = [tolmax]
    positions = [argmax]
    while tolmax < -10 ** (-13):
        i = 0
        while equal(inf_A[int(envs[i][0]) - 1], sup_A[int(envs[i][0]) - 1]):
            i += 1
            if i == 3:
                return "Not answer"
        for j in range(len(inf_A[int(envs[i][0]) - 1])):
            new_rad = (sup_A[int(envs[i][0]) - 1][j] - inf_A[int(envs[i][0]) - 1][j]) / 4
            mid = (sup_A[int(envs[i][0]) - 1][j] + inf_A[int(envs[i][0]) - 1][j]) / 2
            inf_A[int(envs[i][0]) - 1][j] = mid - new_rad
            sup_A[int(envs[i][0]) - 1][j] = mid + new_rad
        [tolmax, argmax, envs, ccode] = tolsolvty(inf_A, sup_A, inf_b, sup_b)
        iterations.append(tolmax)
        positions.append(argmax)
    pd.plot_tolmax_iterations(iterations, "Построчная коррекция матрицы")
    pd.error_position_argmax(positions, "Построчная коррекция матрицы")
    return inf_A, sup_A, argmax

print(matrixCorrection(inf_A, sup_A, inf_b, sup_b))
print(matrixLineCorrection(inf_A, sup_A, inf_b, sup_b))
