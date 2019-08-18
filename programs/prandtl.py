from numpy import array
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def model(t,Z):
	x=Z[0]
	y=Z[1]
	z=Z[2]
	return [z,x,-1/2*y*z]

z0 = array([0,0,0.332])

solve = solve_ivp(model,[0, 6],z0,method='LSODA',min_step=0.00001,max_step=0.01)

t=solve.t
z=solve.y

y=z[1]
dy=z[0]
ddy=z[2]


plt.plot(t,y)
plt.show()
plt.plot(t,dy)
plt.show()
plt.plot(t,ddy)
plt.show()

import numpy as np
A=np.array([t,y,dy,ddy]).T
np.savetxt('../img/data/prandtl.tsv', A, delimiter='\t', header='t\ty\tdy\tddy',comments='')