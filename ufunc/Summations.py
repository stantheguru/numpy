import numpy as np 

arr1 = np.array([3,5,7,97])
arr2 = np.array([5,8,3,6])
arr = np.sum([arr1,arr2])

#summation over an exis
arr_axis = np.sum([arr1,arr2], axis=1)

#Cumulative sum
arr_cum = np.cumsum([arr1])
print(arr_cum)