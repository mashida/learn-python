"""
Задача 2024.10.16.02

Написать функцию для генерации строки из n строчных и заглавных латинских букв
Заглавные должны добавляться в строку только если параметр use_uppercase в функции равен True.
А если параметр use_uppercase не указан при использовании функции, то генерируем строку только из строчных букв.
"""

from random import choices
from string import ascii_lowercase, ascii_uppercase

def generate_random_string(n: int, use_uppercase: bool = False) -> str:
    chars: str = ascii_lowercase
    if use_uppercase:
        chars += ascii_uppercase
    return ''.join(choices(population=chars, k=n))

if __name__ == '__main__':
    print(generate_random_string(10))
    print(generate_random_string(10, use_uppercase=True))