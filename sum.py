import numpy as np
arr = np.array([[3, 56, 90],
                [34, 68, -5],
                [-45, 9, -14]])
print(np.sum(arr))
print(repr(np.sum(arr, axis=0)))
print(repr(np.sum(arr, axis=1)))
