''' Remove empty List from List '''

list1 = [[1,2,3],['a','b','c'],[],['ROHAN'],'String',44]

for i in list1:
    if len(str(i))==0:
        list1.remove(i)
print(list1)

# print(len(str(12)))