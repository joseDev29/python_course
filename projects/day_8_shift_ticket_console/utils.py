from typing import Callable, Generator


def input_number(label: str) -> int | float | None:
    entered_value = input(label).strip()
    if entered_value.isnumeric():
        return int(entered_value)
    try:
        return float(entered_value)
    except ValueError:
        return None


def get_numbers_generator() -> Generator[int, None, None]:
    curr = 0
    while True:
        curr += 1
        yield curr


def turn_metadata(function: Callable) -> Callable:
    def new_func(*args, **kwargs):
        result = function(*args, *kwargs)
        turn_text = f'\n--- Your turn is ---\n{result}\n--- Wait and you will be attended ---\n'''
        print(turn_text)
        return turn_text
    return new_func


@turn_metadata
def generate_turn(generator: Generator[int, None, None], prefix: str) -> str:
    new_turn = next(generator)
    turn_text = new_turn if new_turn >= 10 else f'0{new_turn}'
    return f'{prefix}-{turn_text}'
