# Write a Python program to write a list to a file.

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

with open('checkfor5.txt', "w") as myfile:
        for c in color:
                myfile.write(c)
                myfile.write('\n')

content = open('checkfor5.txt')
print(content.read())