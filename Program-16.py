''' Python program to print all odd numbers in a range '''

def oddRange(list1,start,end):
    ans_list=[]
    for i in range(len(list1)):
        if list1[i] %2 != 0 and start <= list1[i] <= end:
            ans_list.append(list1[i])
    print(ans_list)

l1 = [4,3,7,2,1]
start, end = 1 , 3
oddRange(l1, start, end)