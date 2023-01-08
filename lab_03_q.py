from operator import mod


year=int(input("Enter the year : "))
if year%4==0 :
    print("Leap Year")
else :
    print("Not a leap year")