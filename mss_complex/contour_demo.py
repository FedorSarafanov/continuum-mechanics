
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

delta = 0.025
R=2
G=50
size = 4

x = np.arange(-size, size, delta)
y = np.arange(-size, size, delta)
x, y = np.meshgrid(x, y)
X,Y=x,y
Z=y-y*R**2/(x**2+y**2)-G/4/np.pi*np.log(x**2+y**2)


matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, np.linspace(-20,20,100), colors='black')
circle1 = plt.Circle((0, 0), R, color='black',zorder=10)

ax.set_aspect('equal')
ax.add_artist(circle1)

ax.set_title('G='+str(G))
plt.show()

