''' Different ways to clear a list in Python '''


# Using clear() method
myList = ['C','C++','Java','Python','JavaScript','Python']
myList.clear()
print(myList)

# Using Reinitializing the list 

list2 = [1,2,3]
print(list2)
list2 = []
print(list2)

# Using “*= 0”

list3 = ['a','b']
print(list3)
list3 *= 0
print(list3)

# Using del : del can be used to clear the list elements in a range, if we don’t give a range, all the elements are deleted.

list4 = ['R','O']
print(list4)
del list4[:]
print(list4)