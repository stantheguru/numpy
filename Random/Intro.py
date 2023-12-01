from numpy import random

x = random.rand() #Generate a random float from 0 to 1:

#Generate random array
#1d array containing 5 integers from 0 to 100
arr = random.randint(100,size=(5))

#Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
arr_2d = random.randint(100,size=(3,5))


#Floats
#1d
arr_floats = random.rand(5)

#2d
arr_floats_2d = random.rand(3,5)

#Random number from an array
num = random.choice([2,3,7,8,9])

#Random array
arr_rand = random.choice([2,4,5,6], size=(3,5))
print(arr_rand)