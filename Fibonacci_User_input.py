f1=int(input("Enter the first number for fibonacci series : "))
f2=int(input("Enter the second number for fibonacci series : "))
f3=0
n=int(input("Enter the running series : "))
print("Fibonacci Series in for loop : ")
print(f1,f2,end=" ")
for i in range (0,n):
    f3=f1+f2
    f1=f2
    f2=f3
    print(f3,end=" ")