def fact1(n):
    a=1
    for i in range(2,n+1):
        a=a*i
    print(a)
n=int(input("Enter the number :"))
fact1(n)