def divisible_3_4(m):
    for i in range(m+1):
        if i % 3 == 0 or i % 4 == 0:
            yield i
m = int(input())
numbers = divisible_3_4(m)
for num in numbers:
    print(num)
