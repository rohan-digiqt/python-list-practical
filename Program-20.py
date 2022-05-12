''' Python program to print all negative numbers in a range '''

def negativeRange(a,s,e):
    for i in a:
        if i < 0 and s <= i <= e:
            print(i)

list1 = [1,2,-3]
start, end = -5, 20
negativeRange(list1, start, end)