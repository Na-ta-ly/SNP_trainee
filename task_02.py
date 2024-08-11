from typing import Optional
from test import assert_function


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


if __name__ == '__main__':
    assert_function(coincidence([1, 2, 3, 4, 5], range(3, 6)),
                    [3, 4, 5],
                    '1')
    assert_function(coincidence(), [], '2')
    assert_function(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)),
                    [1, 2, 2.5],
                    '3')
