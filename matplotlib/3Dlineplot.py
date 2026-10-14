import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
x=[1,2,3,4,5]
y=[2,4,6,8,10]
z=[1,3,5,7,9]
ax.plot(x,y,z)
ax.set_title("3D Line Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()