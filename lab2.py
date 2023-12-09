# a = [[1.0, 3.0, 1.0],
#      [3.0, 3.0, 1.0],
#      [5.0, 12.0, 2.0]]
# b = [1.0, 2.0, 3.0]


def gauss(matrix, tail):
    n = len(matrix)

    # прямой ход
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
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= matrix[i][k] * ratio
            tail[j] -= tail[i] * ratio

    # обратный ход
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = tail[i]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]

    return x


def read_matrix():
    matrix = []
    tail = []
    with open('input.txt') as file:
        for line in file.readlines():
            separated_line = line.split()
            matrix.append(list(map(float, separated_line[:-1])))
            tail.append(float(separated_line[-1]))
    return matrix, tail


if __name__ == "__main__":
    a, b = read_matrix()
    print(gauss(a, b))
