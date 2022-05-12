''' Cloning or Copying a list '''

'''
 This method is considered when we want to modify a list and also keep a copy of the original. In this we make a copy of the list itself, along with the reference. This process is also called cloning.

'''

def cloning(list1):
    list2 = list1 # list(list1)
    print(list2)

list1 = [1,2,3]
print(list1)
cloning(list1)