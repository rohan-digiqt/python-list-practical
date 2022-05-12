'''  Program to print duplicates from a list of integers '''

def duplicate(a):
    l2=[]
    lnt = len(a)
    for i in range(lnt):
        m = i + 1
        for j in range(m, lnt):
            if a[i] == a[j] and a[i] not in l2:
                l2.append(a[i])
    print(l2)




list1 = [10, 20, 30, 20, 20, 30, 40,50, -20, 60, 60, -20, -20]
duplicate(list1)


# Using Count

l3 = []

for i in list1:
    counter = list1.count(i)
    if counter > 1:
        if l3.count(i)==0:
            l3.append(i)
print(l3)