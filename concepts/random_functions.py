# from random import randint, uniform, ...
import random

# return random int  # last included
random_number = random.randint(1, 50)
print(random_number)

# return random float # last not included
random_float = random.uniform(1, 5)
print(random_float)

random_float = round(random.uniform(1, 5))
print(random_float)

# return float in interval [0, 1)
random_value = random.random()

# random.choice(iterable)
random_item = random.choice(['Red', 'Green', 'Blue'])
random_item2 = random.choice('Hello world')

# random.shuffle(list | str) mixes the elements
numbers_list = [*range(5, 51, 5)]
random.shuffle(numbers_list)
print(numbers_list)
