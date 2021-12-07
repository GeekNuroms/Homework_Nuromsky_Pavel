# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:

def _generator(max_num: int) -> object:
    for digit in range(1, max_num + 1, 2):
        yield digit


nums_gen = _generator(10 ** 3)
print(nums_gen)
print(list(nums_gen))
