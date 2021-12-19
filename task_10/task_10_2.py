# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def wages(self):
        pass


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        # self.wages = None

    @property
    def wages(self):
        return self.height*2 + 0.3


class HorseSuit(Clothes):
    def __init__(self, size):
        self.size = size
        # self.wages = None

    @property
    def wages(self):
        return self.size/6.5 + 0.5


model_a = Suit(120)
print(model_a.wages)
model_b = HorseSuit(120)
print(model_b.wages)
print(model_a.wages + model_b.wages)