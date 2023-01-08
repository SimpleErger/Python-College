m=6
n=6

a=[1,2,3,4,7,9]
b=[0,1,2,1,1,4]
tempArr=[]
for i in range(m):
    rand=0
    for j in range(n):
        if b[j]<=a[i]:
            rand+=1
    tempArr.append(rand) 
print(tempArr)
