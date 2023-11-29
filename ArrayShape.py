import numpy as np 

#2D
arr = np.array([[12,4,5,6,7],[84,5,5,3,33]])

#5D
arr_5d = np.array([1,3,5,5,56], ndmin=5)
print(arr_5d.shape)