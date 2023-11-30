import numpy as np

arr = np.array([1,4,5,6,6,9])
for i in arr:
    print(i)

#2D
arr_2d = np.array([[13,4,5,6,6],[4,5,5,6,6]])
for j in arr_2d:
    for k in j:
        print(k)


#3D
arr_3d = np.array([[[1,4,5,6,6],[5,5,4,4,3],[5,4,3,2,2]]])
for l in arr_3d:
    for m in l:
        for o in m:
            print(o)



#Iterating using nditer()
arr_nd = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr_nd):
    print(x)

#Iterating with differnt data types
arr_dt = np.array([3,5,6,7,7])
for z in np.nditer(arr_dt, flags=['buffered'], op_dtypes=['S']):
    print(z)

#Iterating with different step size
arr_step = np.array([[2,4,5,6],[4,5,6,4]])
for s in np.nditer(arr_step[:, ::2]):
    print(s)

#Enumerated iteration using ndenumerate()
arr_en = np.array([1,4,5,56])
for idx, dx in np.ndenumerate(arr_en):
    print(idx,dx)

#Enumerate 2D
arr_2d_en = np.array([[2,3,4],[4,5,6]])
for idx2, dx2 in np.ndenumerate(arr_2d_en):
    print(idx2,dx2)
