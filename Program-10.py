''' Python program to find largest number in a list '''

def largest(myList):
    myList.sort()
    print(myList[len(myList) - 1])

l1 = [4,3,7,2,1]
largest(l1)