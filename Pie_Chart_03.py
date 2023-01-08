from matplotlib import pyplot as plt
sweets="Ladoo","Barfi","Rasmalai","Kheer"
popularity=[42,22,10,26]
explode=(0.3,0.1,0.1,0.1)
fig1,ax1=plt.subplots()
ax1.pie(popularity,explode=explode,labels=sweets,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.show()