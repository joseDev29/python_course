import os
import shutil
from pathlib import Path
import send2trash

fold_1_path = Path('fold_1')
fold_2_path = Path('fold_2')

if not fold_1_path.exists():
    os.mkdir('fold_1')

if not fold_2_path.exists():
    os.mkdir('fold_2')

sub_fold_path = Path(fold_2_path, 'sub_fold')

if not sub_fold_path.exists():
    Path.mkdir(sub_fold_path)

my_file = open(Path(fold_1_path, 'test.txt'), 'w')
my_file.write('Test text')
my_file.close()

sub_file = open(Path(sub_fold_path, 'sub_test.txt'), 'w')
sub_file.write('Subtext')
sub_file.close()

print(os.listdir())  # out: [ files name in current path ]
# print(os.listdir(Path('path')))  # out: [ files name in param path ]

# move files

shutil.move(Path(fold_1_path, 'test.txt'), fold_2_path)


# os.walk(path) iter all path items

walk_result = os.walk(fold_2_path)

for fold, sub_folds, files in walk_result:
    print(f"Fold: {fold}")
    print(f"Sub folds: {sub_folds}")
    print(f"Files: {files}")

# Delete all items into the path
# shutil.rmtree permanently deletes the contents of the path
# shutil.rmtree(fold_2_path)  # include fold_2
# shutil.rmtree(fold_1_path)  # include fold_1

remove_all = input("All created elements will be deleted (Input 'n' to keep them) : ").strip().lower()

if remove_all == 'n':
    exit()

# send items to the trash
send2trash.send2trash([fold_1_path, fold_2_path])
