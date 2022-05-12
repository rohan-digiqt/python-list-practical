''' Python program to print positive numbers in a list '''

def positive(a):
    for i in a:
        if i >= 0:
            print(i)

list1 = [1,2,-3]
positive(list1)