import numpy as np 

arr = np.array([1,6,7,8,4,44,6,63,55])
newarr = np.sort(arr)

#Sort string array
arr_str = np.array(['Joe','Arthur', 'Eckart', 'Alan','Elon'])
newarr_str = np.sort(arr_str)

#2d
arr_2d = np.array([[2,4,6],[6,1,4]])
newarr_2d = np.sort(arr_2d)
print(newarr_2d)