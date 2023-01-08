def sumone(n):
    r = n+1
    result=0
    for i in range(1,r):
        result+=1
    return result
r = int(input("Enter the range :"))
print("Sum = ",sumone(r))