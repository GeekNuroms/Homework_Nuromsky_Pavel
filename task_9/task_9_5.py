# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = f'{title} чувствует себя бесполезным'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'В сети появились фото 18+ {__class__.__name__}')


class Pencil(Stationery):
    def draw(self):
        print(f'ОГО! Ученые узнали, что {__class__.__name__}...')


class Handle(Stationery):
    def draw(self):
        print(f'ШОК! {__class__.__name__} помогает при растройствах...')

pen = Stationery('picle')
pen.draw()
pen = Pen('picle')
pen.draw()
pen = Pencil('picle')
pen.draw()
pen = Handle('picle')
pen.draw()
