# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый — с декоратором @classmethod. Он должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

from datetime import datetime


class Date:

    def __init__(self, mydate: str):
        self.date = mydate

    @classmethod
    def get_time(cls) -> tuple:
        cls.date = datetime.now().strftime('%d-%m-%y').split('-')
        cls.day, cls.month, cls.year = map(int, cls.date)
        return cls.day, cls.month, cls.year

    @staticmethod
    def validation(_date: tuple[int, int, int]) -> bool:
        result = False
        if len(_date) == 3:
            if all([isinstance(value, int) for value in _date]):
                if _date[0] in range(1, 32) and _date[1] in range(1, 13):
                    result = True
        return result


date = Date(datetime.now().strftime('%d-%m-%y'))
print(date.date, Date.get_time(), Date.validation(Date.get_time()), date.validation((32, 12, 21)))