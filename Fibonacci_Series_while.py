f1=0
f2=1
f3=0
i=0
n=int(input("Enter a number : "))
print("Fibonacci Series in while loop : ")
print(f1,f2,end=" ")
while i<n:
    f3=f1+f2
    f1=f2
    f2=f3
    i+=1
    print(f3,end=" ")
