"""
Задача 2024.10.11.04

Мы получаем на вход текст, состоящий из предложений. Эти предложения состоят из слов с сепараторами, пробелами и запятыми.

Напишите функцию, которая делит этот текст на случайные сегменты случайной длины.

Например:
Текст: "Что?.. Да! Вышел корень из тумана; Вынул ножик из кармана. Раз, два, всё?.. "
Результат: ['Вышел корень', ' из т', 'умана; ', 'Вынул но', 'жик из кармана. Раз, два, всё?..']
"""
from random import randint


def text_random_split(input_string: str) -> list[str]:
    result: list[str] = []
    left = 0
    right = 1

    while right > left != len(input_string):
        right = randint(left + 1, len(input_string))
        result.append(input_string[left: right])
        left = right
        right += 1

    return result


if __name__ == "__main__":
    text: str = "Что?.. Да! Вышел корень из тумана; Вынул ножик из кармана. Раз, два, всё?.. "
    split_texts = text_random_split(text)
    print(text)
    print(split_texts)

    assert len(split_texts) > 1
