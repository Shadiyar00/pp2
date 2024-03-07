s = input()
count_lower = 0
count_upper = 0
for i in s:
    if i.islower():
        count_lower += 1
    else:
        count_upper += 1
print(count_lower)
print(count_upper)