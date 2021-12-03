# Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.


def odd_gen(max_num: int) -> object:
    return (digit for digit in range(1, max_num + 1, 2))


nums_gen = odd_gen(10 ** 3)
print(nums_gen)
print(list(nums_gen))
