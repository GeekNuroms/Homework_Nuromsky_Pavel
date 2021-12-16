# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

def test(_: object):
    print('_'*100)
    print(vars(_))
    _.turn('left')
    _.go()
    _.show_speed()
    _.go()
    _.show_speed()
    print('\n')


class Car:

    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        self.speed = self.speed + 20

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        print(f'{self.name} turn to {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        message = self.speed if self.speed <= 60 else f'Чуть помедленнее {self.name}, чуть помедленнее ({self.speed})'
        print(message)


class SportCar(Car):

    def go(self):
        self.speed = self.speed + 120


class WorkCar(Car):

    def show_speed(self):
        message = self.speed if self.speed <= 40 else f'Чуть помедленнее {self.name}, чуть помедленнее ({self.speed})'
        print(message)


class PoliceCar(Car):

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)
        self.is_police = True


car = Car(40, 'black', 'abc')
test(car)
car = TownCar(40, 'black', 'TownCar')
test(car)
car = SportCar(40, 'black', 'SportCar')
test(car)
car = WorkCar(40, 'black', 'WorkCar')
test(car)
car = PoliceCar(40, 'black', 'PoliceCar')
test(car)
