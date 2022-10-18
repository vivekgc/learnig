def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end=" ")
        print()
def pattern2(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()
num = int(input("Enter the number boss==   "))
pattern(num)
pattern2(num)