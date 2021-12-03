#Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

from utils import currency_rates_with_time

print(currency_rates_with_time('USD'))
print(currency_rates_with_time('eur'))
print(currency_rates_with_time('XXX'))