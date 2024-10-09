def split_text(s: str, separator: str) -> list[str]:
    return s.split(sep=separator)

if __name__ == '__main__':
    test_string = "Вышел корень из тумана. Вынул ножик из кармана. Раз, два, всё."
    print(split_text(test_string, '.'))
