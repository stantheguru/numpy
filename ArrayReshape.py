import numpy as np 

#Reshape 1D to 2D
arr = np.array([1,2,3,4,5,5,6,7,8,8,8,6])

newarr = arr.reshape(4,3)

#Reshape 1D to 3D
arr_3d = arr.reshape(2,3,2)

#Check if its copy or view
print(arr.reshape(3,4).base)

#Unknown Dimension
arr_un = arr.reshape(2,2,-1) #-1 is the unknown value


#Flattening array - Converting array to 1D
arr_2d = np.array([[2,4,6,7],[5,6,7,8]])
arr_1d = arr_2d.reshape(-1)
print(arr_1d)
