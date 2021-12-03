#  Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
#  Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
#  В качестве примера выведите курсы доллара и евро.

from utils import currency_rates

print(currency_rates('USD'))
print(currency_rates('eur'))
print(currency_rates('XXX'))