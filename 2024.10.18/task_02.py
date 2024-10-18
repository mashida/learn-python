import requests  # импорт библиотеки requests

LANGUAGES = ['ru', 'en']


def get_list_of_available_countries() -> list[dict[str, str]]:

    url = 'https://date.nager.at/api/v3/AvailableCountries'
    res = requests.get(url)

    return res.json()


def main() -> None:
    print(get_list_of_available_countries())


if __name__ == '__main__':
    main()
