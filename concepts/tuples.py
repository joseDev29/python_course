# tuples are not alterable

roles_tuple = ('standard', 'admin', 'superAdmin')

print(roles_tuple[0])

standard, admin, superAdmin = roles_tuple


def iterator(item):
    print(item)
    return item


roles_list = map(iterator, roles_tuple)

print(list(roles_list))

print(len(roles_tuple))  # out: 3

print(roles_tuple.count('standard'))  # out: 1

print(roles_tuple.index('superAdmin'))  # out: 2

numbers = (1, 2, 3)
new_numbers = tuple(element * 2 for element in numbers)  # out: (2, 4, 6)
new_numbers2 = tuple(element * 2 if element % 2 == 0 else element * 3 for element in numbers)  # out: (3, 4, 9)

print(numbers)
print(new_numbers)
print(new_numbers2)
