from typing import Any


def max_odd(array: list[Any]) -> [int | None]:
    max_value = 0
    for item in array:
        if (isinstance(item, (int, float)) and
                item - int(item) == 0.0 and
                int(item) % 2 == 1 and
                int(item) > max_value):
            max_value = int(item)
    return max_value if max_value > 0 else None
