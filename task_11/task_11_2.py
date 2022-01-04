# Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class Nizya(ZeroDivisionError):
    def __str__(self):
        return 'Импортозамещение ZeroDivisionError удалось'


def div(a, b):
    try:
        if not b:
            raise Nizya
        return print(a / b)
    except Nizya as proryv:
        return print(proryv)

div(100, 0)
div(100, 10)
