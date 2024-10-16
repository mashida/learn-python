"""
Задача 2024.10.16.04

Добавьте в генератор опцию, которая будет контролировать разрешены ли в строке повторяющиеся символы.
И если не разрешены, то нельзя допускать повторяющихся символов в строке.
"""

from random import choices, sample
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def generate_random_string(n: int, use_uppercase: bool = False, use_digits: bool = False,
                           use_punctuation: bool = False, use_unique: bool = False) -> str:
    chars: str = ascii_lowercase
    if use_uppercase:
        chars += ascii_uppercase

    if use_digits:
        chars += digits

    if use_punctuation:
        chars += punctuation

    if use_unique:
        return ''.join(sample(population=chars, k=n))

    return ''.join(choices(population=chars, k=n))


if __name__ == '__main__':
    print(generate_random_string(10))
    print(generate_random_string(10, use_uppercase=True))
    print(generate_random_string(10, use_uppercase=True, use_digits=True))
    print(generate_random_string(10, use_uppercase=True, use_punctuation=True))
    print(generate_random_string(10, use_uppercase=True, use_punctuation=True, use_unique=True))
