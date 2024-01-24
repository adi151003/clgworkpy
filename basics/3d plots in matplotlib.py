import numpy as np
import matplotlib.pyplot as plt
 
 
fig = plt.figure()
ax = plt.axes(projection ='3d')

z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
 
# plotting
ax.plot3d(x, y, z, 'green')
ax.scatter(x, y, z,'green')
ax.set_title('3D line plot by Aditya')
plt.show()