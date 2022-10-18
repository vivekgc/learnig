list1 = [5,1,12,4,14,3,0]
print(list1)
for i in range(len(list1)):
    min_value= min(list1[i:])
    print(min_value)
    min_index= list1.index(min_value)
    print(min_index)
    list1[i],list1[min_index]=list1[min_index],list1[i]

print(list1)