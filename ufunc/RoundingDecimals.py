import numpy as np 

#Truncation
arr_trunc = np.trunc([-3.6373, 5.786])
print(arr_trunc)

#Fix
arr_fix = np.trunc([-3.6373,5.4333])
print(arr_fix)

#Rounding
arr_round = np.around([3.689, 2])
print(arr_round)

#Floor
arr_floor = np.floor([3.5,7.9,2.1])
print(arr_floor)

#Ceil
arr_ceil = np.ceil([11.3,78.9])
print(arr_ceil)