import numpy as np

# Creating two arrays
arr1 = np.array([[11, 12], [13, 14]])
arr2 = np.array([[15, 16], [17, 18]])

# Joining the NumPy arrays
arr3 = np.concatenate((arr1, arr2), axis=0)

print(arr3)