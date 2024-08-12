from datetime import timedelta, datetime


def date_in_future(day_distance: int = 0) -> str:
    str_format = "%d-%m-%Y %H:%M:%S"
    if not isinstance(day_distance, int):
        return datetime.today().strftime(str_format)
    date_delta = timedelta(days=day_distance)
    return (datetime.today() + date_delta).strftime(str_format)
