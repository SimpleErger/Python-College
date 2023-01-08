from turtle import color
from matplotlib import pyplot as plt
names=["Arun","James","Ricky","Robin"]
marks=[45,77,89,35]
plt.bar(names,marks,color='red')
plt.title("Result")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()