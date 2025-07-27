import numpy as np

# Create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Perform basic operations
addition = A + B
subtraction = A - B
multiplication = A * B  # element-wise
matrix_product = A @ B  # matrix multiplication
A_transpose = A.T

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("A + B:\n", addition)
print("A - B:\n", subtraction)
print("A * B (element-wise):\n", multiplication)
print("A @ B (matrix product):\n", matrix_product)
print("Transpose of A:\n", A_transpose)
