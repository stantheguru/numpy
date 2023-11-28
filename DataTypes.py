#Numpy datatypes
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )


import numpy as np 

#Integer Array
arr_int = np.array([2,3,4,7,8])

print(arr_int.dtype)

#String array
arr_str = np.array(['Joy', 'Love','Peace'])
print(arr_str.dtype)

#Array with defined data type
arr_defined = np.array([1,2,4,4,4], dtype='S')
print(arr_defined.dtype)

#For i, u, f, S and U we can define size as well.

arr_size = np.array([1,3,2,4], dtype='i4')
print(arr_size.dtype)

#If array cannot be coinverted to a nitehr data tyoe you get value error
arr_error = np.array(['4','4','t'],dtype='S')

#Converting existing array to anotehr data type

arr_toconvert = np.array([1.2,4.6,6.7,5.8])
#Convert float array to integer array using i
new_arr = arr_toconvert.astype('i')
print(new_arr)
print(new_arr.dtype)

#Convert float array to integer array using int
new_arr_int = arr_toconvert.astype(int)
print(new_arr_int)
print(new_arr_int.dtype)

#Integer array to boolean
arr_int = np.array([1,2,3,0])
arr_bool = arr_int.astype(bool)
print(arr_bool)
print(arr_bool.dtype)



