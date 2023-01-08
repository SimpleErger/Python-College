from matplotlib import pyplot as plt
percentage=[12,86,79,96,46,88,78,47,32,33,56,96]
no_stds=[0,10,20,30,40,50]
plt.hist(percentage,no_stds,histtype='bar',rwidth=0.5)
plt.xlabel("Percentage")
plt.ylabel("Number of students")
plt.title("Histogram Chart")
plt.show()