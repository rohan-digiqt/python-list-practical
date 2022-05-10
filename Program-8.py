''' Multiply all numbers in the list '''

def mul(myList):
    ans = 1
    for i in range(0, len(myList)):
        ans *= myList[i]
    print(ans)

list1 = [1,2,3,4]
mul(list1)