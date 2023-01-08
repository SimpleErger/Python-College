class Animal:
    def __init__(self) -> None:
        print("Running !")
    def walk(self):
        print("Walking !")
    def eat(self):
        print("Eating !")

class Birb(Animal):
    def __init__(self) -> None:
        super().__init__()
    def fly(self):
        print("Udd jaa bsdk")

b=Birb()
b.walk()
b.fly()