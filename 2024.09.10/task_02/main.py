def split_text_by_separators(text: str, seps: list[str]) -> list[str]:
    result: list[str] = ['']
    waiting_for_separator: bool = True

    for symbol in text:
        if waiting_for_separator:
            if symbol in seps:
                waiting_for_separator = False
        else:
            if not symbol in seps and symbol != ' ':
                result.append('')
                waiting_for_separator = True

        result[-1] += symbol

    return result

if __name__ == "__main__":
    separators: list[str] = [';', '.', '!', '?']
    test_string = "Что?.. Да! Вышел корень из тумана; Вынул ножик из кармана. Раз, два, всё?.."
    print(split_text_by_separators(test_string, separators))