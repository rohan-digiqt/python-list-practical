''' 2.Python program to swap two elements in a list '''

def swap(sList, fp, lp):
    
    fe = sList.pop(fp)
    se = sList.pop(lp-1)

    sList.insert(fp, se)
    sList.insert(lp, fe)

    print(sList)

list1 = [0,1,2,3,4,5]
p1, p2 = 2, 4
swap(list1, p1-1, p2-1)

list2 = ['A','B','C','D','E']
p1, p2 = 3, 5
swap(list2, p1-1, p2-1)