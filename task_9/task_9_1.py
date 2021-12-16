# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
from termcolor import cprint
import random


class TrafficLight:
    """Если смотреть достаточно долго, то можно увидеть, как зеленый горит 6(!) секунд вместо 7"""

    def __init__(self):
        self.__color = {
            'red': (7, 'STOP '),
            'yellow': (2, 'READY'),
            'green': (7, ' GO  ')
        }

    def running(self):
        while True:
            for color_value in self.__color.keys():
                cprint(self.__color[color_value][1], 'grey', f'on_{color_value}', attrs=['dark', 'blink', 'concealed'])
                timeshift = 1 if color_value == 'green' and random.randint(0, 1000) == 1 else 0
                time.sleep(self.__color[color_value][0] - timeshift)


my_intresting_life = TrafficLight()
my_intresting_life.running()
