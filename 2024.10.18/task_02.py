from itertools import count

import requests  # импорт библиотеки requests

LANGUAGES = ['ru', 'en']


def get_list_of_available_countries() -> list[dict[str, str]]:

    url = 'https://date.nager.at/api/v3/AvailableCountries'
    response = requests.get(url).json()

    return response

def get_dict_of_countries_out_of_list(c: list[dict[str, str]]):
    result = dict()
    for country in c:
        result[country['name']] = country['countryCode']

    return result

# или однострочник
# def get_dict_of_countries_out_of_list(c: list[dict[str, str]]):
    # return dict((country['name'], country['countryCode']) for country in c)


def main() -> None:
    list_of_countries = get_list_of_available_countries()
    dict_of_countries = get_dict_of_countries_out_of_list(list_of_countries)

    if 'Russia' in dict_of_countries:
        print(f'Страна Russia, код [{dict_of_countries["Russia"]}]')
    else:
        print(f"Страна Russia не найдена")


if __name__ == '__main__':
    main()
