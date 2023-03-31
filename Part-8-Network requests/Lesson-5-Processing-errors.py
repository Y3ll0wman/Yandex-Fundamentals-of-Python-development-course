# Напишите функцию what_weather(), которую затем будете использовать в коде Анфисы:
# Выполните HTTP-запрос, поместив вызов функции get() внутрь блока try.
# Значения URL и параметров получите из функций make_url() (в неё нужно передать нужный город как аргумент city) и make_parameters().
# При «выбрасывании» исключения типа requests.ConnectionError — функция what_weather() должна возвращать сообщение об ошибке '<сетевая ошибка>'.
# Если код HTTP-ответа равен 200 (всё хорошо), верните из функции текст ответа. В противном случае функция должна вернуть строку '<ошибка на сервере погоды>'.


import requests

cities = [
    'Омск',
    'Калининград',
    'Челябинск',
    'Владивосток',
    'Красноярск',
    'Москва',
    'Екатеринбург'
]


def make_url(city):
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'format': 2,
        'M': ''
    }
    return params


def what_weather(city):
    try:
        response = requests.get(make_url(city), params=make_parameters())
        if response.status_code == 200:
            return response.text
        elif response.status_code != 200:
            return '<ошибка на сервере погоды>'
    except requests.ConnectionError:
        return '<сетевая ошибка>'


print('Погода в городах:')
for city in cities:
    print(city, what_weather(city))
    