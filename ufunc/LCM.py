import numpy as np 

num1 = 2
num2 = 4

x = np.lcm(num1,num2)

#LCM in arrays
arr = np.array([3,5,7,8])
lcm = np.lcm.reduce(arr)
print(lcm)