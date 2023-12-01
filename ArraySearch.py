import numpy as np 

arr = np.array([1,5,6,7,3,3,32])
#Where return index
x = np.where(arr==3)

#Where values are even
even = np.where(arr%2==0)

#where values are odd
odd = np.where(arr%2==1)


#searchsorted() -> performs a binary search where the specified value should be inserted to maintain a sorted order
sort = np.searchsorted(arr,2)


#search from right side
right = np.searchsorted(arr,7, side='right')

#Multiple values
multiple = np.searchsorted(arr,[2,1,3])
print(multiple)