a = [[1.0, 3.0, 1.0],
     [3.0, 3.0, 1.0],
     [5.0, 12.0, 2.0]]
b = [1.0, 2.0, 3.0]


def mat_print(m):
    for el in m:
        print(el)
    print()


def gauss(matrix, tail):
    n = len(matrix)

    # прямой ход метода Гаусса
    for i in range(n-1):

        # нахождение максимального элемента по матрице
        max_el = matrix[i][i]
        max_x = i
        max_y = i
        for j in range(i, n):
            for k in range(i, n):
                if abs(matrix[j][k]) > abs(max_el):
                    max_el = matrix[j][k]
                    max_x = k
                    max_y = j

        # обмен строками, если максимальный элемент не на текущей строке
        if max_y != i:
            matrix[i], matrix[max_y] = matrix[max_y], matrix[i]
            tail[i], tail[max_y] = tail[max_y], tail[i]

        # обмен столбцами, если максимальный элемент не на текущем столбце
        if max_x != i:
            for j in range(n):
                matrix[j][max_x], matrix[j][i] = matrix[j][i], matrix[j][max_x]

        # приведение к верхнетреугольному виду
        for j in range(i+1, n):
            ratio = matrix[j][i]  # todo мб сделать ratio = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= matrix[i][k] * (ratio/matrix[i][i])
            tail[j] -= tail[i] * (ratio/matrix[i][i])  # todo здесь проверить на что делится


    # обратный ход метода Гаусса
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = tail[i]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]

        x[i] /= matrix[i][i]

    return x


if __name__ == "__main__":
    print(gauss(a, b))
