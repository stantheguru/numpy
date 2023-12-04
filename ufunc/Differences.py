import numpy as np 

arr = np.array([10,7,9,34])
arr_diff = np.diff(arr)

#Calculate discrete difference twice
arr_twice = np.diff(arr, n=2)
print(arr_twice)