import os

file = 'C:\Users\Admin\Desktop\pp2\lab6\Dir-and-files\checkfor8'
if os.access(file, os.F_OK)==True:
    os.remove(file)
else:
    print('Такого файла нет')