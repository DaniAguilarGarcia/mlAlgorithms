import numpy as np
arr = np.array([[3, 56, 90],
                [34, 68, -5],
                [-45, 9, -14]])
print(repr(np.cumsum(arr)))
print(repr(np.cumsum(arr, axis=0)))
print(repr(np.cumsum(arr, axis=1)))
