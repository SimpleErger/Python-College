def Fibo1(n):
    if n<=1:
        return 1
    return Fibo1(n-1)+Fibo1(n-2)
n=int(input("Enter the series number : "))
print("The sum of fibonacci series is : ",Fibo1(n))
    