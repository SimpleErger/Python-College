f1=0
f2=1
f3=0
n=int(input("Enter a number : "))
print("Fibonacci Series in for loop : ")
print(f1,f2,end=" ")
for i in range (0,n):
    f3=f1+f2
    f1=f2
    f2=f3
    print(f3,end=" ")