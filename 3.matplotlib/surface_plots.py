from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
# MORE COMPLEX SHAPES

a = np.arange(-1, 1, 0.02)
b = a

a, b = np.meshgrid(a, b)
fig = plt.figure()
axes = fig.gca(projection='3d')
# experiment with z to get some great plots
axes.plot_surface(a, b, a**2 + b**2, cmap='rainbow')
plt.show()

fig = plt.figure()
axes = fig.gca(projection='3d')

# experiment with z to get some great plots
axes.contour(a, b, a**2+b**2, cmap='rainbow')
plt.show()
