import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
x=[1,2,3,4,5]
y=[2,4,6,8,10]
z=[5,4,3,2,1]
ax.scatter(x,y,z,c='red',marker='o')
ax.set_title("Colored 3D Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()