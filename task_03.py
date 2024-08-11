from typing import Any
from test import assert_function


def max_odd(array: list[Any]) -> [int | None]:
    max_value = 0
    for item in array:
        if (isinstance(item, (int, float)) and
                item - int(item) == 0.0 and
                int(item) % 2 == 1 and
                int(item) > max_value):
            max_value = int(item)
    return max_value if max_value > 0 else None


if __name__ == '__main__':
    assert_function(max_odd([1, 2, 3, 4, 4]), 3, '1')
    assert_function(max_odd([21.0, 2, 3, 4, 4]), 21, '2')
    assert_function(max_odd(['ololo', 2, 3, 4, [1, 2], None]), 3, '3')
    assert_function(max_odd(['ololo', 'fufufu']), None, '4')
    assert_function(max_odd([2, 2, 4]), None, '5')
