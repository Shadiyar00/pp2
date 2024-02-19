def square_sequence(a, b):
    start = a
    stop = b
    while start <= stop:
        yield start ** 2
        start += 1

a = int(input())
b = int(input())
square = square_sequence(a,b)
for num in square:
    print(num)