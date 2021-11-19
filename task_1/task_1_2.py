# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.


CORRECTION_VALUE = 17

def check_number(number: int) -> bool:
    sum = 0
    result = False
    while number > 0:
        sum += number % 10
        number = number // 10
    if not sum % 7:
        result = True
    return result

def check_number_correction (number: int, correction = CORRECTION_VALUE) -> bool:
    if correction:
        number += correction
    return check_number(number)

cube_list = [number**3 for number in range(1, 1001) if number % 2]
sum_7 = sum(list(filter(check_number, cube_list)))
print(sum_7)
defiled_sum_7 = sum(list(filter(check_number_correction, cube_list)))
print(defiled_sum_7)# * Решить задачу под пунктом b, не создавая новый список.
