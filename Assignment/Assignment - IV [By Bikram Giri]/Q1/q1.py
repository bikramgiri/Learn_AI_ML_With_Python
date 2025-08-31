# Linear Algebra Fundamentals
import numpy as np

def matrix_operations(A, B):
    A = np.array(A)
    B = np.array(B)

    # Matrix multiplication
    try:
        mat_mul = np.matmul(A, B)
    except ValueError:
        mat_mul = "Matrix multiplication not possible (incompatible dimensions)."

    # Element-wise multiplication
    try:
        elem_mul = np.multiply(A, B)
    except ValueError:
        elem_mul = "Element-wise multiplication not possible (different shapes)."

    # Determinant of A
    try:
        det_A = np.linalg.det(A)
    except np.linalg.LinAlgError:
        det_A = "Determinant not defined for this matrix."

    # Transpose of B
    transpose_B = np.transpose(B)

    # Return results
    return mat_mul, elem_mul, det_A, transpose_B


# Test with first matrix pair
A1 = [[2, 3], [1, 4]]
B1 = [[5, 2], [3, 1]]
results1 = matrix_operations(A1, B1)

print("Test 1:")
print("Matrix Multiplication:\n", results1[0])
print("Element-wise Multiplication:\n", results1[1])
print("Determinant of A:", results1[2])
print("Transpose of B:\n", results1[3])

# Test with second matrix pair
A2 = [[1, 2, 3], [4, 5, 6]]
B2 = [[7, 8], [9, 10], [11, 12]]
results2 = matrix_operations(A2, B2)

print("\n\nTest 2:")
print("Matrix Multiplication:\n", results2[0])
print("Element-wise Multiplication:\n", results2[1])
print("Determinant of A:", results2[2])
print("Transpose of B:\n", results2[3])
