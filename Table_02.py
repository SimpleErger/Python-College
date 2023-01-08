from prettytable import PrettyTable, prettytable
myData=PrettyTable(["Name","Roll No."])
myData.add_row(["Ezio Auditore","01"])
myData.add_row(["Alex Mercer","02"])
myData.add_row(["Kratos","03"])
print(myData)