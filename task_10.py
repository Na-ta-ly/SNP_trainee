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
