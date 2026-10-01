from math import sqrt


def multiply(A, B):
    n = len(A)
    m = len(B[0])
    k = len(B)

    C = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for l in range(k):
                C[i][j] += A[i][l] * B[l][j]

    return C


def qr_decomp(A):
    n = len(A)

    Q = [[0.0] * n for _ in range(n)]
    R = [[0.0] * n for _ in range(n)]

    for j in range(n):
        v = [A[i][j] for i in range(n)]

        for i in range(j):
            R[i][j] = sum(
                Q[k][i] * A[k][j]
                for k in range(n)
            )

            for k in range(n):
                v[k] -= R[i][j] * Q[k][i]

        R[j][j] = sqrt(
            sum(x * x for x in v)
        )

        for k in range(n):
            Q[k][j] = v[k] / R[j][j]

    return Q, R


def qr_algorithm(A, eps):
    n = len(A)

    iterations = []

    while True:
        Q, R = qr_decomp(A)

        A = multiply(R, Q)

        error = 0

        for i in range(n):
            for j in range(i - 1):
                error += A[i][j] * A[i][j]

        error = sqrt(error)

        iterations.append(error)

        if error < eps:
            break

    return A, iterations


def eigenvalues(A, eps):
    n = len(A)
    values = []

    i = 0

    while i < n:

        if i == n - 1 or abs(A[i + 1][i]) < eps:
            values.append(A[i][i])
            i += 1

        else:
            a = A[i][i]
            b = A[i][i + 1]
            c = A[i + 1][i]
            d = A[i + 1][i + 1]

            trace = a + d
            determinant = a * d - b * c

            discriminant = (
                trace * trace
                - 4 * determinant
            )

            if discriminant >= 0:
                x1 = (trace + sqrt(discriminant)) / 2

                x2 = (trace - sqrt(discriminant)) / 2

                values.append(x1)
                values.append(x2)

            else:
                real = trace / 2
                imaginary = sqrt(-discriminant) / 2

                values.append(
                    complex(real, imaginary)
                )

                values.append(
                    complex(real, -imaginary)
                )

            i += 2

    return values


if __name__ == "__main__":

    A = [
        [-5, -8, 4],
        [4, 2, 6],
        [-2, 5, -6]
    ]

    eps = 0.00001

    A_qr, iterations = qr_algorithm(A, eps)

    values = eigenvalues(A_qr, eps)

    print("Собственные значения:")

    for value in values:
        if isinstance(value, complex):
            print(
                round(value.real, 2),
                "+",
                round(value.imag, 2),
                "i"
            )
        else:
            print(round(value, 2))

    print("\nКоличество затраченных итераций:")
    print(len(iterations))