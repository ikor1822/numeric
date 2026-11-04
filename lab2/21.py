
import matplotlib.pyplot as plt
import math

def phi(x):
    expr = -x ** 2 + 2 * x + 1

    return math.copysign(abs(expr) ** (1 / 3), expr)


def simple_iteration_method(a, b, epsilon, max_iter=100):

    x = b

    for i in range(101):
        val = a + (b - a) * i / 100
        phi_val = phi(val)

        if not (a <= phi_val <= b):
            print("Функция phi(x) выходит за пределы интервала.")
            return

    for k in range(max_iter):
        x_new = phi(x)

        if abs(x_new - x) < epsilon:
            print(
                f"Метод простой итерации: "
                f"корень = {x_new:.7f}, итераций = {k + 1}"
            )
            return x_new

        x = x_new

    print("Не удалось найти корень за максимальное количество итераций")




def f(x):
    return x**3 + x**2 - 2*x - 1


def df(x):
    return 3*x**2 + 2*x - 2


def ddf(x):
    return 6*x + 2


def newton_method(a, b, epsilon, max_iter=100):

    x = (a + b) / 2

    if f(a) * f(b) >= 0:
        print("Начальное приближение не подходит")
        return


    check_a = False
    check_b = False

    if abs(f(a) * ddf(a)) < df(a) * df(a):
        check_a = True

    if abs(f(b) * ddf(b)) < df(b) * df(b):
        check_b = True

    if check_b and check_a:
        if f(b) * ddf(b) <= 0:
            print("Начальное приближение не подходит")
            return

    if check_a:
        x = a

    if check_b:
        x = b

    for k in range(max_iter):

        x_new = x - f(x) / df(x)

        if abs(x_new - x) < epsilon:
            print(
                f"Метод Ньютона: "
                f"корень = {x_new:.7f}, итераций = {k + 1}"
            )
            return x_new

        x = x_new

    print("Не удалось найти корень за максимальное количество итераций")




def f1(x):
    return x**3 + x**2


def f2(x):
    return 2*x + 1


x = [i * 0.01 for i in range(-300, 300)]

y1 = [f1(i) for i in x]
y2 = [f2(i) for i in x]

plt.figure(figsize=(8, 6))

plt.plot(x, y1, label='$f_1(x) = x^3 + x^2$')
plt.plot(x, y2, label='$f_2(x) = 2x + 1$')

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.grid()
plt.legend()

plt.show()


x0_a = 1
x0_b = 1.5

epsilon = 1e-6

newton_method(x0_a, x0_b, epsilon)

simple_iteration_method(x0_a, x0_b, epsilon)
