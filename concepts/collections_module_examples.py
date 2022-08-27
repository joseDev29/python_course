from collections import Counter, defaultdict, namedtuple, deque

# Counter

numbers = [8, 9, 6, 6, 4, 9, 9, 3, 3]

# Counter returns a Counter object containing a dictionary where the keys
# are the values of the iterable and the values are the number of times
# each element is repeated in the iterable
counter_result = Counter(numbers)  # out: Counter({ 9: 3, 6: 2, 3: 2, 8: 1, 4: 1 })

print(Counter('Al pan pan y al vino vino'.lower().split()))  # out: Counter({ 'pan': 2, 'vino': 2, 'al': 2, 'y': 1 })

# Sort and return in tuples from the most common element to the least common ( (iterable_item, repeat), ... )
print(counter_result.most_common())  # out: tuple( (9, 3), (6, 2), ... )

# Sort and return the 2 most common elements
print(counter_result.most_common(2))  # out: tuple( (9, 3), (6, 2) )


# defaultdict

my_dic = {1: 'Red', 2: 'Green', 3: 'Blue'}

my_def_dic = defaultdict(lambda: 'empty_val')

print(my_def_dic['one'])  # out: 'empty_val'
print(my_def_dic)  # out: { 'one': 'empty_val' }


# namedtuple

Person = namedtuple('Person', ['name', 'age', 'work'])

eren = Person('Eren', 18, 'Warrior')
print(eren.name)
print(eren.age)

kyllua = Person('Kyllua', 15, 'Hunter')
print(kyllua)
print(kyllua[2])  # out: 'Hunter'


# deque

my_deque = deque(["London", "Barcelona", "Miami"])
my_deque.append("Lima")
my_deque.appendleft("New York")
