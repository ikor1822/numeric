
import matplotlib.pyplot as plt

# Метод прогонки
def tridiagonal_solve(a, b, c, d):
    n = len(b)

    # Проверка диагонального преобладания
    for i in range(n):
        if i == 0:
            if abs(b[i]) <= abs(c[i]):
                return

        elif i == n - 1:
            if abs(b[i]) <= abs(a[i - 1]):
                return

        else:
            if abs(b[i]) <= abs(a[i - 1]) + abs(c[i]):
                return

    # Прямой ход
    alpha = [0.0] * n
    beta = [0.0] * n

    alpha[0] = c[0] / b[0]
    beta[0] = d[0] / b[0]

    for i in range(1, n - 1):
        denom = b[i] - a[i - 1] * alpha[i - 1]
        alpha[i] = c[i] / denom
        beta[i] = (d[i] - a[i - 1] * beta[i - 1]) / denom

    beta[n - 1] = (d[n - 1] - a[n - 2] * beta[n - 2]) / (
        b[n - 1] - a[n - 2] * alpha[n - 2]
    )

    # Обратный ход
    x = [0.0] * n
    x[n - 1] = beta[n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = beta[i] - alpha[i] * x[i + 1]

    return x


# Исходные данные
X_star = 0.1

xi = [-0.4, -0.1, 0.2, 0.5, 0.8]
fi = [1.9823, 1.6710, 1.3694, 1.0472, 0.64350]

n = len(xi) - 1

# Вычисление шагов
h = [xi[i + 1] - xi[i] for i in range(n)]

# Составление системы
A = [0.0] * (n - 1)
B = [0.0] * (n - 1)
C = [0.0] * (n - 1)
D = [0.0] * (n - 1)

for i in range(1, n):
    A[i - 1] = h[i - 1]
    B[i - 1] = 2 * (h[i - 1] + h[i])
    C[i - 1] = h[i]

    D[i - 1] = 3 * (
        (fi[i + 1] - fi[i]) / h[i]
        - (fi[i] - fi[i - 1]) / h[i - 1]
    )

# Решение системы
c_internal = tridiagonal_solve(A[1:], B, C[:-1], D)

c = [0.0] + c_internal + [0.0]

# Вычисление коэффициентов сплайна
a = [0.0] * n
b = [0.0] * n
d = [0.0] * n

for i in range(n):
    a[i] = fi[i]

    b[i] = ((fi[i + 1] - fi[i]) / h[i]
            - h[i] * (2 * c[i] + c[i + 1]) / 3)

    d[i] = (c[i + 1] - c[i]) / (3 * h[i])


# Вычисление значения сплайна
def evaluate_spline(x):
    for i in range(n):
        if xi[i] <= x <= xi[i + 1]:
            dx = x - xi[i]

            return (a[i] + b[i] * dx
                    + c[i] * dx ** 2 + d[i] * dx ** 3)

    raise ValueError("Точка вне диапазона интерполяции")


# Вывод коэффициентов
print("Коэффициенты сплайна:")

for i in range(n):
    print(f"\nОтрезок [{xi[i]}, {xi[i + 1]}]")
    print(f"a = {a[i]:.6f}")
    print(f"b = {b[i]:.6f}")
    print(f"c = {c[i]:.6f}")
    print(f"d = {d[i]:.6f}")

# Вычисление в заданной точке
y_star = evaluate_spline(X_star)

print(f"\nS({X_star}) = {y_star:.6f}")


# Построение графика
x_dense = []
x_val = xi[0]

while x_val <= xi[-1]:
    x_dense.append(round(x_val, 5))
    x_val += 0.005

y_dense = [evaluate_spline(x) for x in x_dense]

plt.plot(xi, fi, 'ro', label='Узлы интерполяции')
plt.plot(x_dense, y_dense, 'b-', label='Кубический сплайн')

plt.title("Интерполяция кубическим сплайном")
plt.xlabel("x")
plt.ylabel("S(x)")
plt.legend()
plt.grid(True)
plt.show()
