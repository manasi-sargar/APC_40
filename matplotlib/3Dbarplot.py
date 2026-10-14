import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
x=[1,2,3,4]
y=[1,1,1,1]
z=[0,0,0,0]
dx=[0.5,0.5,0.5,0.5]
dy=[0.5,0.5,0.5,0.5]
dz=[10,20,30,40]
ax.bar3d(x,y,z,dx,dy,dz)
ax.set_title("3D Bar Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Height")
plt.show()