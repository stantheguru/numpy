import numpy as np 

arr = np.array([1,4,5,6,7,7,7,7,5,4])
newarr = np.array_split(arr, 3) #3 -> number of splits

#Access solit arrays
arr0 = newarr[0]


#2D
arr_2d = np.array([[1,3], [5,7],[7,9],[4,7],[8,10],[6,8]])
newarr_2d = np.array_split(arr_2d,3)

#Specify axis
newarr_axis = np.array_split(arr_2d,3, axis=1)

#hsplit() -> Split 2d array into 2d arrays along rows
newarr_hsplit = np.hsplit(arr_2d,2)
print(newarr_hsplit)