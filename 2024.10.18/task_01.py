import requests  # импорт библиотеки requests

url = 'http://api.forismatic.com/api/1.0/' # создал и инициировал переменную url
payload = {'method': 'getQuote', 'format': 'json', 'lang': 'ru'} # создал какой-то словарь
res = requests.get(url, params=payload) # создал переменную res и сохранил в неё результат работы функции requests.get

data = res.json() # создал переменную data и сохранил в неё результат работы функции res.json

print(data) # вывел data на экран
