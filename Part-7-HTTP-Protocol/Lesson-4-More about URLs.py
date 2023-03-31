# У вас есть запрос «как стать бэкенд-разработчиком». Соберите URL страницы, на которой Яндекс покажет результаты поиска по этому запросу.

user_query = 'как стать бэкенд-разработчиком'
user_query_list = user_query.split(' ')
url = 'https://yandex.ru/search/?text=' + '%20'.join(user_query_list)
print(url)