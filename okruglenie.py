import time
import numpy as np
import math
import solve
import matplotlib.pyplot as plt

size = range(50, 100)

V = []
V2 = []
V3 = []
V4 = []

def M_Gauss(n):
    A = np.random.uniform(0, 10, (n, n))
    b = np.random.uniform(0, 10, (n, 1))
    M = np.hstack((A, b))
    # вычисление значения матрицы методом гаусса БЕЗ округления
    t = time.time()
    for i in range(0, n):
        m = i
        for k in range(i + 1, n):
            if (math.fabs(M[k, i]) > math.fabs(M[m, i])):
                m = k
        for j in range(i, n + 1):
            z = M[i, j]
            M[i, j] = M[m, j]
            M[m, j] = z
        c = M[i, i]
        for j in range(i, n + 1):
            M[i, j] = (M[i, j]) / c
        for k in range(i + 1, n):
            b = M[k, i]
            for l in range(i, n + 1):
                M[k, l] = M[k, l] - b * M[i, l]
    c = M[n - 1, n - 1]
    for j in range(n - 1, n):
        M[n - 1, j] = M[n - 1, j] / c
    x = []
    for i in range(0, n):
        x.append(0)
    x[n - 1] = M[n - 1, n] / M[n - 1, n - 1]
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = s + M[k, j] * x[j]
        x[k] = M[k, n] - s
        k = k - 1
    T = time.time() - t
    V2.append(T)
    # вычисляется значение матрицы методом гаусса С ОКРУГЛЕНИЕМ до 3 (e) цифр после запятой
    e = 3
    p = time.time()
    for i in range(0, n):
        m = i
        for k in range(i + 1, n):
            if (math.fabs(M[k, i]) > math.fabs(M[m, i])):
                m = k
        for j in range(i, n + 1):
            z = M[i, j]
            M[i, j] = M[m, j]
            M[m, j] = z
        c = M[i, i]
        for j in range(i, n + 1):
            M[i, j] = round(((M[i, j]) / c), e)
        for k in range(i + 1, n):
            b = M[k, i]
            for l in range(i, n + 1):
                M[k, l] = round((M[k, l] - b * M[i, l]), e)
    c = M[n - 1, n - 1]
    for j in range(n - 1, n):
        M[n - 1, j] = round((M[n - 1, j] / c), e)
    x = []
    for i in range(0, n):
        x.append(0)
    x[n - 1] = round((M[n - 1, n] / M[n - 1, n - 1]), e)
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = (s + M[k, j] * x[j])
        x[k] = round((M[k, n] - s), e)
        k = k - 1
    P = time.time() - p
    V3.append(P)
    # вычисляется значение матрицы методом гаусса С ОКРУГЛЕНИЕМ до 6 (e) цифр после запятой
    e = 3
    p = time.time()
    for i in range(0, n):
        m = i
        for k in range(i + 1, n):
            if (math.fabs(M[k, i]) > math.fabs(M[m, i])):
                m = k
        for j in range(i, n + 1):
            z = M[i, j]
            M[i, j] = M[m, j]
            M[m, j] = z
        c = M[i, i]
        for j in range(i, n + 1):
            M[i, j] = round(((M[i, j]) / c), e)
        for k in range(i + 1, n):
            b = M[k, i]
            for l in range(i, n + 1):
                M[k, l] = round((M[k, l] - b * M[i, l]), e)
    c = M[n - 1, n - 1]
    for j in range(n - 1, n):
        M[n - 1, j] = round((M[n - 1, j] / c), e)
    x = []
    for i in range(0, n):
        x.append(0)
    x[n - 1] = round((M[n - 1, n] / M[n - 1, n - 1]), e)
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = (s + M[k, j] * x[j])
        x[k] = round((M[k, n] - s), e)
        k = k - 1
    P = time.time() - p
    V4.append(P)

for n in size:
    t = time.time()
    d = time.time()
    p = time.time()
    g = time.time()
    M_Gauss(n)

# отображение результатов
fig, ax = plt.subplots()
ax.set_xlabel('размерность')
ax.set_ylabel('времязатраты')
plt.plot(size, V2, 'r-', label='Без округления')
plt.plot(size, V3, 'b--', label='Округление дл 3')
plt.plot(size, V4, 'g-', label ='Округление до 6')
ax.legend()
plt.grid()
plt.show()