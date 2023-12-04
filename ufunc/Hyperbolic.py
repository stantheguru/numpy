import numpy as np 

x = np.sinh(np.pi/2)

#cosh for values in an array
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
arr_cosh = np.cosh(arr)

#Finding Angles
angle = np.arcsinh(1.0)

#Angles of tanh values in an array
arr_tanh = np.array([0.1,0.2,0.3,0.4])
arr_angles = np.arctanh(arr_tanh)
print(arr_angles)