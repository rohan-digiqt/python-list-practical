''' Python program to find sum of elements in list '''

def sum(myList):
    sum = 0
    for i in range(0, len(myList)):
        sum += myList[i]
    print(sum)

list1 = [1,2,3]
sum(list1)


# Using sum() method

print(sum(list1))

