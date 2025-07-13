# Day10: 

import numpy as np 

# **Matrix Transformation
A = np.array([[2, -1],
              [3, 4]])  # 2x2 matrix
x = np.array([1, 2])  # 1x2 matrix
TM = A @ x  # Matrix multiplication
print(f"TM: {TM}")  # This will print the result of the matrix multiplication


# **Scaling Transformation
kx, ky = 1.5, 0.5
A = np.array([[kx, 0],
              [0, ky]])  # Scaling matrix
x = np.array([2, 3])  # 1x2 matrix
ST = A @ x  # Matrix multiplication
print(f"Original Vector: {x}\nScaled Vector: {ST}")  # This will print the result of the matrix multiplication


# **Rotation Transformation
theta = np.pi / 4  # 45 degrees in radians
A = np.array([[np.cos(-theta), -np.sin(-theta)],  # Anti-clockwise rotation matrix
              [np.sin(-theta), np.cos(-theta)]])  # Rotation matrix
x = np.array([3, 2])  # 1x2 matrix
RT = A @ x  # Matrix multiplication
print(f"Original Vector: {x}\nRotated Vector: {RT}")  # This will print the result of the matrix multiplication


# **Reflection about the x-axis
A = np.array([[1, 0],   
              [0, -1]])  # Reflection matrix
x = np.array([3, 2])  # 1x2 matrix
RF = A @ x  # Matrix multiplication
print(f"Original Vector: {x}\nReflected Vector: {RF}")  # This will print the result of the matrix multiplication


# **Reflection about the y-axis
A = np.array([[-1, 0],
              [0, 1]])  # Reflection matrix
x = np.array([3, 2])  # 1x2 matrix
RF = A @ x  # Matrix multiplication
print(f"Original Vector: {x}\nReflected Vector: {RF}")  # This will print the result of the matrix multiplication


# **Composition of Linear Transformations
A1 = np.array([[2, 0],
                [0, 3]])  # Scaling matrix
A2 = np.array([[0, -1],
                [1, 0]])  # Rotation matrix
A3 = np.array([[1, 0],
               [0, -1]])  # Reflection matrix
# Combined transformation
A_combined = A3 @ A2 @ A
x = np.array([1, 2])  # 1x2 matrix
result = A_combined @ x  # Matrix multiplication
print(f"Original Vector: {x}\nTransformed Vector: {result}")  # This will print the result of the matrix multiplication


# **Associative Property of Matrix Multiplication
# (B @ A) @ x = B @ (A @ x)
A = np.array([[2, 3],
              [4, 9]])
B = np.array([[4, 7],
              [4, 10]])
x = np.array([1, 2])
result1 = B @ (A @ x)
intermediate_matrix = B @ A  # B @ (A @ x) = (B @ A) @ x 
result2 = intermediate_matrix @ x 
print(result1)
print(result2)