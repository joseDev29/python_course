from functools import reduce
from typing import Tuple, Callable, TypeVar, Sequence, List


def hello():
    print("Hello!")


Number = int | float


def add(num1: Number, num2: Number) -> Number:
    return num1 + num2


result = add(23, 45)

multiply: Callable[[int, int], int] = lambda a, b: a * b

result_2 = multiply(2, 4)


def func() -> Tuple[str, str, str]:
    return 'A', 'B', 'C'


a, b, c = func()
print(a, b, c)

result_3 = func()
print(result_3)  # out: tuple('A', 'B', 'C')

T = TypeVar('T')


def some(iterator: Callable[[T], bool], iterable: Sequence[T]) -> bool:
    return any(iterator(item) for item in iterable)


print(some(lambda n: n % 2 == 0, [1, 25, 3]))


def every(iterator: Callable[[T], bool], iterable: Sequence[T]):
    return all(iterator(item) for item in iterable)


print(every(lambda n: n % 2 == 0, [2, 4, 6]))


# *args

def dynamic_add(*args):
    return reduce(lambda acc, curr: acc + curr, args, 0)


print(dynamic_add(1, 2, 3))  # out: 6
print(dynamic_add(*[1, 2, 3]))  # out: 6
print(dynamic_add(*(1, 2, 3)))  # out: 6


def dynamic_func(param1, *args):
    print(param1)
    print(args)


# **kwargs

def kwargs_printer(**kwargs):
    print(f"kwargs: {kwargs}")
    for key, value in kwargs.items():
        print(f"key={key}, value={value}")


kwargs_printer(x=3, y=2, z=1)
kwargs_printer(**{'x': 3, 'y': 2, 'z': 1})


# mix args types

# There can be no positional parameters after a keyword argument

def dynamic_printer(param1, param2, *args, **kwargs):
    print(f'Param 1: {param1}')
    print(f'Param 2: {param2}')
    print(f'*args: {args}')
    print(f'kwargs: {kwargs}')


dynamic_printer(23, 34, 54, 54, 65, *[1, 2, 3], 2, 3, **{'x': 2, 'y': 3}, z=4, h=5)


# is_prime_number: Callable[[int], bool] = lambda n: all(n % i != 0 for i in range(2, n))
is_prime_number: Callable[[int], bool] = lambda n: not any(n % i == 0 for i in range(2, n))


print(f"5 is prime: {is_prime_number(5)}")
print(f"6 is prime: {is_prime_number(6)}")
print(f"7 is prime: {is_prime_number(7)}")
print(f"11 is prime: {is_prime_number(11)}")
print(f"24 is prime: {is_prime_number(24)}")


# list_of_prime_numbers: Callable[[int], List[int]] = lambda n: [i for i in range(2, n + 1) if is_prime_number(i)]
def list_of_prime_numbers(n: int) -> List[int]:
    return [i for i in range(2, n + 1) if is_prime_number(i)]


print(list_of_prime_numbers(13))
print(list_of_prime_numbers(20))
