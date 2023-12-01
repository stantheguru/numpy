#Used for signal processing
from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sbn

x = random.rayleigh(scale=2,size=(2,3))

#Visualization
sbn.distplot(x, hist=False)
plt.show()

