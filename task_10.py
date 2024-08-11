from test import assert_function


def count_words(string: str) -> dict:
    string = string.lower()
    for sep in [',', '.', '-', '!', '?', ':', ';']:
        string = string.replace(sep, '')
    words = string.split(sep=' ')

    result = dict()
    for word in words:
        if len(word) > 0:
            if result.get(word, None):
                result[word] += 1
            else:
                result[word] = 1
    return result


if __name__ == '__main__':
    assert_function(count_words("A man, a plan, a canal -- Panama"),
                    {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1},
                    '1')
    assert_function(count_words("Doo bee doo bee doo"),
                    {"doo": 3, "bee": 2},
                    '2')
