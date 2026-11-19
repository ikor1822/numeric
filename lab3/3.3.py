
import matplotlib.pyplot as plt

# Исходные данные
x = [-0.7, -0.4, -0.1, 0.2, 0.5, 0.8]
y = [2.3462, 1.9823, 1.671, 1.3694, 1.0472, 0.6435]

n = len(x)


# Решение системы методом LU-разложения
def solve_system(A, b):
    n = len(A)
    A = [row[:] for row in A]

    # LU-разложение
    for k in range(n):
        for i in range(k + 1, n):
            A[i][k] /= A[k][k]

            for j in range(k + 1, n):
                A[i][j] -= A[i][k] * A[k][j]

    # Прямая подстановка
    z = [0.0] * n

    for i in range(n):
        z[i] = b[i] - sum(A[i][j] * z[j] for j in range(i))

    # Обратная подстановка
    result = [0.0] * n

    for i in range(n - 1, -1, -1):
        result[i] = (z[i] - sum(A[i][j] * result[j]
                                for j in range(i + 1, n))) / A[i][i]

    return result


# Нормальная система для многочлена первой степени
def normal_system1(x, y):
    n = len(x)

    A = [
        [n, sum(x)],
        [sum(x), sum(xi ** 2 for xi in x)]
    ]

    b = [
        sum(y),
        sum(x[i] * y[i] for i in range(n))
    ]

    return A, b


# Нормальная система для многочлена второй степени
def normal_system2(x, y):
    n = len(x)

    A = [
        [n, sum(x), sum(xi ** 2 for xi in x)],
        [sum(x), sum(xi ** 2 for xi in x),
         sum(xi ** 3 for xi in x)],
        [sum(xi ** 2 for xi in x),
         sum(xi ** 3 for xi in x),
         sum(xi ** 4 for xi in x)]
    ]

    b = [
        sum(y),
        sum(x[i] * y[i] for i in range(n)),
        sum(x[i] ** 2 * y[i] for i in range(n))
    ]

    return A, b


# Вычисление суммы квадратов ошибок
def compute_error(x, y, coeffs):
    error = 0

    for i in range(len(x)):
        fx = sum(coeffs[j] * x[i] ** j for j in range(len(coeffs)))
        error += (fx - y[i]) ** 2

    return error


# Решение нормальных систем
A1, b1 = normal_system1(x, y)
A2, b2 = normal_system2(x, y)

coeffs1 = solve_system(A1, b1)
coeffs2 = solve_system(A2, b2)


# Вывод многочленов
print("Многочлен первой степени:")
print(f"F1(x) = {coeffs1[0]:.6f} + ({coeffs1[1]:.6f}) * x")

print("\nМногочлен второй степени:")
print(f"F2(x) = {coeffs2[0]:.6f} + ({coeffs2[1]:.6f}) * x "
      f"+ ({coeffs2[2]:.6f}) * x^2")


# Вычисление ошибок
error1 = compute_error(x, y, coeffs1)
error2 = compute_error(x, y, coeffs2)

print(f"\nСумма квадратов ошибок F1: {error1:.8f}")
print(f"Сумма квадратов ошибок F2: {error2:.8f}")


# Построение графиков
x_plot = [min(x) + i * 0.01
          for i in range(int((max(x) - min(x)) / 0.01) + 1)]

y1 = [sum(coeffs1[j] * xi ** j for j in range(len(coeffs1)))
      for xi in x_plot]

y2 = [sum(coeffs2[j] * xi ** j for j in range(len(coeffs2)))
      for xi in x_plot]

plt.scatter(x, y, label="Исходные точки")
plt.plot(x_plot, y1, label="Многочлен 1-й степени")
plt.plot(x_plot, y2, label="Многочлен 2-й степени")

plt.title("Аппроксимация методом МНК")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
