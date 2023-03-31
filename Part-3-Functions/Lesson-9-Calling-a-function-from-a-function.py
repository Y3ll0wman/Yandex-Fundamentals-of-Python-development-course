# Программа делает всё, что требовалось Афанасию: рассчитывает количество материала, необходимое для строительства восьми кубов. А если понадобится сделать три куба или десять?
# Сделайте программу более универсальной, измените её так, чтобы в неё можно было передать не только сторону куба, но и количество кубов. Для этого понадобится второй аргумент в функции calc_cube()
# Измените строку, в которой объявляется функция calc_cube(): добавьте второй аргумент (назовите его, например, amount).
# В тех строках функции calc_cube(), где используется число кубов, используйте значение переменной amount.
# В строке, которую печатает функция, выводится количество кубов; там тоже потребуется вывести значение переменной amount.


def calc_cube_perimeter(side):
    return side * 12


def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area


def calc_cube(side, amount):
    one_cube_perimeter = calc_cube_perimeter(side)

    full_length = one_cube_perimeter * amount

    one_cube_area = calc_cube_area(side)

    full_area = one_cube_area * amount

    print('Для', amount, 'кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area)


calc_cube(3, 2)

# Афанасий опубликовал свою программу, прославился — и к нему потянулись заказчики: оказалось, что очень многим знаменитым компаниям нужны кубы из стекла и палок.
# Компания Microgates заказала четыре кубика с ребром 2 метра: они хотят водрузить их на крыше своего здания.
# Компания RubiCUBE сделала заказ на 26 кубиков с ребром 0.5 м: их логотип выглядит как кубик Рубика, развалившийся на части; они решили установить инсталляцию перед главным офисом.
# Школа программирования Питоникум заказала подиум для студентов-чемпионов: шесть кубиков с ребром 0.61 м.
# Сделайте три вызова функции calc_cube() с нужными аргументами, чтобы рассчитать объём материалов для каждого заказа.


def calc_cube_perimeter(side):
    return side * 12


def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area


def calc_cube(side, amount):
    one_cube_perimeter = calc_cube_perimeter(side)
    full_length = one_cube_perimeter * amount
    one_cube_area = calc_cube_area(side)
    full_area = one_cube_area * amount
    print('Для', amount, 'кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area)


calc_cube(2,4)
calc_cube(0.5,26)
calc_cube(0.61,6)
