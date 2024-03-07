first_file = open('C:\Users\Admin\Desktop\pp2\lab6\Dir-and-files\checkfor7.txt', "r")
texts = first_file.readlines()
first_file.close()

second_file = open('C:\Users\Admin\Desktop\pp2\lab6\Dir-and-files\checkfor7_1.txt', "w")
for s in texts:
    second_file.write(s)
second_file.close()