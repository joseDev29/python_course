from typing import Tuple, Dict, List, Set, Any

my_number: int = 23
my_number_2: int | float = 23.45


def add(num_1: int | float, num_2: int | float) -> int | float:
    return num_1 + num_2


def my_print(value: str) -> None:
    print(value)


my_numbers_list: List[int] = [23, 45, 56]
my_tuple: Tuple[str, str, str] = ('A', 'B', 'C')
my_dict: Dict[str, bool] = {'xs': True, 'sm': True, 'md': False, 'lg': False}
my_set: Set[int] = {34, 55, 67}

MyType = Tuple[str, str]
my_cards_list: list[MyType] = [('A', 'B'), ('C', 'D')]

my_any_var: Any = 'Hello'
print(my_any_var)
my_any_var = 23
print(my_any_var)
my_any_var = True
