from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sbn

x = random.binomial(n=10,p=0.5,size=1000)

#Visualization
sbn.distplot(x,hist=False, label='Normal')

#Diff btn normal and binomial distributions
xnormal = random.normal(loc=50,scale=5,size=1000)
sbn.distplot(xnormal,hist=False,label='Binomial')

plt.show()

