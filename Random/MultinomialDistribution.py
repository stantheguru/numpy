from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sbn 

x = random.multinomial(n=10,pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(x)