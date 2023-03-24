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
x = np.loadtxt('BPstep.nastruct.dat',unpack = True,usecols=(0),skiprows=(1))
x1=x/5
y = np.loadtxt('BPstep.nastruct.dat',dtype='str',unpack = True,usecols=(1),skiprows=(1))
z = np.loadtxt('BPstep.nastruct.dat',unpack = True,usecols=(4),skiprows=(1))
df = pd.DataFrame.from_dict(np.array([x1,y,z]).T)
df.columns = ['Time (ns)','Basepairs','Slide']
df['Slide'] = pd.to_numeric(df['Slide'])
pivotted= df.pivot('Basepairs','Time (ns)','Slide')
sns.heatmap(pivotted,cmap='RdBu')
plt.title("Width of Slide in DNA (Angstroms)")
plt.show()

