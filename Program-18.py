''' Python program to print negative numbers in a list '''

def negative(a):
    for i in a:
        if i < 0:
            print(i)

list1 = [1,2,-3]
negative(list1)