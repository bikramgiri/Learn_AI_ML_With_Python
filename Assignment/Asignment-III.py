# 2

# import numpy as np

# def check_linearity(T):
#     # Create two sample vectors and a scalar
#     u = np.array([[1], [2]])
#     v = np.array([[3], [4]])
#     c = 5

#     # Additivity: T(u + v) == T(u) + T(v)
#     left_add = T @ (u + v)
#     right_add = (T @ u) + (T @ v)
#     additivity = np.allclose(left_add, right_add)

#     # Homogeneity: T(c * u) == c * T(u)
#     left_hom = T @ (c * u)
#     right_hom = c * (T @ u)
#     homogeneity = np.allclose(left_hom, right_hom)

#     # Final result
#     if additivity and homogeneity:
#         print("The transformation is linear.")
#     else:
#         print("The transformation is NOT linear.")

# # Example usage:
# T = np.array([[2, 0], [0, 3]])  # This is the matrix for T(x, y) = (2x, 3y)
# check_linearity(T)




# 3

# import numpy as np

# # Coefficient matrix A and augmented matrix [A|b]
# A = np.array([[1, 2],
#               [2, 4]])

# b = np.array([[3],
#               [6]])

# augmented = np.hstack((A, b))

# # Compute ranks
# rank_A = np.linalg.matrix_rank(A)
# rank_aug = np.linalg.matrix_rank(augmented)
# n = A.shape[1]  # number of variables

# # Classification based on rank
# if rank_A == rank_aug:
#     if rank_A == n:
#         print("The system is consistent and independent (unique solution).")
#     else:
#         print("The system is consistent and dependent (infinitely many solutions).")
# else:
#     print("The system is inconsistent (no solution).")





# 4

# import numpy as np

# # Coefficient matrix A and constant vector b
# A = np.array([[2, 3],
#               [5, 4]])

# b = np.array([8, 13])

# # Solve using np.linalg.solve (for exact solution)
# try:
#     solution_solve = np.linalg.solve(A, b)
#     print("Solution using np.linalg.solve:", solution_solve)
# except np.linalg.LinAlgError:
#     print("np.linalg.solve: No unique solution.")

# # Solve using np.linalg.lstsq (least squares, works for all systems)
# solution_lstsq, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
# print("Solution using np.linalg.lstsq:", solution_lstsq)





# 5

# import numpy as np

# # Define the matrix A
# A = np.array([[1, 2],
#               [3, 4]])

# # Transpose
# transpose_A = A.T
# print("Transpose of A:\n", transpose_A)

# # Determinant
# det_A = np.linalg.det(A)
# print("\nDeterminant of A:", det_A)

# # Inverse (only if determinant is not 0)
# if det_A != 0:
#     inverse_A = np.linalg.inv(A)
#     print("\nInverse of A:\n", inverse_A)

#     # Verify A * A^-1 ≈ Identity matrix
#     identity = np.dot(A, inverse_A)
#     print("\nA * A^-1:\n", identity)
#     print("\nIs A * A^-1 ≈ Identity?:", np.allclose(identity, np.eye(2)))
# else:
#     print("\nMatrix A is not invertible (determinant is 0).")






# 6

# import numpy as np
# from scipy.linalg import lu

# # Define a 3x3 matrix
# A = np.array([[4, 3, 2],
#               [2, 1, 5],
#               [6, 7, 8]])

# # Perform LU decomposition
# P, L, U = lu(A)

# print("Permutation matrix P:\n", P)
# print("\nLower triangular matrix L:\n", L)
# print("\nUpper triangular matrix U:\n", U)






# 7

# import numpy as np

# # Given matrix A and vector b
# A = np.array([[1, 2],
#               [3, 4],
#               [5, 6]])
# b = np.array([1, 2, 3])

# # Perform QR decomposition of A
# Q, R = np.linalg.qr(A)

