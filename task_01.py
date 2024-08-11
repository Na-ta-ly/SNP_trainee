from test import assert_function


def is_palindrome(test_string: [str | int | float | None]) -> bool:
    test_string = str(test_string)
    test_string = test_string.lower()

    test_list = []
    for item in test_string:
        if item.isalpha() or item.isdigit():
            test_list.append(item)

    for index in range(len(test_list) // 2):
        if test_list[index] != test_list[len(test_list) - index - 1]:
            return False
    return True


if __name__ == '__main__':
    assert_function(is_palindrome("A man, a plan, a canal -- Panama"),
                    True,
                    '1')
    assert_function(is_palindrome("Madam, I'm Adam!"), True, '2')
    assert_function(is_palindrome(333), True, '3')
    assert_function(is_palindrome(None), False, '4')
    assert_function(is_palindrome("Abracadabra"), False, '5')
