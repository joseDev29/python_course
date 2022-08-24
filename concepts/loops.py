letters = ['a', 'b', 'c']

for letter in letters:
    print(f"{letters.index(letter) + 1}: {letter}\n")

word = 'Hello'

for char in word:
    print(char)

money = 5

while money > 0:
    print("Buy!")
    money -= 1
else:
    print('I am bankrupt')


# pass = is used as a placeholder for future code
# break = finalize loop
# continue = finalize current iteration and continue to next iteration

# range(count)
# range(init, stop(not included))
# range(init, stop(not included), step)

for i in range(5):
    print(f'Hello {i}')

for i in range(0, 5):
    print(f'Hola {i}')

for i in range(0, 5, 2):
    print(f'Hi {i}')

numbers = list(range(1, 101))  # out: [1,...,100]
numbers_2 = [*range(1, 101)]  # out: [1,...,100]

# enumerate( str | list | tuple | set )

for item in enumerate(['a', 'b', 'c']):
    print(item)  # out: tuple(index, value)

for index, value in enumerate(['a', 'b', 'c']):
    pass

numbers_3 = list(enumerate(['a', 'b', 'c']))  # out: [...,tuple(index,value)]
numbers_4 = [*enumerate(['a', 'b', 'c'])]  # out: [...,tuple(index,value)]

# zip(iterable1, iterable2, ...iterables) use the length of the shortest list

names_list = ['Pepe', 'Juan', 'Cami']
lastnames_list = ['Gutierrez', 'Lopez', 'Gonzales']

print([*zip(names_list, lastnames_list)])  # out: [...tuple(iterable_1_value, iterable_2_value, ...iterables_value)]
