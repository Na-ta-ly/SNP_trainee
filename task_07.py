def combine_anagrams(words_array: list[str]) -> list[list[str]]:
    words_array = [str(word).lower() for word in words_array]
    result = []
    while len(words_array) > 1:
        single_result = [words_array[0]]
        for word in words_array[1:]:
            if len(word) == len(words_array[0]):
                pivot_word = words_array[0]
                check = True
                for letter in word:
                    if letter in pivot_word:
                        pivot_word = pivot_word.replace(letter, '', 1)
                    else:
                        check = False
                        break
                if check:
                    single_result.append(word)
                    words_array.remove(word)
        result.append(single_result)
        words_array = words_array[1:]
    return result
