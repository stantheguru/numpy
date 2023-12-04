import numpy as np 

arr = np.array([2,5,6,7,7])
x = np.prod(arr)

#2arrays
arr1 = np.array([2,6,4,90])
arr2 = np.array([5,7,8,66])
arr_prod = np.prod([arr1,arr2])

#Product on axis
arr_axis = np.prod([arr1,arr2], axis=1)

#Cumulative product
arr_cumprod = np.cumprod(arr1)
print(arr_cumprod)