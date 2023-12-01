import numpy as np 

arr = np.array([13,5,7,8])
x = np.array([True,False,True,True])
newarr = arr[x]

#Creating filter array

filter_array = []
for i in arr:
    if i>3:
        filter_array.append(True)
    else:
        filter_array.append(False)

newarr_filter = arr[filter_array]

#Filter directly from array
filter_direct = arr > 6
newarr_direct = arr[filter_direct]
print(newarr_direct)