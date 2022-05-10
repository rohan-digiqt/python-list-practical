''' Ways to check if element exists in list ''' 

# Using for loop and in 

myList = ['C','C++','Java','Python','JavaScript','Python']

key = 'Python'

for i in myList:
    if i==key:
        print('Exists')

# Using Count

count = myList.count('Python')

if count > 0:
    print('Exists')

# Using any() method
# any() method return true whenever a particular element is present in a given iterator.

ans = any('Python' in sublist for sublist in myList)

print(str(ans))