''' 1.Python program to interchange first and last elements in a list '''

def exchange(eList):
    fp = eList.pop(0)
    lp = eList.pop(len(eList) - 1)

    eList.insert(0, lp)
    eList.insert(len(eList), fp)

    print(eList)

list1 = [0,1,2,3,4,5]
exchange(list1)

list2 = ['A','B','C','D','E']
exchange(list2)