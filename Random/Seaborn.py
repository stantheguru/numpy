import matplotlib.pyplot as plt 
import seaborn as sbn #pip install seaborn ->used to visualize random distributions.


#sbn.distplot([1,4,6,7,7])
#plt.show()

#Plot without histogram
sbn.distplot([7,4,32,3,2,22,34],hist=False)
plt.show()
