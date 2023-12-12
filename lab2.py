def gauss(matrix, tail):
    n = len(matrix)
    x_order = [i for i in range(n)]  # считает порядок x по столбцам

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

            x_order[i], x_order[max_x] = x_order[max_x], x_order[i]

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
        if matrix[i][i] == 0:
            raise Exception("Матрица вырожденная. Решение СЛАУ методом Гаусса невозможно")
        else:
            x[i] /= matrix[i][i]

    result = []
    for i in range(n):
        result.append((x[i], x_order[i]))
    result.sort(key=lambda z: z[1])

    return [z[0] for z in result]


def read_matrix():
    matrix = []
    tail = []
    with open('input.txt') as file:
        for line in file.readlines():
            if line == "\n" or line == "":
                continue
            separated_line = line.split()
            matrix.append(list(map(float, separated_line[:-1])))
            tail.append(float(separated_line[-1]))
    return matrix, tail


if __name__ == "__main__":
    a, b = read_matrix()
    try:
        solution = gauss(a, b)
        print('Корни СЛАУ:')
        for i in range(len(solution)):
            print(f'X{i + 1} = {round(solution[i], 10)}')
    except Exception as e:
        print(e)


# https://mipt.lectoriy.ru/lecture/Maths-NumAnalysis-L03-Aristova-140917.03?video=local#materials
