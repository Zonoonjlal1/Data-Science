# Importing the numpy library
import numpy as np
# Creating a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Demonstrating basic operations on arrays
array_addition = array + 5
array_subtraction = array - 2

# Demonstrating mathematical functions
array_sum = np.sum(array)
array_mean = np.mean(array)

# Demonstrating slicing
array_slice = array[1:4]

# Printing the output of operations
print("Original Array:", array)
print("Array after addition:", array_addition)
print("Array after subtraction:", array_subtraction)
print("Sum of array elements:", array_sum)
print("Mean of array elements:", array_mean)
print("Sliced Array:", array_slice)
