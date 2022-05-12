''' Python program to print all positive numbers in a range '''

def positiveRange(a,s,e):
    for i in a:
        if i >= 0 and s <= i <= e:
            print(i)

list1 = [1,2,-3]
start, end = -5, 20
positiveRange(list1, start, end)