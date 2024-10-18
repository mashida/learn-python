import requests  # импорт библиотеки requests

LANGUAGES = ['ru', 'en']


def get_quote(lang: str) -> str:
    if lang not in LANGUAGES:
        raise ValueError(f"lang must be 'en' or 'ru', not '{lang}'")

    url = 'http://api.forismatic.com/api/1.0/'  # api endpoint - точка куда мы отправляем запрос
    payload = {  # уточнённые настройки нашего запроса
        'method': 'getQuote',  # мы указываем, что метод - это getQuote или ПолучитьЦитату
        'format': 'text',  # мы указываем, что формат - это json
        'lang': lang}  # мы указываем, что нам нужна цитата на русском языке
    res = requests.get(url,
                       params=payload)  # создал переменную res и сохранил в неё результат работы функции requests.get

    return res.text  # создал переменную data и сохранил в неё результат работы функции res.json


def main() -> None:
    print(f"Выберите на каком языке хотите цитату\n0 - Русский | 1 - Английский: ", end="")
    choice: int = int(input())
    if choice not in [0, 1]:
        raise ValueError(f"Choice can be 0 or 1, not {choice}")
    print(get_quote(LANGUAGES[choice]))


if __name__ == '__main__':
    main()
