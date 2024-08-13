from typing import Optional


def coincidence(test_list: Optional[list] = None,
                test_range: Optional[range] = None) -> list[int]:
    if not test_list or not test_range:
        return []

    assert isinstance(test_range, range), 'test_range should be range type'
    low_border = test_range.start
    high_border = test_range.stop

    result = []
    for item in test_list:
        if (isinstance(item, (int, float))
                and low_border <= item < high_border):
            result.append(item)
    return result
