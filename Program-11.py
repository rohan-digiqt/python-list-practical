''' Python program to find second largest number in a list '''

def secLargest(myList):
    myList.sort()
    print(myList[len(myList) - 2])

l1 = [4,3,7,2,1]
secLargest(l1)