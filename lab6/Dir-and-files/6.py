# for i in range(65, 65+26):
#     filename = chr(i)+'.txt'
#     with open(chr(i) + ".txt", "w") as file:
#         file.writelines(chr(i))
import os.path
for i in range(65,65+26):
    f = open(os.path.expanduser(os.path.join("C:\Users\Admin\Desktop\pp2\lab6\Dir-and-files\checkfor6",chr(i) + ".txt")), "a")