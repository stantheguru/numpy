from numpy import random 
import seaborn as sbn
import matplotlib.pyplot as plt

x = random.logistic(loc=1,scale=2,size=(2,3))

#Visualization
#sbn.distplot(x, hist=False)
#plt.show()

#Logistic vs Normal
sbn.distplot(random.normal(size=1000,scale=2,loc=1), hist=False, label='Normal')
sbn.distplot(random.logistic(size=1000,loc=1,scale=2),hist=False,label='Logistic')
plt.legend()

plt.show()