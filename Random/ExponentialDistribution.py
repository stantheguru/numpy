from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sbn

x = random.exponential(scale=2,size=(2,3))

#Visualization
print(random.exponential(size=1000))
sbn.distplot(random.exponential(size=1000),hist=False)
plt.show()
