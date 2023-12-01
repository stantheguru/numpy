from numpy import random
import numpy as np

#shuffle()
arr = np.array([1,9,3,4,5])
random.shuffle(arr)

#permutation
print(random.permutation(arr))