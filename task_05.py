from datetime import timedelta, datetime
from test import assert_function


def date_in_future(day_distance: int = 0) -> str:
    str_format = "%d-%m-%Y %H:%M:%S"
    if not isinstance(day_distance, int):
        return datetime.today().strftime(str_format)
    date_delta = timedelta(days=day_distance)
    return (datetime.today() + date_delta).strftime(str_format)


if __name__ == '__main__':
    assert_function(date_in_future([]),
                    datetime.today().strftime("%d-%m-%Y %H:%M:%S"), '1')
    assert_function(date_in_future(2),
                    (datetime.today() +
                     timedelta(days=2)).strftime("%d-%m-%Y %H:%M:%S"),
                    '2')