# # Compute Q^T * b
# Qt_b = np.dot(Q.T, b)

# # Since R is upper-triangular (2x2), solve Rx = Q^T b by back-substitution
# # np.linalg.solve works for square systems
# x = np.linalg.solve(R, Qt_b)

# print("Solution x:", x)





# 8

# import numpy as np
# import matplotlib.pyplot as plt

# # Consistent system
# # x + y = 2
# # x - y = 0
# A1 = np.array([[1, 1], [1, -1]])
# b1 = np.array([2, 0])
# x1 = np.linalg.solve(A1, b1)

# # Inconsistent system
# # x + y = 2
# # x + y = 4 (parallel lines, different intercepts)
# A2 = np.array([[1, 1], [1, 1]])
# b2 = np.array([2, 4])
# # Least-squares approach (gives best approx. even if no exact solution)
# x2, residuals, rank, s = np.linalg.lstsq(A2, b2, rcond=None)

# # Plotting
# x_vals = np.linspace(-1, 4, 100)
# fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# # Plot Consistent
# axs[0].plot(x_vals, 2 - x_vals, label="x + y = 2")
# axs[0].plot(x_vals, x_vals, label="x - y = 0")
# axs[0].plot(*x1, 'ro', label='Intersection')
# axs[0].set_title("Consistent System")
# axs[0].legend()
# axs[0].grid(True)

# # Plot Inconsistent
# axs[1].plot(x_vals, 2 - x_vals, label="x + y = 2")
# axs[1].plot(x_vals, 4 - x_vals, label="x + y = 4")
# axs[1].set_title("Inconsistent System")
# axs[1].legend()
# axs[1].grid(True)

# plt.tight_layout()
# plt.show()






# 9

# import numpy as np

# A = np.array([[1, 2],
#               [2, 4]])
# b = np.array([3, 6])

# # Check determinant
# det = np.linalg.det(A)

# # Try solving using lstsq (since solve will fail)
# x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

# print("Determinant:", det)
# print("Rank:", rank)
# print("Solution (least squares):", x)






# 10

# import numpy as np

# def classify_system(A, b):
#     A = np.array(A, dtype=float)
#     b = np.array(b, dtype=float).reshape(-1, 1)

#     # Augmented matrix [A | b]
#     Ab = np.hstack((A, b))

#     # Compute ranks
#     rank_A = np.linalg.matrix_rank(A)
#     rank_Ab = np.linalg.matrix_rank(Ab)
#     n_vars = A.shape[1]

#     # Classification
#     if rank_A == rank_Ab:
#         if rank_A == n_vars:
#             return "Consistent with a unique solution"
#         else:
#             return "Consistent with infinite solutions"
#     else:
#         return "Inconsistent system"

# # Example 1: Unique Solution 
# A1 = [[2, 3], [1, 2]]
# b1 = [8, 5]
# print("System 1:", classify_system(A1, b1))

# # Example 2: Infinite Solutions
# A2 = [[1, 2], [2, 4]]
# b2 = [3, 6]
# print("System 2:", classify_system(A2, b2))

# # Example 3: Inconsistent
# A3 = [[1, 2], [2, 4]]
# b3 = [3, 7]
# print("System 3:", classify_system(A3, b3))





# 12

# import numpy as np

# # Define the vectors
# v1 = [1, 0, 0]
# v2 = [0, 1, 0]
# v3 = [0, 0, 1]

# # Stack as columns of a matrix
# A = np.column_stack((v1, v2, v3))

# # Compute the rank
# rank = np.linalg.matrix_rank(A)

# # Check if rank is 3
# if rank == 3:
#     print("The vectors form a basis for R^3.")
# else:
#     print("The vectors do NOT form a basis for R^3.")





# 13

# import numpy as np

# A = np.array([[1, 2, 3],
#               [4, 5, 6]])

# rank = np.linalg.matrix_rank(A)
# print("Rank =", rank)






