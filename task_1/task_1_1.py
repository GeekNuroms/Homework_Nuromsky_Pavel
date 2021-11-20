### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.


def duration_calculator(duration:int, divider: int) -> tuple:
    ###не уверен, что тип данных на выходе именно кортеж, но не знаю как описать это корректнее
    result = duration // divider
    remains = duration % divider
    return result, remains

def time_formating(duration: str) -> str:
    if not duration.isdigit():
        return 'Некорректное значение продолжительности времени - должно быть целым'
    _duration = int(duration)
    days, remaining_duration = duration_calculator(_duration, 60*60*24)
    hours, remaining_duration = duration_calculator(remaining_duration, 60*60)
    minutes, remaining_duration = duration_calculator(remaining_duration, 60)
    sec, remaining_duration = duration_calculator(remaining_duration, 1)
    result_list = [(days, 'дн'), (hours, 'час'), (minutes, 'мин'), (sec, 'сек')]
    result = ' '.join([f'{value[0]} {value[1]}' for value in result_list if value[0]])
    return result

if __name__ == '__main__':
    duration = input('Введите значение продолжительности в секундах')
    print(time_formating(duration))

    ###Testing_zone
    # for number in range(7):
    #     number = 10 ** number
    #     print(number, time_formating(str(number)))


