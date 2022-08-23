# sets are not include lists or dictionaries
# all set values are unique

# my_set = set([1, 2, 3, 4, 5, 6])
# my_set = set((1, 2, 3, 4, 5, 6))
my_set = {1, 2, 3, 4, 5, 6}

print(2 in my_set)  # out: True

my_set2 = {7, 8, 9}

union_set = my_set.union(my_set2)

print(my_set)  # out: {1, 2, 3, 4, 5, 6}
print(my_set2)  # out: { 7, 8, 9}
print(union_set)  # out: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# union_set.remove(10)  # out: Error
union_set.discard(10)

# delete random item from set
union_set.pop()

union_set.add(2)  # not added
union_set.add(10)  # added
union_set.clear()  # out: { }

numbers = {1, 2, 3}
new_numbers = {element * 2 for element in numbers}  # out: {2, 4, 6}
new_numbers2 = {element * 2 if element % 2 == 0 else element * 3 for element in numbers}  # out: [3, 4, 9]

print(numbers)
print(new_numbers)
print(new_numbers2)
