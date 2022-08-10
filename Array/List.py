#!/usr/bin/python 
list1 = ['physics','chemistry','maths','biology']
list2 = [1,2,3,4,5,6,7]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
print(list2[1:])
print(list2[:5])
midIndex = len(list2)//2
print(list2[midIndex:])
print(list2[:midIndex])