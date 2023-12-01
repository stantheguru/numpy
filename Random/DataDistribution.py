from numpy import random

x = random.choice([3,5,7,8],p=[0.1,0.0,0.7,0.2],size=(100))

#2d
arr_2d = random.choice([3,6,9,10,56], p=[0.0,0.4,0.3,0.2,0.1],size=(3,5))
print(arr_2d)