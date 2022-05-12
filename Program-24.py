''' Count occurrences of an element in a list '''

a = [1,2,3,4,5,6,7,8]
count = 0

for i in a:
    count += 1
print('Total occurrence = ',count)

# Count particular emelent

b =[1,2,4,5,4,2,3,7,8,7,4]

count = 0

for i in b:
    if i==4:
        count += 1
print(count)


# Using count()

count = 0

print(b.count(4))