
import math

# Функция
def f(x):
    return x / (x ** 2 + 9)


# Метод прямоугольников
def rectangle_method(a, b, h):
    n = int((b - a) / h)
    result = 0

    for i in range(n):
        x = a + (i + 0.5) * h
        result += f(x)

    return result * h


# Метод трапеций
def trapez_method(a, b, h):
    n = int((b - a) / h)
    result = (f(a) + f(b)) / 2

    for i in range(1, n):
        x = a + i * h
        result += f(x)

    return result * h


# Метод Симпсона
def simpson_method(a, b, h):
    n = int((b - a) / h)

    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h

        if i % 2 == 0:
            result += 2 * f(x)
        else:
            result += 4 * f(x)

    return result * h / 3


# Метод Рунге-Ромберга
def runge_romberg(Fh, Fkh, k, p):
    return Fh + (Fh - Fkh) / (k ** p - 1)


# Исходные данные
a = 0
b = 2
h1 = 0.5
h2 = 0.25

k = int(h1 / h2)

F_true = 0.5 * math.log(13 / 9)


# Метод прямоугольников
F_rect1 = rectangle_method(a, b, h1)
F_rect2 = rectangle_method(a, b, h2)

F_rect = runge_romberg(F_rect2, F_rect1, k, 2)


# Метод трапеций
F_trap1 = trapez_method(a, b, h1)
F_trap2 = trapez_method(a, b, h2)

F_trap = runge_romberg(F_trap2, F_trap1, k, 2)


# Метод Симпсона
F_simp1 = simpson_method(a, b, h1)
F_simp2 = simpson_method(a, b, h2)

F_simp = runge_romberg(F_simp2, F_simp1, k, 4)


# Вывод результатов
print(f"Точное значение: {F_true:.8f}\n")

print("Метод прямоугольников:")
print(f"h = {h1}: {F_rect1:.8f}")
print(f"h = {h2}: {F_rect2:.8f}")
print(f"Рунге-Ромберг: {F_rect:.8f}")
print(f"Погрешность: {abs(F_true - F_rect):.8f}\n")

print("Метод трапеций:")
print(f"h = {h1}: {F_trap1:.8f}")
print(f"h = {h2}: {F_trap2:.8f}")
print(f"Рунге-Ромберг: {F_trap:.8f}")
print(f"Погрешность: {abs(F_true - F_trap):.8f}\n")

print("Метод Симпсона:")
print(f"h = {h1}: {F_simp1:.8f}")
print(f"h = {h2}: {F_simp2:.8f}")
print(f"Рунге-Ромберг: {F_simp:.8f}")
print(f"Погрешность: {abs(F_true - F_simp):.8f}")
