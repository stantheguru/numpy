from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sbn

x = random.normal(size=(2,3),loc=1,scale=2)

#Visualize Normal Distribution
sbn.distplot(random.normal(size=1000), hist=False)
plt.show()
