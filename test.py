from typing import Callable, Any, Type


def assert_function(result: Any, true_value: Any, test_name: str) -> None:
    if result != true_value:
        print('test', test_name, 'failed')
    else:
        print('test', test_name, 'passed')


def assert_error(function: Callable,
                 params: tuple,
                 error_class: Type[Exception],
                 test_name: str) -> None:
    try:
        function(*params)
        print('test', test_name, 'failed')
    except error_class:
        print('test', test_name, 'passed')
