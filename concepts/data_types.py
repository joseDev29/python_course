my_string = "Hello world"

my_int = 23

my_float = 23.45

my_boolean = True

my_list = ['Eren', 'Armin', 'Mikasa']

# The order of tuples can't modify
my_tuple = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

my_dictionary = {'name': 'Eren', 'lastname': 'Jaeger'}

# Each data in a set is unique
my_set = {'Batman', 'Superman', 'Wonder Woman'}


parsed_int_to_string = str(my_int)
parsed_float_to_int = int(my_float)

print(type(my_string))
print(type(my_int))
print(type(my_float))
print(type(my_boolean))
print(type(my_list))
print(type(my_tuple))
print(type(my_dictionary))
print(type(my_set))

print(isinstance(my_string, str))
print(isinstance(my_int, int))
print(isinstance(my_float, float))
print(isinstance(my_boolean, bool))
print(isinstance(my_list, list))
print(isinstance(my_tuple, tuple))
print(isinstance(my_dictionary, dict))
print(isinstance(my_set, set))

