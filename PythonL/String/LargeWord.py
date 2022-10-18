#!/user/bin/python

def smallword(s):
 
    s = sorted(s, key = len,reverse=True)
 
    # Print last word
    print("small wod is ",s[-1])
 
 

def largestWordfromme(s):
    max1 = len(s[0])
    temp = s[0]
    for n in s:
        if(len(n)>max1):
            max1= len(n)
            temp =n


    print("Longest word ",temp, " and length is ",max1)
    # Given string

def smallestWordfromme(s):
    max1 = len(s[0])
    temp = s[0]
    for n in s:
        if(len(n)<max1):
            max1= len(n)
            temp =n
    
    print("smallest word ",temp, " and length is ",max1)


s = "be confident and be yourself"

 
    # Split the string into words
l = list(s.split(" "))
 
smallword(l)
largestWordfromme(l)
smallestWordfromme(l)