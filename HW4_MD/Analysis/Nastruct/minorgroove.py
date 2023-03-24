import numpy as np
from numpy import *
import pandas as pd
import seaborn as sns
#import matplotlib as plt
from matplotlib import pyplot as plt
sns.set()

#ix = np.arange(start=0, stop=12)
#y = np.arange(start=0, stop = 500)
#BP.nastruct.dat
x = np.loadtxt('BP.nastruct.dat',unpack = True,usecols=(0),skiprows=(1))
x1=x/5
y = np.loadtxt('BP.nastruct.dat',unpack = True,usecols=(1),skiprows=(1))
z = np.loadtxt('BP.nastruct.dat',unpack = True,usecols=(12),skiprows=(1))
df = pd.DataFrame.from_dict(np.array([x1,y,z]).T)
df.columns = ['Time(ns)','Basepair number','Minor Groove']
df['Minor Groove'] = pd.to_numeric(df['Minor Groove'])
pivotted= df.pivot('Basepair number','Time(ns)','Minor Groove')
sns.heatmap(pivotted,cmap='RdBu')
plt.title("Width of Minor Groove in DNA (Angstroms)")
plt.show()

