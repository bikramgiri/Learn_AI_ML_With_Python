#  Day15: Broadcasting, Broadcasting a 1D and 2D Array, Broadcasting a Scalar to a Matrix, Broadcasting a Scalar to a Vector , Broadcasting a Vector to a Matrix, Sorting a 1D and 2D Array, Sorts each column and row in ascending order, Sorts each column and row in descending order, Appending: Adding a new row to a matrix, Adding a new column to a matrix, 

import numpy as np

# Scalar(s) to Vector(v)
arr = np.array([1, 2, 3, 4, 5]) # V
s = 5 # s
new_arr = arr * s
print(arr)
print(new_arr)

# Scalar(s) to Matrix(m)
matx = np.array([[1, 2, 4], [2, 3, 5], [5, 7, 3]]) # M
s = 4 # s
new_matx = matx + s
print(matx)
print(new_matx)

# vector(v) to Matrix(m)
matx = np.array([[2, 4, 7], [3, 4, 6], [4, 6, 9]]) # M
v = np.array([1, 2, 3]) # v
new_matx = matx + v
print(matx)
print(new_matx)


# Sorting
a = np.array([1, 4, 2, 3, 5]) # 1D array
# sorted_a = np.sort(a) # Sorts the array in ascending order
sorted_a = np.sort(a)[::-1] # Sorts the array in descending order
print(a)
print(sorted_a)

# Sorts each column and row in ascending order
matx = np.array([[4, 6, 9],
                 [2, 1, 8],
                 [7, 9, 1]])
new_matx1 = np.sort(matx, axis=1) # Sorts each row in ascending order
new_matx2 = np.sort(matx, axis=0) # Sorts each column in ascending order
print(matx)
print(new_matx1)
print(new_matx2)

# Sorts each column and row in descending order
matx = np.array([[4, 6, 9],
                 [2, 1, 8],
                 [7, 9, 1]])
new_matx1 = np.sort(matx, axis=1)[::-1] # Sorts each row in descending order
new_matx2 = np.sort(matx, axis=0)[::-1] # Sorts each column in descending order
print(matx)
print(new_matx1)
print(new_matx2)

#Appending: 
# Adding a new row to a matrix
matx = np.array([[1, 2, 3],
                 [2, 3, 6]])
new_row = np.array([[2, 5, 7]]) # New row to be added
new_row2 = np.array([[3, 4, 5]]) # Another new row to be added
new_matx = np.append(matx, new_row, axis=0)
new_matx2 = np.append(new_matx, new_row2, axis=0)
print(matx)
print(new_matx)
print(new_matx2)

# Adding a new column to a matrix
matx = np.array([[1, 2, 3],
                 [2, 3, 6]])
new_col = np.array([[4], [5]])
new_col2 = np.array([[6], [7]])
new_matx = np.append(matx, new_col, axis=1)
new_matx2 = np.append(new_matx, new_col2, axis=1)
print(matx)
print(new_matx)
print(new_matx2)
