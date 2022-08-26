import sys
from os import system

print('Hello')

input('Input name: ')

system('cls' if sys.platform.startswith('win32') else 'clear')

print('World')
