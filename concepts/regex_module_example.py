import re

# Special characters

# /d : numeric digit  => example: v\d.\d\d  match with 'v1.01' | 'v3.23' | 'v0.41'
# /w : alphanumeric character  => example: \w\w\w-\w\w  match with  'sol-do' | 'abc-25' | 'Nro-al'
# /s : blank space   => example:  number\s\d\d = number\s\d{2}  match with  'number 20' | 'number 59' | 'number 34'
# /D : not numeric digit
# /W : not alphanumeric digit  => example:  \W\W\W = \W{3}  match with  '+=-' | '???' | '#>!'
# /S : not blank space  => example:  \S\S\S = \S{3}  match with  '123' | 'abc' | 'v.2'


# Quantifiers

# + : one or more
# * : zero o more
# ? : zero or one
# {n} : n=number of repeats
# {n, m} : range [n, m]
# {n,} : range [n, infinite)


# Others

# | : or
# ^ : init string
# $ : end string
# [pattern] : exclude pattern
# [pattern]+

text = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'

search_result = re.search('ayuda', text)

print(search_result)  # out: <re.Match object; span=(13, 18), match='ayuda'>
print(search_result.span())  # out: (13, 18)  location string index tuple(init, end)
print(search_result.start())  # out: 13  location string init index
print(search_result.end())  # out: 18  location string end index
print(re.search('hello', text))  # out: None

print(re.findall('ayuda', text))  # out: ['ayuda', 'ayuda']

print(re.finditer('ayuda', text))  # out: [ re.Match(), ... ]

for matched in re.finditer('ayuda', text):
    print(matched.span())

# phone_pattern = r'\(\d{3}\)-\d{3}-\d{4}'
phone_pattern = re.compile(r'(\(\d{3}\))-(\d{3})-(\d{4})')

print(re.findall(phone_pattern, text))

for matched in re.finditer(phone_pattern, text):
    print(matched.span())

# only for re.compile()
print(re.search(phone_pattern, text).group(0))

print(re.fullmatch(phone_pattern, '(314)-234-5567'))  # out: re.Match
print(re.fullmatch(phone_pattern, '(314)-234-5567 '))  # out: None
print(re.fullmatch(phone_pattern, ' (314)-234-5567'))  # out: None
