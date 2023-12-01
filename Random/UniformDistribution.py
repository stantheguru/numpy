from numpy import random 
import seaborn as sbn
import matplotlib.pyplot as plt

x = random.uniform(size=(2,3))

#Visualization
sbn.distplot(x)
plt.show()
