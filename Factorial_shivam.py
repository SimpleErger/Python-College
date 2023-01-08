def Fact4(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        if (i<n) :
            print("{} X".format(i),end=" ")
        elif (i==n):
            print(i,end=" ")
    print(" = ",f)
n=int(input("Enter the number : "))
Fact4(n)