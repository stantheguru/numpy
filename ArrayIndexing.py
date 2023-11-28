import numpy as np 

#1-D
arr_1dm = np.array([1,2,3,4,4,4])

#2-D
arr_2dm = np.array([[1,5,6,43,4],[3,7,8,9,7]])

#access second element on second rowx
element = arr_2dm[1,1]


#3-D
arr_3dm = np.array([[[1,4,5,6,9],[4,5,7,33,55],[6,6,5,5,2]]])

#access second elemnt on 1st row
elem = arr_3dm[0,0,1]

#Negative indexing
#Get last element from the 2dm
print(arr_2dm[1,-1])



