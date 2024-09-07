"""
Задача 7. Матрицы
Контекст
Вы стажируетесь в лаборатории искусственного интеллекта,
в ней вам поручили разработать класс Matrix для обработки и анализа данных.
Ваш класс должен предоставлять функциональность для выполнения основных операций с матрицами,
таких как сложение, вычитание, умножение и транспонирование.
Это будет полезно для обработки и структурирования больших объёмов данных,
которые используются в обучении нейронных сетей.

Задача
Создайте класс Matrix для работы с матрицами.
Реализуйте методы:
- сложения,
- вычитания,
- умножения,
- транспонирования матрицы.
Создайте несколько экземпляров класса Matrix и протестируйте реализованные операции.
Советы
- Методы сложения/вычитания/умножения должны получать параметром другую матрицу (объект класса Matrix)
    и выполнять указанное действие над своей и этой другой матрицей.
    Например, метод сложения должен получить параметром новую матрицу
    и сложить её со своей текущей.
- Метод транспонирования не должен ничего получать,
    он должен работать исключительно со своей матрицей.
Транспонирование — это алгоритм, при котором строки матрицы меняются местами с её столбцами:
    Алгоритм транспонирования матрицы можно расписать следующим образом:
        - Создать новую матрицу result с размерами, обратными размерам исходной матрицы.
            Количество строк новой матрицы равно количеству столбцов исходной,
            а количество столбцов новой матрицы равно количеству строк исходной.
        - Пройтись по каждому элементу исходной матрицы.
            Для каждого элемента с индексами (i, j):
            Поместить значение этого элемента (i, j) в ячейку с индексами (j, i) новой матрицы.
            То есть транспонирование происходит с помощью обмена индексов местами.
            После завершения цикла новая матрица result будет содержать транспонированную матрицу,
            которую можно вернуть.
"""


class Matrix:

    def __init__(self, row: int, column: int, data=[]):
        self.row = row
        self.column = column
        self.data = data

    def __str__(self):
        matrix_str = ''
        for row in self.data:
            matrix_str += '|'
            for elem in row:
                matrix_str += str(elem) + ' '
            matrix_str += '|\n'
        return matrix_str

    def __add__(self, other):
        new_matrix = list()
        for row_1, row_2 in zip(self.data, other.data):
            new_row = [elem_1 + elem_2 for elem_1, elem_2 in zip(row_1, row_2)]
            new_matrix.append(new_row)
        return Matrix(self.row, self.column, new_matrix)

    def __sub__(self, other):
        new_matrix = list()
        for row_1, row_2 in zip(self.data, other.data):
            new_row = [elem_1 - elem_2 for elem_1, elem_2 in zip(row_1, row_2)]
            new_matrix.append(new_row)
        return Matrix(self.row, self.column, new_matrix)

    def __mul__(self, other):
        # Результатом умножения матрицы Am×n на матрицу Bn×k будет матрица Cm×k такая,
        # что элемент матрицы C, стоящий в i-той строке и j-том столбце (cij),
        # равен сумме произведений элементов i-той строки матрицы A на соответствующие
        # элементы j-того столбца матрицы B.
        # Две матрицы можно перемножить если количество столбцов первой матрицы равно
        # количеству строк второй матрицы.

        if isinstance(other, (int, float)):
            new_matrix = Matrix(self.row, self.column, self.data)
            new_matrix.data = list()
            for row in self.data:
                new_row = [elem * other for elem in row]
                new_matrix.data.append(new_row)

        else:
            new_matrix = Matrix(self.row, other.column)
            new_matrix.data = [[None for _ in range(other.column)] for _ in range(self.row)]

            for i, row in enumerate(new_matrix.data):
                for j, elem in enumerate(row):
                    new_matrix.data[i][j] = sum(self.data[i][k] * other.data[k][j]
                                                for k in range(len(other.data)))

        return new_matrix

    def transpose(self):
        transpose_matrix = Matrix(self.column, self.row)
        for j in range(self.column):  # Creates sample matrix
            new_row = [None for _ in range(self.row)]
            transpose_matrix.data.append(new_row)

        for i, row in enumerate(self.data):
            for j, elem in enumerate(row):
                transpose_matrix.data[j][i] = elem

        return transpose_matrix


def create_matrix(row, column):
    matrix = list()
    for i in range(row):
        print(f'Enter {i + 1}-row through space:')
        row = input('').split()
        row = [int(elem) for elem in row]
        matrix.append(row)
    return matrix


m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]
print(f'Matrix 1:\n{m1}')
m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]
print(f'Matrix 2:\n{m2}')
m_addition = m1 + m2
print(f'Addition of matrix:\n{m_addition}')
m_sub = m1 - m2
print(f'Subtraction of matrix:\n{m_sub}')
m_3 = Matrix(3, 2)
m_3.data = [[1, 2], [3, 4], [5, 6]]
print(f'Matrix 3:\n{m_3}')
m_mul = m1 * m_3
print(f'Multiple of matrix m1 and m3:\n{m_mul}')
m_mul_constant = m1 * 2
print(f'Multiple of matrix m1 and constant 2:\n{m_mul_constant}')
m_transpose = m1.transpose()
print(f'Transpose m1:\n{m_transpose}')

