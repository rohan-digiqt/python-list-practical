''' Python program to print all even numbers in a range '''

''' Python program to print even numbers in a list '''

def evenRange(list1,start,end):
    ans_list=[]
    for i in range(len(list1)):
        if list1[i] %2 == 0 and start <= list1[i] <= end:
            ans_list.append(list1[i])
    print(ans_list)

l1 = [4,3,7,2,1]
start, end = 1 , 8
evenRange(l1, start, end)