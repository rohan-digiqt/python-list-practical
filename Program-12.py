'''  Python program to find N largest elements from a list '''

def nLarge(list1, num):
    ans_list=[]
    list1.sort()
    list1.reverse()
    for i in range(num):
        ans_list.append(list1[i])
    ans_list.sort()
    print(ans_list)

l1 = [4,3,7,2,1]
nLarge(l1, 2)