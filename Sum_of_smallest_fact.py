from math import factorial


n=40321
arr=[]
for i in range (0,10):
    arr.append(factorial(i))
for j in range (0,10):
    for k in range (0,10):
        a=arr[i]+arr[k]
        if (a==n):
            print(a)