# 14

# import numpy as np

# A = np.array([[1, 2, 3],
#               [2, 4, 6],
#               [1, 1, 1]])

# rank = np.linalg.matrix_rank(A)
# print("Rank of matrix A =", rank)






# 15

# import numpy as np
# from scipy.linalg import lu

# A = np.array([[1, 2, 3],
#               [2, 4, 6],
#               [3, 6, 9]], dtype=float)

# # Row Echelon Form via LU Decomposition
# _, L, U = lu(A)

# print("Row Echelon Form (U):\n", np.round(U, 2))

# # Count pivot columns
# rank = np.linalg.matrix_rank(A)
# print("Rank of A:", rank)





# 16

# import numpy as np

# # Create a rank-1 matrix where all columns are multiples of [1, 2, 3]
# col = np.array([[1], [2], [3]])
# A = np.hstack([col, 2*col, -5*col]) 

# # Display the matrix
# print("Matrix A:\n", A)

# # Compute rank
# rank = np.linalg.matrix_rank(A)
# print("Rank of A:", rank)

# # Check linear dependence
# print("\nColumn 2 = 2 × Column 1?")
# print(np.allclose(A[:, 1], 2 * A[:, 0]))

# print("Column 3 = -5 × Column 1?")
# print(np.allclose(A[:, 2], -5 * A[:, 0]))






# 17

# import numpy as np

# def check_full_rank_matrices(n=10, size=4):
#     full_rank_count = 0
    
#     for i in range(n):
#         matrix = np.random.randint(-10, 10, size=(size, size))
#         rank = np.linalg.matrix_rank(matrix)
#         print(f"Matrix {i+1}:\n{matrix}")
#         print(f"Rank: {rank}\n")
#         if rank == size:
#             full_rank_count += 1

#     percentage = (full_rank_count / n) * 100
#     print(f"Full rank matrices: {full_rank_count} out of {n}")
#     print(f"Percentage of full rank matrices: {percentage:.2f}%")

# # Run the function
# check_full_rank_matrices()








# 18

# import numpy as np

# # Define three vectors in R^3
# v1 = np.array([1, 0, 0])
# v2 = np.array([0, 1, 0])
# v3 = np.array([0, 0, 1])

# # Stack vectors column-wise into a matrix
# A = np.column_stack((v1, v2, v3))

# # Check rank
# rank = np.linalg.matrix_rank(A)

# # Display matrix and result
# print("Matrix A (formed by vectors as columns):\n", A)
# print("Rank of A:", rank)

# if rank == 3:
#     print("The vectors are linearly independent and form a basis of R^3.")
# else:
#     print("The vectors do not form a basis.")






# 19

# import numpy as np

# # Define the matrix
# A = np.array([
#     [1, 0, 1],
#     [0, 1, 1],
#     [0, 1, 1]
# ])

# # Compute the rank
# rank = np.linalg.matrix_rank(A)
# print("Rank of A:", rank)






# 20

import numpy as np
from numpy.linalg import matrix_rank

def find_column_space_basis(A):
    """
    Returns a basis for the column space of matrix A
    by selecting linearly independent columns.
    """
    A = np.array(A, dtype=float)
    rank = matrix_rank(A)
    n_cols = A.shape[1]

    basis_columns = []
    for i in range(n_cols):
        # Add the i-th column to the current basis set
        candidate = A[:, basis_columns + [i]]
        if matrix_rank(candidate) > len(basis_columns):
            basis_columns.append(i)
        # Stop if we've collected enough independent columns
        if len(basis_columns) == rank:
            break

    basis = A[:, basis_columns]
    return basis, basis_columns

# Example matrix
A = np.array([
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 1]
])

basis, cols = find_column_space_basis(A)
print("Original Matrix:\n", A)
print("\nBasis for the Column Space:\n", basis)
print("\nIndices of Basis Columns:", cols)



