# Day11: R square and R cube

import numpy as np 

# Rank = no of linearly independent columns in a vector space

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

# Compute the rank of the matrix
Rank = np.linalg.matrix_rank(A)
print(f"Rank of the matrix = {Rank}")   

# *Rank of R square: Full rank is 2
v1 = np.array([1, 2])
v2 = np.array([3, 10]) # v2 = 3 * v1 : Linearly dependent

# *OR

v1 = np.array([1, 2])
v2 = np.array([2, 4]) # v2 = 2 * v1 : Linearly dependent

A = np.column_stack((v1, v2))
print(A)

Rank = np.linalg.matrix_rank(A)
print(f"Rank of the matrix = {Rank}")

# Rank of R cube
v1 = np.array([1, 2, 3]) # Linearly independent
v2 = np.array([2, 4, 6]) # Linearly dependent (v2 = 2 * v1)
v3 = np.array([9, 8, 10]) # Linearly independent

A = np.column_stack((v1, v2, v3))
print(A)

Rank = np.linalg.matrix_rank(A)
print(f"Rank of the matrix = {Rank}")