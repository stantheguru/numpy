from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sbn

x = random.chisquare(df=2,size=(4,5))

#Visualization
sbn.distplot(x)
plt.show()