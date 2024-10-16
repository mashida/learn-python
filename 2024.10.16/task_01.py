"""
Задача 2024.10.16.01

Написать функцию для генерации строки из n строчных латинских букв
"""

from random import choices
from string import ascii_lowercase

def generate_random_string(n: int) -> str:
    return ''.join(choices(population=ascii_lowercase, k=n))

if __name__ == '__main__':
    print(generate_random_string(10))