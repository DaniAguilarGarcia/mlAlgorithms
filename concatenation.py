import numpy as np
#aggregates 2 arrays
arr1 = np.array([[0, 72, 3],
                 [1, 3, -60],
                 [-3, -2, 4]])
arr2 = np.array([[-15, 6, 1],
                 [8, 9, -4],
                 [5, -21, 18]])
print(repr(np.concatenate([arr1, arr2])))
#axis=1 horizontally 
print(repr(np.concatenate([arr1, arr2], axis=1))) 
print(repr(np.concatenate([arr2, arr1], axis=1)))
