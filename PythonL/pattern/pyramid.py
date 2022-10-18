def pyramid(row):
    for i in range(0,row):
        for j in range(0,row-i-1):
            print(end=" ")
        for j in range(0,i+1):
            print("*", end=" ")
        print()
 
def pyramidrev(row):
    for i in range(row,0,-1):
        for j in range(0,row-i):
            print(end=" ")
        for j in range(0,i):
            print("*",end=" ")
        print()


        

num = int(input("Enter the Rows  "))
pyramid(num)
pyramidrev(num)
    