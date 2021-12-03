import requests
from datetime import datetime, date

def currency_rates(_id: str) -> float:
    _id = _id.upper()
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    req = requests.get(url)
    req.close()
    row_data = requests.get(url).content.decode("windows-1251")
    valute_list = row_data.split('Valute ID')
    _time = valute_list[0].split('"')[5]
    currency_dict = {}
    for valute in valute_list[1:]:
        currency_dict.update(parse_list(valute))
    if currency_dict.get(_id):
        return currency_dict.get(_id).get('value')


def parse_list(string: str) -> dict:
    valute_id, nominal, name, value = tuple(string.split('</')[1:5])
    _dict = {}
    _dict[valute_id.split('>')[-1]] = {
        'nominal': nominal.split('>')[-1],
        'name': name.split('>')[-1],
        'value': value.split('>')[-1]
    }
    return _dict


def currency_rates_with_time(_id: str) -> tuple or None:
    _id = _id.upper()
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    req = requests.get(url)
    req.close()
    row_data = requests.get(url).content.decode("windows-1251")
    valute_list = row_data.split('Valute ID')
    _time = (valute_list[0].split('"')[5].split('.'))
    _time = datetime(year=int(_time[2]), month=int(_time[1]), day=int(_time[0]))#.strftime("%d-%m-%y")
    currency_dict = {}
    for valute in valute_list[1:]:
        currency_dict.update(parse_list(valute))
    if currency_dict.get(_id):
        return currency_dict.get(_id).get('value'), _time, type(_time,)

def currency_rates_with_time_console(valutes:list) -> tuple or None:
    valutes = valutes[1:]
    if not valutes:
        return
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    req = requests.get(url)
    req.close()
    row_data = requests.get(url).content.decode("windows-1251")
    valute_list = row_data.split('Valute ID')
    _time = (valute_list[0].split('"')[5].split('.'))
    _time = datetime(year=int(_time[2]), month=int(_time[1]), day=int(_time[0])).strftime("%y-%m-%d")
    currency_dict = {}
    for valute in valute_list[1:]:
        currency_dict.update(parse_list(valute))
    for _id in valutes:
        _id = _id.upper()
        if currency_dict.get(_id):
            print(f"{currency_dict.get(_id).get('value')}, {_time}")
