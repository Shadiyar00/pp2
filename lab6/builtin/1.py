def multiplyList(mylist):
    result = 1
    for x in mylist:
        result *= x
    return result
input_list = input()
list1 = list(map(int, input_list.split()))
list_list = multiplyList(list1)
print(list_list)