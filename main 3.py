import numpy as np
import time
import matplotlib.pyplot as plt

A1 = np.array([[3.78, 3.44, 3.02], [4.33, 3.88, 3.39], [4.76, 4.24, 3.72]])
B1 = np.array([46.81, 53.43, 58.73])

A2 = np.random.rand(4, 4)
B2 = np.random.rand(4)

A3 = np.random.rand(5, 5)
B3 = np.random.rand(5)

matrices = [(A1, B1), (A2, B2), (A3, B3)]

for idx, (A, B) in enumerate(matrices):
    n = len(B)

    for i in range(n):
        pivot_idx = np.argmax(np.abs(A[i:, i])) + i
        A[[i, pivot_idx]] = A[[pivot_idx, i]]
        B[[i, pivot_idx]] = B[[pivot_idx, i]]
        for k in range(i + 1, n):
            factor = A[k, i] / A[i, i]
            A[k, i:] -= factor * A[i, i:]
            B[k] -= factor * B[i]


    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (B[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    print(f"Решение для матрицы {idx + 1}:")
    print("Мой метод:")
    print(x)
    print("Встроенный метод:")
    print(np.linalg.solve(A, B))
    print("------------------------")

system_sizes = range(50, 200)
execution_times_float32 = []
execution_times_float64 = []
execution_times_longdouble = []

data_types = [np.float32, np.float64, np.longdouble]

for n in system_sizes:
    for dtype in data_types:

        A = np.random.rand(n, n).astype(dtype)
        B = np.random.rand(n).astype(dtype)

        start_time = time.time()
        for i in range(n):
            maxEl = abs(A[i][i])
            maxRow = i
            for k in range(i + 1, n):
                if abs(A[k][i]) > maxEl:
                    maxEl = abs(A[k][i])
                    maxRow = k

            A[[i, maxRow]] = A[[maxRow, i]]
            B[i], B[maxRow] = B[maxRow], B[i]

            for k in range(i + 1, n):
                c = -A[k][i] / A[i][i]
                A[k, i:] += c * A[i, i:]
                B[k] += c * B[i]
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = B[i]
            for j in range(i + 1, n):
                x[i] -= A[i][j] * x[j]
            x[i] /= A[i][i]
        end_time = time.time()
        execution_time = end_time - start_time
        if dtype == np.float32:
            execution_times_float32.append(execution_time)
        elif dtype == np.float64:
            execution_times_float64.append(execution_time)
        elif dtype == np.longdouble:
            execution_times_longdouble.append(execution_time)

plt.plot(system_sizes, execution_times_float32, marker='o', label='np.float32')

plt.plot(system_sizes, execution_times_float64, marker='o', label='np.float64')

plt.plot(system_sizes, execution_times_longdouble, marker='o', label='np.longdouble')

plt.xlabel('Размер матрицы')
plt.ylabel('Время выполнения (секунды)')
plt.title('Отношение временных затрат к размеру матрицы для разных типов данных')
plt.legend()
plt.show()
