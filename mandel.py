import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import cm

nx, ny = (1000,1000)
x = np.linspace(-2,1,nx)
y = np.linspace(-1.5,1.5,ny)
X, Y = np.meshgrid(x,y)
cgrid = X + 1j*Y

# For some numbers c doing z^2 + c again and again from 0 will diverge, not for others, plot it to get the mandelbrot set

Z = 0*cgrid
ZC = Z
for i in range(1,50):    
    Z = np.power(Z,2) + cgrid
    ZC[Z>1000] = i

ZC = np.abs(ZC) 

#fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
#surf = ax.plot_surface(X, Y, Z, linewidth=0, antialiased=False, cmap=cm.coolwarm)

mycount = [1]

# Get the mouse click

def onclick(event):
    mycount[0] = mycount[0] + 1
    plt.clf()
    print(event.xdata, event.ydata)

    nx, ny = (500,500)
    scale = 3/(2**mycount[0])
    
    x = np.linspace(event.xdata - scale,event.xdata + scale,nx)
    y = np.linspace(event.ydata - scale,event.ydata + scale,ny)
    X, Y = np.meshgrid(x,y)
    cgrid = X + 1j*Y
    Z = 0*cgrid
    ZC = Z

    for i in range(1,40 + mycount[0]*10):    
        Z = np.power(Z,2) + cgrid
        ZC[Z>1000] = i

    ZC = np.abs(ZC) 

    plt.pcolormesh(X,Y,ZC)
    plt.pause(0.1)
    print(mycount[0])
    
print(ZC)

fig,ax = plt.subplots()
plt.pcolormesh(X,Y,ZC)

fig.canvas.mpl_connect('button_press_event', onclick)
#fig.canvas.mpl_connect('button_press_event', lambda event: onclick(event, mycount))

'''
ax.set_xlim(-4.01, 4.01)
ax.set_ylim(-4.01, 4.01)
'''

plt.show()



'''
value = np.abs(grid)**(-1)
print(value)
value.flatten()
colour = np.stack((value,value,value))
print(colour)

fig = plt.figure()
ax = plt.axes(xlim=(-1,1),ylim=(-1,1))

ax.scatter(xv,yv,c=colour)

'''