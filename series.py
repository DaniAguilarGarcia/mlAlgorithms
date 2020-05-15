#The code below shows how to create pandas Series objects using pd.Series.
import numpy as np
import pandas as pd  
series = pd.Series()
# Newline to separate series print statements
#we initialized each Series with its values by setting the first argument using a scalar, list, or NumPy array.
print('{}\n'.format(series))

series = pd.Series(5)
print('{}\n'.format(series))

series = pd.Series([1, 2, 3])
print('{}\n'.format(series))

series = pd.Series([1, 2.2]) # upcasting
print('{}\n'.format(series))

arr = np.array([1, 2])
series = pd.Series(arr, dtype=np.float32) #pd.Series also needs a dtype keyword argument for manual casting
print('{}\n'.format(series))

series = pd.Series([[1, 2], [3, 4]])
print('{}\n'.format(series))
 # Furthermore, since Series objects are 1-D, the ser variable represents a Series with lists as elements, rather than a 2-D matrix.
