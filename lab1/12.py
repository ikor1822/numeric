def tridiagonal_solve(a, b, c, d):
    n = len(b)

    for i in range(n):
        if i == 0:
            if abs(b[i]) <= abs(c[i]):
                return
        elif i == n - 1:
            if abs(b[i]) <= abs(a[i - 1]):
                return
        else:
            if abs(b[i]) < abs(a[i - 1]) + abs(c[i]):
                return

    p = [0] * n
    q = [0] * n

    p[0] = c[0] / b[0]
    q[0] = d[0] / b[0]

    for i in range(1, n - 1):
        z = b[i] - a[i - 1] * p[i - 1]
        p[i] = c[i] / z
        q[i] = (d[i] - a[i - 1] * q[i - 1]) / z

    q[n - 1] = (d[n - 1] - a[n - 2] * q[n - 2]) / (b[n - 1] - a[n - 2] * p[n - 2])

    x = [0] * n
    x[n - 1] = q[n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = q[i] - p[i] * x[i + 1]

    return [round(val, 6) for val in x]


a = [-2, 2, -8, -7] 
b = [8, 12, -9, 17, 13] 
c = [-4, -7, 1, -4] 
d = [32, 15, -10, 133, -76]

x = tridiagonal_solve(a, b, c, d)

print("Решение системы:", x)