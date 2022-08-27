from pathlib import Path
import zipfile
import shutil

# with zipfile

# zipfile.is_zipfile(Path('path'))

my_zip = zipfile.ZipFile('my_zip.zip', 'w')

my_zip.write('my_text_1.txt')
my_zip.write('my_text_2.txt')

my_zip.close()

Path('my_text_1.txt').unlink()
Path('my_text_2.txt').unlink()

# opened_zip = zipfile.ZipFile('my_zip.zip', 'r')
opened_zip = zipfile.ZipFile('my_zip.zip')
opened_zip.extractall()
opened_zip.close()
# opened_zip.extract('my_text_1.txt')
# opened_zip.extract('my_text_2.txt')


# with shutil

shutil.make_archive('with_shutil/shutil_zip', 'zip', Path(Path.cwd(), 'with_shutil'))

Path(Path.cwd(), 'with_shutil', 'text_1.txt').unlink()
Path(Path.cwd(), 'with_shutil', 'text_2.txt').unlink()

shutil.unpack_archive(Path(Path.cwd(), 'with_shutil', 'shutil_zip.zip'), 'with_shutil', 'zip')
