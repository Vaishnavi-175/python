import numpy as np


arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

zeros = np.zeros((2, 3))
print("Zeros array:\n", zeros)

ones = np.ones((3, 2))
print("Ones array:\n", ones)


range_arr = np.arange(10, 21, 2)
print("Range array:", range_arr)


arr2 = np.array([5, 4, 3, 2, 1])
sum_arr = arr + arr2
print("Sum of arrays:", sum_arr)

print("Mean of arr:", np.mean(arr))
print("Standard deviation of arr:", np.std(arr))
