"""
Задача 2024.10.11.03

Теперь мы на вход получаем список строк и список сепараторов и должны вернуть список строк.

Пример.

Получаем сепараторы: .;!?
Входной список: ['Вышел корень', ' из т', 'умана; ', 'Вынул но', 'жик из кармана. ', 'Раз, два, всё?..']
Выход: ['Вышел корень из тумана; ', 'Вынул ножик из кармана. ', 'Раз, два, всё?..']
"""

SEPARATORS = set('.;!?')


def join_similar_segments(segments: list[str], seps: set[str]) -> list[str]:
    if not segments:
        return []

    result: list[str] = ['']
    for segment in segments:
        result[-1] += segment
        if segment.strip()[-1] in seps and segment is not segments[-1]:
            result.append('')

    return result


if __name__ == "__main__":
    texts: list[str] = ['Вышел корень', ' из т', 'умана; ', 'Вынул но', 'жик из кармана. ', 'Раз, два, всё?..']
    joined_segments = join_similar_segments(texts, SEPARATORS)

    sample = ['Вышел корень из тумана; ', 'Вынул ножик из кармана. ', 'Раз, два, всё?..']
    assert joined_segments == sample
