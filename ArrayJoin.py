import numpy as np 

arr1 = np.array([1,4,5,5,5])
arr2 = np.array([2,3,4,45,7,5,5,5])
arr = np.concatenate((arr1,arr2))

#3D
#Join 2 2D arrays along rows(axis=1)
arr_2d1 = np.array([[1,3,4,5],[4,7,8,89]])
arr_2d2 = np.array([[2,5,6,6],[7,6,54,4]])
arr_2d = np.concatenate((arr_2d1,arr_2d2),axis=1)

#Joining using stack functions - done along a new axis
arr_1 = np.array([1,2,3])
arr_2 = np.array([4,8,7])

arr_stack = np.stack((arr_1,arr_2), axis=1)
print(arr_stack),

#Stacking alomg rows using hstack()
arr_hstack = np.hstack((arr_1,arr_2))
print(arr_hstack)

#Stacking along columns using vstack()
arr_vstack = np.vstack((arr_1, arr_2))
print(arr_vstack)

#Stack along height/depth using dstack()
arr_dstack = np.dstack((arr_1,arr_2))
print(arr_dstack)