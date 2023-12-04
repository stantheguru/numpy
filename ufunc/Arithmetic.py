import numpy as np 

arr1 = np.array([1,4,5,6,4])
arr2 = np.array([3,2,7,8,8])
arr_add = np.add(arr1,arr2)

#subtract
arr_sub = np.subtract(arr1,arr2)

#multiply
arr_multi = np.multiply(arr1,arr2)

#Division
arr_div = np.divide(arr1,arr2)

#Power
arr_power = np.power(arr1,arr2)

#Remainder
arr_rem = np.remainder(arr1,arr2)

#Mod
arr_mod = np.mod(arr1,arr2)

#Quotient and Mod ->divmod() return tow arrays, that is, quotient and mod
arr_quo = np.divmod(arr1,arr2)

#Absolute
arr_abs = np.absolute(arr1)
print(arr_abs)
