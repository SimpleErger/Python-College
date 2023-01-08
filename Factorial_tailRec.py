def Fact5(n,acc):
    if n==0:
        return acc
    else:
        return Fact5(n-1,acc*n)
n=int(input("Enter a number :"))
print("The factorial of the entered number is : ",Fact5(n,1))