def Fibo5(n,a=0,b=1):
    if n==0:
        return a
    if n==1:
        return b
    return Fibo5(n-1,b,a+b)
n=int(input("Enter a value till fibonacci series will run :"))
print("Fib("+str(n)+")="+str(Fibo5(n)))