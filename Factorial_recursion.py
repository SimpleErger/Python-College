def fact3(n):
    if n==0 or n==1:
        return 1
    else :
        return n*fact3(n-1)
n=int(input("Enter :"))
print(fact3(n))
