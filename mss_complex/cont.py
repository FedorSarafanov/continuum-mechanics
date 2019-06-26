import numpy as np
from numpy import sin,cos,pi
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib
import matplotlib.cm as cm

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.25)

# sint=np.linspace(-0.003,0.003,100000);
# P=180/pi*3600
# s = (sin(N*k*d*sint/2)/sin(k*d*sint/2))**2*(sin(k*b*sint/2)/((k*b*sint/2)))**2
# l, = plt.plot(sint*P, s, c='red',linestyle='-',alpha=0.7,lw=1.4)
# plt.yscale('log')
# plt.axis([-500, 500, 10**-3, (N**2)*10])

axcolor = 'lightgoldenrodyellow'
# axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axphi = plt.axes([0.1, 0.15, 0.8, 0.03], facecolor=axcolor)

# sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0, valstep=delta_f)
PHI = Slider(axphi, 'Г', -40, 40, valinit=0,valstep=0.001)
# plt.xlim([-500,500])
# plt.ylim(ymin=10**-3,ymax=(N**2)*1.5)


delta = 0.025
R=2
G=0
size = 4

x = np.arange(-size, size, delta)
y = np.arange(-size, size, delta)
x, y = np.meshgrid(x, y)
X,Y=x,y
Z=y-y*R**2/(x**2+y**2)-G/4/np.pi*np.log(x**2+y**2)


matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
# fig, ax = plt.subplots()
l = ax.contour(X, Y, Z, np.linspace(-20,20,100), colors='black')
circle1 = plt.Circle((0, 0), R, color='black',zorder=10)

ax.set_aspect('equal')
ax.add_artist(circle1)

def update(val):
	G = PHI.val
	# print(G)
	Z=y-y*R**2/(x**2+y**2)-G/4/np.pi*np.log(x**2+y**2)


	matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
	# fig, ax = plt.subplots()
	ax.cla()
	l = ax.contour(X, Y, Z, np.linspace(-20,20,100), colors='black')
	ax.add_artist(circle1)

	fig.canvas.draw_idle()
# sfreq.on_changed(update)
PHI.on_changed(update)


plt.show()