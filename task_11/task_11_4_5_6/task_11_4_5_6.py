# Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведённых типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
from abc import ABC

class Tech(ABC):
    def __init__(self, input_dict: dict):
        self.name = input_dict.get('name')
        self.price = input_dict.get('price')

    def work(self):
        pass

class Printer(Tech):
    type = 'printer'
    @property
    def work(self):
        return 'Print'

class Scaner(Tech):
    type = 'scaner'
    @property
    def work(self):
        print('Сканирую сетчатку глаза, ой')
        return 'Scan'

class Xerox(Tech):
    type = 'xerox'
    @property
    def work(self):
        return 'Xerx The Great'


class Placement(ABC):
    def __init__(self, input_dict: dict):
        if self.basic_validation(input_dict):
            self.store = input_dict
        else:
            print('Должно быть тут какая-то ошибка в документах, не можем открыть офис, налоговая не пропустит')


    @staticmethod
    def basic_validation(input_dict):
        for tech, number in input_dict.items():
            if tech not in ('printer', 'scaner', 'xerox') or not isinstance(number, int):
                return False
            elif number < 0:
                return False
        return True

    @property
    def get_info(self):
        return self.store or {}


class MinorOffice(Placement):
    def value_validation(self, input_dict: dict):
        for tech, value in input_dict.items():
            if self.store.get(tech) - value < 0:
                print(f'Нет столько {tech}')
                return False
            break
        return True

    def make_incident_report(self, tech, destroy_counter=1):
        report = {tech_key: destroy_counter if tech_key == tech.type else 0 for tech_key in ('printer', 'scaner', 'xerox')}
        self.utilize(report)
        report_texr = f'В результате происшествия потерян {destroy_counter} ценный {tech.type} {tech.name}' \
                      f' стоимостью {tech.price} bucks и 1 бесценный стажер'
        return report_texr

    def utilize(self, change_dict):
        if self.value_validation(change_dict):
            self.store = {tech: self.store.get(tech) - value for tech, value in change_dict.items()}

    def get_new_tech(self, change_dict):
        self.store = {tech: self.store.get(tech) + value for tech, value in change_dict.items()}

    def make_some_work(self, tech):
        print(f'Стажер, не поломай {tech.type} {tech.name}, он стоит целых {tech.price} bucks')


class CentralOffice(MinorOffice):

    def create_department(self, start_dict):
        if self.value_validation(start_dict):
            self.store = {tech: self.store.get(tech) - value for tech, value in start_dict.items()}
            return MinorOffice(start_dict)

start_capital = {
'printer': 100,
'scaner': 100,
'xerox': 100
}
new_capital = {
'printer': 10,
'scaner': 10,
'xerox': 10
}
tech_dict = {
'name': 't1000',
'price': 20,
}
office1 = CentralOffice(start_capital)
print(office1.get_info)
office2 = office1.create_department(new_capital)
print(office1.get_info)
print(office2.get_info)
office2.get_new_tech(new_capital)
print(office2.get_info)
office2.utilize(new_capital)
print(office2.get_info)
machine = Scaner(tech_dict)
office2.make_some_work(machine)
machine.work
print(office2.make_incident_report(machine))
print(office2.get_info)

start_capital = {
'printer': 'n',
'scaner': 100,
'xerox': 100
}

office1 = CentralOffice(start_capital)

