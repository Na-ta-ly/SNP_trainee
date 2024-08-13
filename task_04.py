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
