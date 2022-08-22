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
