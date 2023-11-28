import numpy as np 

arr = np.array([1,5,6,78,8,9])
#Copy  - the copy is a new array
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

#View -  the view is a just a view of the original array
arr_original = np.array([1,2,34,45,5,6,6,6])
view = arr_original.view()
arr_original[0] = 45
print(arr_original)
print(view)

#Update view
view[0] = 34
print(arr_original)
print(view)

#Check if Array owns the data
arr_origin = np.array([1,4,5,76,7,8,7])
c = arr_origin.copy()
v = arr_origin.view()

print(c.base)
print(v.base)