# Day14: Revise previously learn topic: NumPy Fundamentals and Mathematical Operations in NumPy

import numpy as np 

#*Matrix
# 2D array
m = np.array([[1, 2], [4, 5]])
print(m)

# Matrix Multiplication
A = np.array([[1], [2], [3]]) # 3x1 matrix
B = np.array([[4, 5]]) # 1x2 matrix
# C = np.dot(A, B) # Matrix multiplication
# *Or
C = A @ B # Matrix multiplication
# *Or
# C = np.matmul(A, B) # Matrix multiplication
# *Or
# C = A * B  # This will perform element-wise multiplication, not matrix multiplication
print(C)

# **Reflection about the x-axis
A = np.array([[1, 0],   
              [0, -1]])  # Reflection matrix
x = np.array([3, 2])  # 1x2 matrix
RF = A @ x  # Matrix multiplication
print(f"Original Vector: {x}\nReflected Vector: {RF}")

# Below rank is 3 because all vectors are linearly independent
v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])
v3 = np.array([0, 0, 1])

# *OR
# Below rank is 3 because all vectors are linearly independent
v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])
v3 = np.array([0, 1, 1])

# **OR
# Below rank is 2 because v3 is a linear combination of v1 and v2
v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])
v3 = np.array([1, 1, 0])

# Create a matrix from the vectors
A = np.column_stack((v1, v2, v3))
print(A)

# print even number 1 to 100
even_numbers = np.arange(2, 101, 2)
print(even_numbers)

# Accessing Element in 1D Array
arr_1d = np.array([10, 20, 30, 40, 50])
print(arr_1d)
print(arr_1d[1:4])
print(arr_1d[::2])


# **Array Reshaping: It is the process of changing the shape of an existing array without changing its data.
# It is valid for evenly divisible arrays.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
re_arr = arr.reshape(5, 2)
re_arr = arr.reshape(2, 5)
re_arr = arr.reshape(5, -1)
re_arr = arr.reshape(2, -1)
re_arr = arr.reshape(10, 1)
re_arr = arr.reshape(10, -1)
print(arr)
print(re_arr)