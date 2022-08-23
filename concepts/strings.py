print('Multiline\nexpression')
print('\ttab')
print('Escape characters: ins\'t')
print('Escape characters: \\')

name = "Levi"
lastname = "Ackerman"
# format function
complete_name = '{0} {1}'.format(name, lastname)
paragraph = '{0} {0} {2} {1}'.format('hello', 'world', 'people')
paragraph2 = '{} {}'.format(2, 3)

city = 'New York'
country = 'United States'
# string literals
location = f'{city}, {country}'
add_result = f'Result: {2+3}'

print("format function: " + complete_name)
print("string literal: " + location)

# string.index(substring, initPosition?, lastPosition?(not included))
# reverse: string.rindex
print(f"'Eren Jaeger'.index('g'): {'Eren Jaeger'.index('g')}")
print(f"'Eren Jaeger'.index('ger'): {'Eren Jaeger'.index('ger')}") # out: 8
# print(f"'Eren Jaeger'.index('g'): {'Eren Jaeger'.index('gor')}")  # out: Error


print(f"'Eren Jaeger'[8]: {'Eren Jaeger'[8]}")  # out: 'g'
# print(f"'Eren Jaeger'[8]: {'Eren Jaeger'[20]}")  # out: Error

# substrings = string[initPosition : lastPosition(not included) : skip]
print("'Eren Jaeger'[3:5] : " + 'Eren Jaeger'[3:6])  # out: 'n J'
print("'Eren Jaeger'[3:5] : " + 'Eren Jaeger'[2:9:2])  # out: 'e ag'
print("'Eren Jaeger'[:4] : " + 'Eren Jaeger'[:4])  # out: 'Eren'
print("'Eren Jaeger'[::2] : " + 'Eren Jaeger'[::2])  # out: 'Ee agr'
# reverse
print("'Eren Jaeger'[::-1] : " + 'Eren Jaeger'[::-1])  # out: 'regeaJ nerE'


upper_case_str = 'Eren Jaeger'.upper()  # out: 'EREN JAEGER'
lower_case_str = 'Eren Jaeger'.lower()  # out; 'eren jaeger'
split_str = 'Eren Jaeger'.split(' ')  # out: [ 'Eren', 'Jaeger' ]
join_str = ','.join(split_str)  # out: 'Eren,Jaeger'
find_str = 'Levi Ackerman'.find("Ac")  # out: 5
find_str_not_found = 'Levi Ackerman'.find("z")  # out: -1
# reverse: string.rfind(substring)
replace_str = 'Salvaje B B'.replace("B", "Bill")  # out: 'Salvaje Bill Bill'

str_length = len("Bill Savage")  # out: 10

multiline_str = '''
    Hello,
    World
'''

multi_value_str = "Hello"*4  # out: HelloHelloHelloHello

print(f"'Hello' in 'Hello world': {'Hello' in 'Hello world'}")  # out: True
print(f"'Hola' in 'Hello world': {'Hola' in 'Hello world'}")  # out: False
print(f"'Hola' not in 'Hello world': {'Hola' not in 'Hello world'}")  # out: True


word = ' Hello '
# string.strip() remove laterals white spaces
print(word.strip())  # out: 'Hello'
# string.lstrip() remove left white spaces
print(word.lstrip())  # out: 'Hello '
# string.rstrip() remove right white spaces
print(word.rstrip())  # out: ' Hello'
