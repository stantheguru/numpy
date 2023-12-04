import numpy as np 

x = np.sin(4)

#Sin of values in an array
arr = np.array([1,4,6,7,7,8])
arr_sin = np.sin(arr)

#Degrees into radians
arr_deg = np.array([30,45,78,180])
arr_rad = np.deg2rad(arr_deg)
print(arr_rad)

#Radians to degrees
arr_rads = np.array([0.52359878,0.78539816,1.36135682,3.14159265])
arr_degs = np.rad2deg(arr_rads)

#Finding Angles
#Angle of 1.0
angle = np.arcsin(1.0)

#Angles in an array
arr_sins = np.array([1,-1,0.1])
arr_angles = np.arcsin(arr_sins)

#Hypotenues
base = 3
perp = 4
hyp = np.hypot(base,perp)
print(hyp)