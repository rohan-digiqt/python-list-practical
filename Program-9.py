''' Python program to find smallest number in a list '''

def smallest(myList):
    myList.sort()
    print(myList[0])

l1 = [4,8,3,4,9]
smallest(l1)