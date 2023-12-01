from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sbn 

x = random.poisson(lam=2,size=1000)
print(x)

#Visualization
sbn.distplot(x,kde=False)
plt.show()
