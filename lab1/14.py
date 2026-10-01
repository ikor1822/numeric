import math

def check_matrix(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] != A[j][i]:
                return False
    return True


def find_max(A):
    n = len(A)
    max_val = 0
    k, m = 0, 1

    for i in range(n):
        for j in range(i + 1, n):
            if abs(A[i][j]) > max_val:
                max_val = abs(A[i][j])
                k, m = i, j

    return k, m, max_val


def rotation(A, V, k, m):
    n = len(A)
    theta = (A[m][m] - A[k][k]) / (2 * A[k][m])
    t = (1 if theta >= 0 else -1) / (abs(theta) + math.sqrt(theta ** 2 + 1))
    c = 1 / math.sqrt(1 + t ** 2)
    s = t * c

    for i in range(n):
        if i != k and i != m:
            x = A[i][k]
            y = A[i][m]
            A[i][k] = x * c - y * s
            A[k][i] = A[i][k]
            A[i][m] = x * s + y * c
            A[m][i] = A[i][m]

    x = A[k][k]
    y = A[m][m]
    z = A[k][m]

    A[k][k] = x - t * z
    A[m][m] = y + t * z
    A[k][m] = 0
    A[m][k] = 0

    for i in range(n):
        x = V[i][k]
        y = V[i][m]
        V[i][k] = x * c - y * s
        V[i][m] = x * s + y * c


def restore_matrix(values, vectors):
    n = len(values)
    A = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                A[i][j] += vectors[i][k] * values[k] * vectors[j][k]

    return A


def show_matrix(A):
    for row in A:
        print("  ".join(f"{x:.3f}" for x in row))


A = [
    [4, 7, -1],
    [7, -9, -6],
    [-1, -6, -4]
]

epsilon = 1e-3
n = len(A)
V = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

if not check_matrix(A):
    print("матрица не симметрична!")
else:
    count = 0

    while True:
        k, m, max_val = find_max(A)
        if max_val < epsilon:
            break

        rotation(A, V, k, m)
        count += 1

    values = [A[i][i] for i in range(n)]

    print("Собственные значения:")
    for x in values:
        print(round(x, 4))

    print("Матрица собственных векторов:")
    for i in range(n):
        print("  ".join(f"{V[i][j]:.3f}" for j in range(n)))

    
    print("Количество затраченных итераций:")
    print(count)
