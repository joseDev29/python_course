from typing import List
import time
import timeit


def test_for(limit: int) -> List[int]:
    numbers_list = []
    for i in range(1, limit + 1):
        numbers_list.append(i)
    return numbers_list


def test_while(limit: int) -> List[int]:
    numbers_list = []
    counter = 1
    while counter <= limit:
        numbers_list.append(counter)
        counter += 1
    return numbers_list


# time.time() not recommended for very short times

init_test_for = time.time()
test_for(10000)
final_test_for = time.time()
print("time() test_for: ", final_test_for - init_test_for)

init_test_while = time.time()
test_while(10000)
final_test_while = time.time()
print("time() test_while: ", final_test_while - init_test_while)


# timeit.timeit(declaration_code, setup_code, number='repeat declaration count')

test_for_declaration = '''
test_for(5)
'''

test_for_setup = '''
from typing import List
def test_for(limit: int) -> List[int]:
    numbers_list = []
    for i in range(1, limit + 1):
        numbers_list.append(i)
    return numbers_list
'''

test_for_duration = timeit.timeit(test_for_declaration, test_for_setup, number=10000000)

print("timeit() test for: ", test_for_duration)

test_while_declaration = '''
test_while(5)
'''

test_while_setup = '''
from typing import List
def test_while(limit: int) -> List[int]:
    numbers_list = []
    counter = 1
    while counter <= limit:
        numbers_list.append(counter)
        counter += 1
    return numbers_list
'''

test_while_duration = timeit.timeit(test_while_declaration, test_while_setup, number=10000000)

print("timeit() test while: ", test_while_duration)
