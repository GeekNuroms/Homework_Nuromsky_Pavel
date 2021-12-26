# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

import itertools


def validator(input_matrix: list) -> tuple:
    try:
        mod_matrix = (list(
            [isinstance(input_list, list)] + [isinstance(val, int) for val in input_list] if input_list else [False]
            for input_list in input_matrix))
        # print(f'Первичное преобразование: {mod_matrix}')
        final_matrix = (set(itertools.chain(*mod_matrix)))
        # print(f'Конечное множество: {final_matrix}')
        if False not in final_matrix:
            size_a = len(mod_matrix)
            set_b = {len(val) for val in mod_matrix}
            if len(set_b) == 1:
                return True, (size_a, set_b.pop()-1)
        return False, None
    except TypeError as err:
        return False, err


class Matrix:
    """Вот и день прошел, дети в слезах смотрят на фото отца, пока я писал этот класс"""
    def __init__(self, matrix_list: list):
        self.matrix_is_correct = None
        self.size_a = None
        self.size_b = None
        self.values = matrix_list

    @property
    def matrix_validation(self):
        """Тип данных список списков
        Значения целые
        длина вложенных списков одинакова"""
        self.matrix_is_correct, size = validator(self.values)
        if self.matrix_is_correct:
            self.size_a, self.size_b = size
        return f'Is {self.__class__.__name__} correct: {self.matrix_is_correct}'

    def __str__(self):
        return '\n'.join([f"| {' '.join(map(str, line))} |" for line in self.values])

    def __add__(self, other):
        # for row in zip(self.values, other.values):
        #     print(row)
        #     for value in zip(*row):
        #         print(sum(value))
        return Matrix([[sum(value) for value in zip(*row)] for row in zip(self.values, other.values)])


input_list1 = [[1, 34, 66], [4, 66, 88]]
input_list2 = [[1, 34, 66], [4, 66]]
input_list3 = [[1, 34, 66], [4, 66, ';;;']]
input_list4 = [[2, 3, 4], [2, 1, 4]]


# print(validator(input_list1))
# print(validator(input_list2))
# print(validator(input_list3))

#
matrix1 = Matrix(input_list1)
print(f'{matrix1.matrix_validation}\n{vars(matrix1)}')
print(matrix1)

matrix2 = Matrix(input_list2)
# print(f'{matrix2.matrix_validation}\n{vars(matrix2)}')
matrix3 = Matrix(input_list3)
# print(f'{matrix3.matrix_validation}\n{vars(matrix3)}')

matrix4 = Matrix(input_list4)
print(f'{matrix4.matrix_validation}\n{vars(matrix4)}')
print(matrix4)

matrix5 = matrix1 + matrix4
print(matrix5)
print(f'{matrix5.matrix_validation}\n{vars(matrix5)}')
