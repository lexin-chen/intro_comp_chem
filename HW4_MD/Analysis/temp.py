import numpy as np
from matplotlib import pyplot as plt

y = np.loadtxt('temp.dat',unpack = True,usecols=0,skiprows=0)
#y1 = np.loadtxt('temp.dat',unpack = True,usecols=1,skiprows=0) 
#y2 = np.loadtxt('temp.dat',unpack = True,usecols=2,skiprows=0)
x = np.arange(start=0, stop=500/5, step=.2)


plt.title("Total Temp of DNA in Explicit Solvent")
plt.xlabel("Time (ns)")
plt.ylabel("Temp (K)")
plt.plot(x,y,color='black',label='Total Temp')
#plt.plot(x,y1,color='blue',label='Kinetic Temp')
#plt.plot(x,y2,color='red',label='Potential Temp')
#plt.legend()
plt.show()

