def Pallin(s):
    return s==s[::-1]
str=input("Enter a string :")
s=str.upper()
a=Pallin(s)
if a:
    print("Pallindrome string")
else:
    print("Not a pallindrome string")