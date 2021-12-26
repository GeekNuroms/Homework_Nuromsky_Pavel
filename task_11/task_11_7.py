# Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число».
# Реализовать перегрузку методов сложения и умножения комплексных чисел.
# Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа), выполнить сложение
# и умножение созданных экземпляров. Проверить корректность полученного результата.


class Complex:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __add__(self, other):
        return Complex(self.i + other.i, self.j + other.j)

    def __mul__(self, other):
        i = self.i * other.i - self.j * other.j
        j = self.i * other.j + self.j * other.i
        return Complex(i, j)



complex1 = Complex(3, 1)
complex2 = Complex(2, -3)
print(vars(complex1+complex2))
print(vars(complex1*complex2))