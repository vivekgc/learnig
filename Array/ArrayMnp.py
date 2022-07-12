from array import *

array1 = array('i',[1,12,13,14,111,17,23,24,25])

print(array1)

array1.insert(1,60)

for x in array1:
    print(x)

array1.remove(14)

print(array1)

array1[2] = 80

print('array after adding ', array1)

