import numpy as np # Numerical Python (NumPy) for numerical operations
import scipy.linalg as la # Linear algebra functions

#*Vector
# 1D array
v = np.array([5, 2, 3])
print(v)

#*Matrix
# 2D array
m = np.array([[1, 2], [4, 5]])
print(m)

#*Scalar Multiplication
# 4 = scalar
v_scaled = v * 4
print(v_scaled)

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

# Matrix Addition
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = A + B  # Matrix addition
print(C)


# Matrix Subtraction
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = A - B  # Matrix subtraction
print(C)

#Matrix Transpose
A = np.array([[1, 2], [3, 4]])
B = A.T  # Transpose of matrix A
print(B)

# *Solving Linear Equations
# 2x + 3y = 5
# 4x + 5y = 6

A = np.array([[2, 2], [4, 5]])  # Coefficient matrix
b = np.array([5, 6])  # Constant terms
x = np.linalg.solve(A, b)  # Solve the linear equations
print(x)  # x contains the values of x and y that solve the equations
# *OR
print(f'x = {x[0]}, y = {x[1]}')  # x contains the values of x and y that solve the equations

A = np.array([[8, 3, -2], [-4, 7, 5], [3, 4, -12]])  # Coefficient matrix
b = np.array([9, 15, 35])  # Constant terms
x = np.linalg.solve(A, b)  # Solve the linear equations
print(f'x = {x[0]}, y = {x[1]}, z = {x[2]}')  # x contains the values of x, y, and z that solve the equations

# *LU Decomposition: Decomposes a matrix into a lower triangular matrix (L) and an upper triangular matrix (U)
# A*Applicable only for square matrices
# P*Permutation matrix is used to handle row exchanges during decomposition
# L*Lower triangular matrix is a matrix where all entries above the main diagonal are zero
# U*Upper triangular matrix is a matrix where all entries below the main diagonal are zero
A = np.array([[2, 4, 5], [1, 3, 2], [4, 2, 1]])  # Coefficient matrix

P, L, U = la.lu(A)  # LU decomposition
# print("P:", P)  # Permutation matrix
# print("L:", L)  # Lower triangular matrix
# print("U:", U)  # Upper triangular matrix
# *OR
print(f"P = {P}")
print(f"L = {L}")
print(f"U = {U}")

# *QR Decomposition: Decomposes a matrix into an orthogonal matrix (Q) and an upper triangular matrix (R)
# A*Applicable for any matrix, not just square matrices
# Q*Orthogonal matrix is a matrix whose columns are orthogonal unit vectors
# R*Upper triangular matrix is a matrix where all entries below the main diagonal are zero

A = np.array([[1, 2, 3], [3, 4, 5]])  # Coefficient matrix
Q, R = la.qr(A)  # QR decomposition
print("Q:", Q)  # Orthogonal matrix
print("R:", R)  # Upper triangular matrix

result = Q @ R  # Reconstruct the original matrix
print("Reconstructed A:", result)  # Should be close to the original matrix A

# *LU Decomposition vs QR Decomposition
# LU decomposition is used for solving linear equations and matrix inversion, while QR decomposition is used for least squares problems and orthogonalization.
# LU decomposition is applicable only for square matrices, while QR decomposition can be applied to any matrix.
# LU decomposition results in a lower triangular matrix and an upper triangular matrix, while QR decomposition results in an orthogonal matrix and an upper triangular matrix.