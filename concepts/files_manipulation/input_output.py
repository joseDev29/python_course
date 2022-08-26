from typing import List

# open(file or path, mode: 'r' | 'w' | 'a' | ... )  r: only read, w: only write, a: only write after last line, ...

mi_file = open('test.txt')

# file_content: str = mi_file.read()  # out: file full content

# print(file_content)

# print(mi_file.readline())  # out: line 2 content
# print(mi_file.readline())  # out: empty str
# print(mi_file.readline())  # out: line 1 content
# print(mi_file.readline())  # out: empty str
# print(mi_file.readline())  # out: empty str

# for line in mi_file:
#    print('Line: ', line)

# all_line: List[str] = mi_file.readlines()

# For performance reasons it is recommended to close the file after use
# mi_file.close()
