from test import assert_function


def connect_dicts(dict1: dict, dict2: dict) -> dict:
    result = dict()
    major_dict, minor_dict = (dict1, dict2) if sum(dict1.values()) > sum(dict2.values()) else (dict2, dict1)

    for item in major_dict.items():
        if item[1] >= 10:
            result[item[0]] = item[1]
    for item in minor_dict.items():
        if item[1] >= 10 and not result.get(item[0], None):
            result[item[0]] = item[1]

    result = dict(sorted(result.items(), key=lambda item: item[1]))
    return result


if __name__ == '__main__':
    assert_function(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}),
                    {"c": 11, "b": 12},
                    '1')
    assert_function(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}),
                    {"d": 11, "c": 12, "a": 13},
                    '2')
    assert_function(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}),
                    {"c": 11, "b": 12, "a": 15},
                    '3')
