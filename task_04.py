from test import assert_function


def sort_list(test_list: list[int]) -> list[int]:
    if len(test_list) == 0:
        return []

    max_item = max(test_list)
    min_item = min(test_list)
    for index, item in enumerate(test_list):
        if item == max_item:
            test_list[index] = min_item
        elif item == min_item:
            test_list[index] = max_item

    test_list.append(min_item)
    return test_list


if __name__ == '__main__':
    assert_function(sort_list([]), [], '1')
    assert_function(sort_list([2, 4, 6, 8]), [8, 4, 6, 2, 2], '2')
    assert_function(sort_list([1]), [1, 1], '3')
    assert_function(sort_list([1, 2, 1, 3]), [3, 2, 3, 1, 1], '4')
