import math

def norm(vector):
    return math.sqrt(sum(x ** 2 for x in vector))


def check1(A):
    n = len(A)

    def check_rows():
        for i in range(n):
            if abs(A[i][i]) <= sum(abs(A[i][j]) for j in range(n) if i != j):
                return False
        return True

    def check_columns():
        for j in range(n):
            if abs(A[j][j]) <= sum(abs(A[i][j]) for i in range(n) if i != j):
                return False
        return True

    return check_rows() or check_columns()


def method_of_simple_iterations(A, b, epsilon=1e-6, max_iter=2000):
    assert check1(A)
    n = len(A)
    x = b[:]
    prev = x[:]

    na = max(sum(abs(A[i][j] / A[i][i]) for j in range(n) if i != j) for i in range(n))

    for k in range(1, max_iter + 1):
        for i in range(n):
            x[i] = b[i] / A[i][i] - sum((A[i][j] / A[i][i]) * prev[j] for j in range(n) if j != i)

        if na / (1 - na) * norm([x[i] - prev[i] for i in range(n)]) < epsilon:
            return x, k

        prev = x[:]

    return x, max_iter


def method_of_zeidel(A, b, epsilon=1e-6, max_iter=2000):
    assert check1(A)
    n = len(A)
    x = b[:]
    prev = x[:]

    na = max(sum(abs(A[i][j] / A[i][i]) for j in range(n) if i != j) for i in range(n))
    nc = max(sum(abs(A[i][j]) for j in range(n) if i != j) / abs(A[i][i]) for i in range(n))

    for k in range(1, max_iter + 1):
        for i in range(n):
            sum1 = sum((A[i][j] / A[i][i]) * x[j] for j in range(i))
            sum2 = sum((A[i][j] / A[i][i]) * prev[j] for j in range(i + 1, n))
            x[i] = b[i] / A[i][i] - sum1 - sum2

        diff = norm([x[i] - prev[i] for i in range(n)])

        if (na < 1 and nc / (1 - na) * diff < epsilon) or (na >= 1 and diff < epsilon):
            return x, k

        prev = x[:]

    return x, max_iter


A = [
    [12, -3, -1, 3],
    [5, 20, 9, 1],
    [6, -3, -21, -7],
    [8, -7, 3, -27]
]
b = [-31, 90, 119, 71]

epsilon = 1e-6

x_simple, iter_simple = method_of_simple_iterations(A, b, epsilon)
print("Метод простых итераций:")
print("Решение:")
for x in x_simple:
    print(round(x, 4))
print("Количество итераций:", iter_simple)

print()

x_zeidel, iter_zeidel = method_of_zeidel(A, b, epsilon)
print("Метод Зейделя:")
print("Решение:")
for x in x_zeidel:
    print(round(x, 4))
print("Количество итераций:", iter_zeidel)

