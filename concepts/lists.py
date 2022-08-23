my_list = ["Bill", "Maria", "Jack"]

print(my_list[0:1])  # out: ['Bill']
print(my_list[::2])  # out: ['Bill', 'Jack']

added_lists = my_list + ["Willy", "Bob", "Diane"]  # out: ['Bill', 'Maria', 'Jack', 'Willy', 'Bob', 'Diane']

# list.sort modify current list
my_list.sort(key=lambda word: word[0])
print(my_list)  # out: [ 'Bill', 'Jack , 'Maria']

# sorted return new list
print(sorted(my_list, key=lambda word: word[0]))  # out: [ 'Bill', 'Jack , 'Maria']

# delete last item
added_lists.pop()

# delete item in index location
added_lists.pop(2)

chars_list = ["A", "B", "C"]

# reverse current list
chars_list.reverse()

# return new reversed list
new_reversed_list = list(reversed(chars_list))

numbers = [1, 2, 3]
new_numbers = [element * 2 for element in numbers]  # out: [2, 4, 6]
new_numbers2 = [element * 2 if element % 2 == 0 else element * 3 for element in numbers]  # out: [3, 4, 9]

print(numbers)
print(new_numbers)
print(new_numbers2)

