import numpy as np 

def myadd(x,y):
    return x+y

myadd = np.frompyfunc(myadd,2,1)
print(myadd([1,4,5,5],[4,6,7,7]))

#Check if a function is a ufunc
if type(np.add) == np.ufunc:
    print("The function is ufunc")
else:
    print("Its not a ufunc")