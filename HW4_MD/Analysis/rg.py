import numpy as np
from matplotlib import pyplot as plt

sed = np.loadtxt('rg_10A.dat',unpack = True,usecols=1,skiprows=1)
x = np.arange(start=0, stop=500/5, step=.2)
y = sed

plt.title("Rg of DNA in Explicit Solvent")
plt.xlabel("Time (ns)")
plt.ylabel("Rg (Angstoms)")
plt.plot(x,y,color='darkolivegreen')
plt.show()

