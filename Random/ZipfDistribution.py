from numpy import random
import seaborn as sbn 
import matplotlib.pyplot as plt  

x = random.zipf(a=2,size=(2,3))

#Visualization 
sbn.distplot(random.zipf(a=2,size=(10)))
plt.xlabel('Rank')
plt.ylabel('PDF')
plt.show()
