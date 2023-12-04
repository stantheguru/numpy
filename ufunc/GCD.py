import numpy as np 

num1=6
num2=9

x = np.gcd(num1,num2)

#GCD/HCF on array
arr = np.array([3,6,7,4,5])
gcd = np.gcd.reduce(arr)
print(gcd)