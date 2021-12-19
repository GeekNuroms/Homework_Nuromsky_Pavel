# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных:
# создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

income_dict = {
    'slave': {'wage': 300,
              'bonus': -300}
}


class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income.get(position)


class Position(Worker):

    def get_full_name(self):
        return f'{self.name.capitalize()} {self.surname.capitalize()}'

    def get_total_income(self):
        return sum(self._income.values())


anton = Position('toNy', 'staRk', 'slave', income_dict)
print(vars(anton))
print(anton.get_full_name(), anton.get_total_income())
