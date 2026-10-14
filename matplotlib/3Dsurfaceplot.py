import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
x=np.linspace(-5,5,50)
y=np.linspace(-5,5,50)
X,Y=np.meshgrid(x,y)
Z=X**2+Y**2
ax.plot_surface(X,Y,Z)
ax.set_title("3D Surface Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()