from tabulate import tabulate
myData=[['a',1],['b',2],['c',3]]
head=["name","roll"]
print(tabulate(myData,headers=head,tablefmt="grid"))