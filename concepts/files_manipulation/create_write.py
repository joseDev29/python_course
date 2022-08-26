# if the file does not exist open(path, 'w') creates it

created_file = open('test_1.txt', 'w')
created_file.write('Hello\n')
created_file.write('world\n')

created_file.writelines(['Hello', 'world'])

created_file.close()


file_for_update = open('test_1.txt', 'a')

file_for_update.write('\nUpdate 1\n')

file_for_update.close()
