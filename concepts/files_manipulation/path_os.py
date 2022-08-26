import os
from pathlib import Path, PureWindowsPath

current_path = os.getcwd()  # out: current path
print(current_path)

# \\ in paths only for windows

# directory = Path('/Users/user/my_directory')  # out: path for all systems
# my_file = directory / 'filename.py'

# os.chdir('C:\\Users\\user\\path')  # change current path
# open('my_file.txt')  # opened in 'C:\\Users\\user\path'

# create directory
# os.makedirs('C:\\Users\\user\\my_new_directory')  create new directory in path entered in param

# file_path = 'C:\\Users\\user\\path\\my_file.py'
# file_name = os.path.basename(file_path)  # out: 'my_file.py'
# file_name = os.path.split(file_path)  # out: tuple('...base-path', 'my_file.py')

# remove directory
# os.rmdir('path')

f_path = Path(os.getcwd() + '/test.txt')
print(f_path.name)  # out: 'test.txt'
print(f_path.suffix)  # out: '.txt'
print(f_path.stem)  # out: 'test'

if f_path.exists():
    print('File exist')
else:
    print('File not exist')

print(PureWindowsPath(f_path))  # out: windows path of f_path

path_1 = Path('dir1', 'dir2', 'dir3')  # out: dir1/dir2/dir3
path_2 = Path('dir1', 'dir2', 'file_1.py')  # out: dir1/dir2/file_1.py
new_path_2 = path_2.with_name('other_file.txt') # out: dir1/dir2/other_file.txt

base_path = Path.home()  # out: user base directory

# path_3 = Path(base_path, 'dir1', 'dir2', 'filecito.py')

print(Path.resolve(Path.cwd() / '../'))  # .../python_course/concepts
print(Path.cwd().parent)  # .../python_course/concepts
print(Path(Path.cwd()).parent)  # .../python_course/concepts
print(Path.cwd().parent.parent)  # .../python_course
print(Path.cwd().parent.parent.parent)  # .../

# print all txt files path into directory
# for file in Path('path').glob('*.txt'):
#    print(file)

# print all txt files path into directory and subdirectories
# for file in Path('path').glob('**/*.txt'):
#    print(file)

# guide_path = Path('Europe', 'Spain', 'Barcelona', 'Bar.py')
# in_europe = guide_path.relative_to(Path('Europe'))  # 'Spain/Barcelona/Bar.py'
# in_spain = guide_path.relative_to(Path('Europe', 'Spain'))  # 'Barcelona/Bar.py'
