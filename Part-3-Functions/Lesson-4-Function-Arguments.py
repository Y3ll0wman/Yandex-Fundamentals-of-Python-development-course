# Функция lets_go() ожидает на вход два аргумента. Если вызвать её без аргументов — она сломается.
# Измените объявление функции так, чтобы при вызове без аргументов она напечатала фразу Друг, пойдём учить Python.


def lets_go(name='Друг', target='учить Python'):
    print(name + ', пойдём ' + target)


lets_go()

# Если при вызове функции lets_go() передавать неименованные аргументы, то передать только второй аргумент не получится: функция передаст единственный аргумент в параметр name, а не в target, как нам хотелось бы.
# Исправьте вызов функции так, чтобы аргумент, указанный при вызове, был передан в параметр target. Вызов с именованными аргументами поможет решить эту задачу.


def lets_go(name='Друг', target='учить Python'):
    print(name + ', пойдём ' + target)


lets_go(target='читать следующий урок!')