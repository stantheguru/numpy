import numpy as np 

arr = np.array([1,4,5,6,6,9,1,1,7])
x = np.unique(arr)

#Union
arr1 = np.array([1,4,5,6,7])
arr2 = np.array([7,8,6,3,2,5,65,4])
arr_union = np.union1d(arr1,arr2)

#Intersection
arr_inter = np.intersect1d(arr1,arr2, assume_unique = True)

#Difference
arr_diff = np.setdiff1d(arr1,arr2,assume_unique=True)

#Symmetric difference - values not present in both sets
arr_sym = np.setxor1d(arr1,arr2,assume_unique=True)
print(arr_sym)
