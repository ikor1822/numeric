
import math

X_star = 0.1
true_value = math.acos(X_star)
x_a = [-0.4, -0.1, 0.2, 0.5]
x_b = [-0.4, 0.0, 0.2, 0.5]
y_a = [math.acos(x) for x in x_a]
y_b = [math.acos(x) for x in x_b]


def lagrange(x, y, X_star):
    n = len(x)
    result = 0
    for i in range(n):
        p = y[i]
        for j in range(n):
            if i != j:
                p *= (X_star - x[j]) / (x[i] - x[j])
        result += p
    return result


def newton(x, y, X_star):
    n = len(x)
    d = [[0.0] * n for _ in range(n)]
    for i in range(n):
        d[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            d[i][j] = (d[i + 1][j - 1] - d[i][j - 1]) / (x[i + j] - x[i])
    result = d[0][0]
    p = 1
    for i in range(1, n):
        p *= X_star - x[i - 1]
        result += d[0][i] * p
    return result


L_a = lagrange(x_a, y_a, X_star)
N_a = newton(x_a, y_a, X_star)
L_b = lagrange(x_b, y_b, X_star)
N_b = newton(x_b, y_b, X_star)

print(f"Точное значение: {true_value:.6f}\n")
print("Набор (а):")
print(f"Лагранж: {L_a:.6f}")
print(f"Погрешность: {abs(true_value - L_a):.8f}")
print(f"Ньютон: {N_a:.6f}")
print(f"Погрешность: {abs(true_value - N_a):.8f}")
print("\nНабор (б):")
print(f"Лагранж: {L_b:.6f}")
print(f"Погрешность: {abs(true_value - L_b):.8f}")
print(f"Ньютон: {N_b:.6f}")
print(f"Погрешность: {abs(true_value - N_b):.8f}")
