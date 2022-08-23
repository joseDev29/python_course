my_true = True
my_false = False

condition = 5 in [1, 2, 3]  # out: False
condition_2 = 'a' not in ['b', 'c', 'd']  # out: True
condition_3 = 'Is par' if 23 % 7 == 0 else 'Is impar'
condition_4 = True or 'second option' or 'third option'
condition_5 = 'If' if ('Sub if' if False else 'Sub else') else 'Else'
condition_6 = 2 * 4 if 24 % 3 == 0 else 4 * 5

print(bool())  # out: False
print(bool(2))  # out: True
print(bool(-1))  # out: True
print(bool(0))  # out: False
print(bool(' '))  # out: True
print(bool(''))  # out: False
print(bool([]))  # out: False
print(bool([0]))  # out: True
print(bool({}))  # out: False
print(bool({'name': 'Jake'}))  # out: True

