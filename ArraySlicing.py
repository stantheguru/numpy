import numpy as np 

#1-D
arr = np.array([1,4,6,8,12,7,8,9,65])

#Slice index 1 to 5 - The result includes the start index but excludes the last index
print(arr[1:5])

#Slice from index 4 to the ened of the array
print(arr[4:])

#Slice from beginning to index 4 - index 4 not included
print(arr[:4])

#NEGATIVE SLICING
#Index 3 from the end to index 1 from the end
print(arr[-3:-1])

#STEP - START:END:STEP
#Print every other element from index 1 to 5
print(arr[1:5]) #without step
print(arr[1:5:2])

#2-D
arr_2dm = np.array([[1,3,4,9,56,6],[23,4,5,6,3,3]])
#Slice secodn row from index 1 to index 4
print(arr_2dm[1,1:4])

#From both element return index 2
print(arr_2dm[0:2,2])

#From both elements slice 1 to 4
print(arr_2dm[0:2,1:4])

#3-D
arr_3d = np.array([[[2,3,4,5,7], [4,5,6,7,7],[5,6,6,7,78],[6,7,8,9,9]]])
#print 1 to 4 from the third row
print(arr_3d[0][2][0:4])