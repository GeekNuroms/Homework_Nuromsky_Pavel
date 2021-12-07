# ### 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# ```
#
# Подсказка: использовать возможности python, изученные на уроке.
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([value for position, value in enumerate(src) if position != 0 and value > src[position-1]])