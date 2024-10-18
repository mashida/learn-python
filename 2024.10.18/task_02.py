from itertools import count

import requests  # импорт библиотеки requests

LANGUAGES = ['ru', 'en']


def get_list_of_available_countries() -> list[dict[str, str]]:

    url = 'https://date.nager.at/api/v3/AvailableCountries'
    response = requests.get(url).json()

    return response


def main() -> None:
    countries = get_list_of_available_countries()

    for country in countries:
        if country['name'] == 'Russia':
            print(f'Страна Russia, код [{country["countryCode"]}]')
            return

    print(f"Страна Russia не найдена")


if __name__ == '__main__':
    main()
