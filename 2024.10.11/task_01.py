"""
Задача 2024.10.11.02

Теперь мы на вход получаем список строк и список сепараторов и должны вернуть список строк.

Пример.

Получаем сепараторы: .;!?
Входной список: 'Дем', 'онстра', 'ция!'
Выход: 'Демонстрация!'
"""

SEPARATORS = set('.;!?')


def join_similar_segments(segments: list[str], seps: set[str]) -> list[str]:
    if not segments:
        return []

    result: list[str] = ['']
    for segment in segments:
        result[-1] += segment
        if segment[-1] in seps and segment is not segments[-1]:
            result.append('')

    return result


if __name__ == "__main__":
    texts: list[str] = ['Дем', 'онстра', 'ция!', 'Баба ', 'Яга?']
    joined_segments = join_similar_segments(texts, SEPARATORS)

    sample = ['Демонстрация!']
    assert joined_segments == sample
