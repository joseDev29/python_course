from typing import Callable


# Decorator
def hello(func: Callable) -> Callable:

    def new_function(*args, **kwargs):
        print('Hello')
        result = func(*args, **kwargs)
        print('Bye')
        return result

    return new_function


@hello
def string_to_uppercase(string: str) -> str:
    return string.upper()


def string_to_lowercase(string: str) -> str:
    return string.lower()


string_to_lowercase_decorated: Callable[[str], str] = hello(string_to_lowercase)


print(string_to_uppercase('my text'))
print(string_to_lowercase('MY TEXT'))
print(string_to_lowercase_decorated('MY TEXT'))
