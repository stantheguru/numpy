import numpy as np 

arr = np.array([1,3,4,5,56])

a = np.array(42) #0-Dimensional array
b = np.array([1, 2, 3, 4, 5]) #1-Dimensional array
c = np.array([[1, 2, 3], [4, 5, 6]]) #2-Dimensional array
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) #3-Dimensional array

#Higher dimensional array

harr = np.array([1,3,4,5], ndmin=5)
print(harr.ndim)