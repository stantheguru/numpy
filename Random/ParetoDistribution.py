from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sbn 

x = random.pareto(a=2,size=(2,3))

#Visualization
sbn.distplot(random.pareto(size=10,a=2), kde=False, label='Pareto')
plt.title('Pareto Distribution')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.show()