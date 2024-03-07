def file_lengthy(fname):
    i = 0
    with open(fname) as f:
        for line in f:
            i += 1
        return i
print("Number of lines in the file: ",file_lengthy("checkfor4.txt"))