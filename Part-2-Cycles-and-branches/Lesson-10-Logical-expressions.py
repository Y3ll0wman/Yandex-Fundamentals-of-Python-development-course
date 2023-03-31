# Замените многоточия в условиях логическим оператором and или or.

for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")

    if current_hour >= 6 and current_hour <= 11:
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour <= 17:
        print('Добрый день!')
    elif current_hour >= 18 and current_hour <= 22:
        print('Добрый вечер!')
    elif current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')

# Научите Анфису информировать вас о новых сообщениях, если их не больше двадцати. Анфиса должна напечатать двадцать одно сообщение подряд:
# У вас нет новых сообщений
# У вас 1 новое сообщение
# ...
# У вас 20 новых сообщений
# Примените логический оператор or и/или and и множественное ветвление с elif, чтобы Анфиса выражалась грамотно. К примеру: «У вас 1 новое сообщение», «У вас 4 новых сообщения», «У вас 11 новых сообщений».

for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас 1 новое сообщение')
    elif messages_count > 1 and messages_count < 5:
        print('У вас', str(messages_count), 'новых сообщения')
    elif messages_count > 4 and messages_count < 21:
        print('У вас', str(messages_count), 'новых сообщений')
    else:
        print('У вас нет новых сообщений')