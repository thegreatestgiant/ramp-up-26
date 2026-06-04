import numpy as np

# Problem 1
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
# Find the distinct overlapping values. Have an output
print(np.union1d(a, b))


c = np.stack((np.arange(1, 6), np.arange(6, 11), np.arange(11, 16)), axis=1)

three = c.flatten("F")
