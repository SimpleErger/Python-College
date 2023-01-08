#WAP to find the greatest number among the 3 using if else :
a,b,c=map(int,input("Enter the numbers : ").split())
print("The first number is {} , second number is {} and the third number is {}.".format(a,b,c))
if(a>b and a>c):
    print("The gretest number is : ",a)
elif(b>a and b>c):
    print("The gretest number is : ",b)
else:
    print("The gretest number is : ",c)