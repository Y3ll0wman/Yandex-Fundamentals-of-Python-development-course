# Научите Анфису сообщать время в формате ЧЧ:ММ:СС (часы, минуты, секунды).
# Программа должна напечатать На часах 19:28:06.


def print_time(hour, minute, second):
    print(f'На часах {hour}:{minute}:{second}')


print_time('19', '28', '06')

# Анфиса получила список listened с длительностью прослушанных песен (в секундах).
# Функция calc_stat() должна вернуть строку, в которой указано количество прослушанных песен: 'Вы прослушали N песен.', где N — длина списка listened.


def calc_stat(listened):
    len_listened = len(listened)
    return(f'Вы прослушали {len_listened} песен.')
print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))

# Допишите функцию calc_stat(): выведите на экран суммарную статистику.
# 'Вы прослушали N песен общей продолжительностью M минут.'
# N — длина списка listened;
# M — количество целых минут общей продолжительности прослушанных песен.


def calc_stat(listened):
    len_listened = len(listened)
    sec_listened = 0
    for m in listened:
        sec_listened += m
        min_listened = sec_listened // 60
    return(f'Вы прослушали {len_listened} песен общей продолжительностью {min_listened} минут.')
print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))

# Вы знаете об f-строках достаточно, чтобы оптимизировать код Анфисы. Все фразы, которые сейчас составляет Анфиса, создаются через конкатенацию строк: фрагменты строк и значения переменных объединяются оператором +.
# Сделайте код проще: замените конкатенацию на f-строки. В коде отмечены места, где это нужно сделать.


DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return f'У тебя {str(count)} друзей.'
    elif query == 'Кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'Где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'

print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))