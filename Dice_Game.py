import random
temp=0
check = "yes"
while check=="yes":
    num=random.randint(1,6)
    if num==1:
        prevC=1
        print(" ---------")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print(" ---------")
    if num==2:
        prevC=2
        print(" ---------")
        print("| 0       |")
        print("|         |")
        print("|       0 |")
        print(" ---------")
    if num==3:
        prevC=3
        print(" ---------")
        print("| 0       |")
        print("|    0    |")
        print("|       0 |")
        print(" ---------")
    if num==4:
        prevC=4
        print(" ---------")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print(" ---------")
    if num==5:
        prevC=5
        print(" ---------")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print(" ---------")
    if num==6:
        prevC=6
        print(" ---------")
        print("| 0     0 |")
        print("| 0     0 |")
        print("| 0     0 |")
        print(" ---------")
        temp+=1
    check = input("Enter yes or no for rolling dice again ! ")
    print("\n")