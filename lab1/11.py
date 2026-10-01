def lu(A):
    n = len(A)
    for k in range(n):
        for i in range(k + 1, n):
            A[i][k] /= A[k][k]
            for j in range(k + 1, n):
                A[i][j] -= A[i][k] * A[k][j]


def forward(A, b):
    n = len(A)
    y = [0] * n
    for i in range(n):
        y[i] = b[i] - sum(A[i][j] * y[j] for j in range(i))
    return y


def backward(A, y):
    n = len(A)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]
    return x


def solve(A, b):
    lu(A)
    y = forward(A, b)
    return backward(A, y)


def det(A):
    lu(A)
    res = 1
    for i in range(len(A)):
        res *= A[i][i]
    return res


def inverse(A):
    n = len(A)
    lu(A)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        b = [0] * n
        b[i] = 1
        y = forward(A, b)
        x = backward(A, y)
        for j in range(n):
            res[j][i] = x[j]
    return res


def check(A):
    n = len(A)
    B = [row[:] for row in A]
    lu(B)
    return [[sum((1 if i == k else B[i][k] if i > k else 0) *
                 (B[k][j] if k <= j else 0) for k in range(n))
             for j in range(n)] for i in range(n)]


A = [
    [-7, -9, 1, -9],
    [-6, -8, -5, 2],
    [-3, 6, 5, -9],
    [-2, 0, -5, -9]
]
b = [29, 42, 11, 75]

x = solve([row[:] for row in A], b)
print("Решение СЛАУ:")
print([round(v, 6) for v in x])

print("Определитель:", round(det([row[:] for row in A]), 6))

print("Обратная матрица:")
for row in inverse([row[:] for row in A]):
    print([round(v, 3) for v in row])

print("Проверка LU-разложения:")
for row in check(A):
    print([round(v, 6) for v in row])
