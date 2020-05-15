import numpy as np
arr = np.array([[3, 56, 90],
                [34, 68, -5],
                [-45, 9, -14]])
print(np.mean(arr))
print(np.var(arr))
print(np.median(arr))
print(repr(np.median(arr, axis=-1)))
