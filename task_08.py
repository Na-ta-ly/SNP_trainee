from typing import Any, Optional


def multiply_numbers(inputs: Optional[Any] = None) -> [int | None]:
    if not inputs:
        return None

    if isinstance(inputs, (list, set)):
        single_digits = []
        for item in inputs:
            single_digits[len(single_digits):len(single_digits)] = get_digits(item)
    else:
        single_digits = get_digits(inputs)

    if len(single_digits) >= 1:
        result = single_digits[0]
        for item in single_digits[1:]:
            result *= item
        return result
    else:
        return None


def get_digits(value: [int | float | str]) -> list[int]:
    value = str(value)
    result = []
    for item in value:
        if item.isdigit():
            result.append(int(item))
    return result
