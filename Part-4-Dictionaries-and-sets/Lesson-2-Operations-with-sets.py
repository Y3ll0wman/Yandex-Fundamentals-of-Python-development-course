# Научим Анфису играть в города. У неё в памяти хранится два перечня городов:
# в множестве all_cities хранятся все города, которые она знает,
# в множестве used_cities — города, которые уже были названы в игре, их уже нельзя использовать.
# Научите Анфису получать перечень городов, которые ещё не были названы в игре.
# В коде объявлена функция: def print_valid_cities(...), допишите её.
# Она должна:
# принять на вход множества all_cities и used_cities;
# создать множество городов, которые ещё не использовались в игре; для этого функция должна найти разницу множеств all_cities и used_cities;
# построчно напечатать элементы получившегося множества на экране.


def print_valid_cities(all_cities, used_cities):
    valid_cities = all_cities.difference(used_cities)
    for city in valid_cities:
        print(city)

all_cities = {
    'Абакан',
    'Астрахань',
    'Бобруйск',
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк',
    'Новосибирск'
}

used_cities = {'Калуга', 'Абакан' , 'Новосибирск'}

print_valid_cities(all_cities, used_cities)

# Игра в города продолжается. Анфиса покопалась в сети и нашла дополнительный список городов для игры. Но у неё нет инструмента, чтобы добавить новые города в множество all_cities.
# Напишите функцию add_cities(), которая добавит элементы из списка new_cities в all_cities.
# Метод union() для этой задачи не подходит, ведь вам нужно добавить элементы в существующее множество, а не создать новое.


def print_valid_cities(all_cities, used_cities):
    diff = all_cities.difference(used_cities)
    for city in diff:
        print(city)


def add_cities(all_cities, new_cities):
    for city in new_cities:
        all_cities.add(city)


new_cities = [
    'Екатеринбург',
    'Выборг' ,
    'Владивосток',
    'Казань',
    'Why',
    'Йезд'
]

all_cities = {
    'Абакан',
    'Астрахань',
    'Бобруйск',
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк',
    'Новосибирск'
}

used_cities = {
    'Калуга',
    'Абакан' ,
    'Новосибирск'
}

add_cities(all_cities, new_cities)
print_valid_cities(all_cities, used_cities)

# Бот Анфиса и бот Алиса хотят сыграть во что-нибудь по сети. Каждая из них составила список игр, в которые она умеет играть. Списки, конечно же, разные, но, возможно, найдутся игры, которые знакомы им обеим.
# Вам нужно написать программу, которая найдёт одинаковые элементы в двух списках.
# Допишите функцию get_together_games(): она должна принимать на вход два списка, а возвращать — множество игр, названия которых есть в обоих списках.
# Получите из функции это множество и построчно напечатайте его элементы (названия игр); перед названием каждой игры поставьте эмоджи 👾 и пробел. Эмоджи — это текстовый символ, как дефис или буква, его можно скопировать из условия и вставить в код.
# Результат должен выглядеть примерно так:
# 👾 Super Hero Developer
# 👾 Python Shooter
# 👾 Online-backgammon


def get_together_games(game_1, game_2):
    together_games = set(game_1).intersection(set(game_2))
    return together_games


anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
together_games = get_together_games(anfisa_games, alisa_games)

for game in together_games:
    print('👾', game)