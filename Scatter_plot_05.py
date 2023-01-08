from turtle import color
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x=[4,8,12]
y=[19,11,7]
x2=[7,10,12]
y2=[8,18,24]
plt.scatter(x,y)
plt.scatter(x2,y2,color='g')
plt.title('Epic info')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()