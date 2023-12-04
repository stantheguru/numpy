import numpy as np
from math import log

arr = np.arange(1,10)
arr_log2 = np.log2(arr)

#Log10
arr_log10 = np.log10(arr)
print(arr_log10)

#Natural log or log base e
arr_loge = np.log(arr)

#Log at any base
nplog = np.frompyfunc(log,2,1)
print(nplog(10,2))
