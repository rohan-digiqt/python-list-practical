''' Python program to print even numbers in a list '''

def odd(list1):
    ans_list=[]
    for i in range(len(list1)):
        if list1[i] %2 != 0:
            ans_list.append(list1[i])
    print(ans_list)

l1 = [4,3,7,2,1]
odd(l1)