#Day13: NumPy Fundamentals: Array Reshaping,Array Iteration, Mathematical Operations in NumPy: Element-wise Arithmetic Operations

import numpy as np

# NumPy Fundamentals:
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

# **Array Iteration: It is the process of iterating over each element in an array.
# Iterating over a 1D array
arr_1d = np.array([10, 20, 30, 40]) 
for num in arr_1d: 
    print(num) 
# *OR
for num in arr_1d:
      print(num, end = " ")

# Iterating over a 2D array
arr_2d = np.array([[10, 20, 30], [40, 50, 60]])
for row in arr_2d:
    for num in row:
        print(num, end = " ")

# Iterating row by row 
for row in arr_2d: 
  print("Row:", row) 

# Iterating element by element 
for element in np.nditer(arr_2d): 
   print("Element:", element) 

# Mathematical Operations in NumPy:
# Element-wise Arithmetic Operations
# Creating two NumPy arrays 
a = np.array([3, 9, 11, 7]) 
b = np.array([15, 2, 1, 8]) 
print("Sum:", a + b)   
print("Sub:", a - b)  
print("Mul:", a * b) 
print("Div:", a / b)   
print("Exp:", a ** 2)  
print("Mod:", b % a)  

#  Universal Functions (ufuncs): It is a function that operates element-wise on arrays.
# Creating a sample array 
arr = np.arange(1, 11) 
print(arr)
# Applying universal functions 
print("Sq_rt:", np.sqrt(arr)) 
print()
print("e^x:", np.exp(arr)) 
print()
print("Natural_log:", np.log(arr))
print() 
print("Log_base_10:", np.log10(arr)) 
print()
print("Sin:", np.sin(arr)) 
print()
print("Cos:", np.cos(arr)) 
print()
print("Tan:", np.tan(arr)) 

# Statistical Functions : It is used to perform statistical operations on arrays.
# Creating a dataset 
data = np.array([10, 20, 30, 40, 50]) 
 
# Calculating key statistics 
print("Mean:", np.mean(data))
print("Median:", np.median(data))  
print("Standard Deviation:", np.std(data))  # Measures data spread 
print("Variance:", np.var(data))  # Square of standard deviation 
print("Minimum value:", np.min(data))   
print("Maximum value:", np.max(data))  
print("Index of Minimum Value:", np.argmin(data))  # Index of smallest value 
print("Index of Maximum Value:", np.argmax(data))  # Index of largest value 

# Creating two matrices
A = np.array([[11, 9], [8, 14]]) 
B = np.array([[6, 23], [19, 28]]) 

# Computing determinant 
print("Determinant of A:", np.linalg.det(A).round(4))
print("Determinant of B:", np.linalg.det(B).round(4))

# Computing inverse
print("Inverse of A:\n", np.linalg.inv(A).round(4))
print("Inverse of B:\n", np.linalg.inv(B).round(4))

# Eigenvalues and Eigenvectors 
# Computing eigenvalues and eigenvectors 
eigenvalues, eigenvectors = np.linalg.eig(A) 
print("Eigenvalues:", eigenvalues) 
print("Eigenvectors:\n", eigenvectors) 

# Cumulative Sum: It is the sum of all elements in an array, where each element is the sum of all previous elements.
arr = np.array([100, 200, 300, 400, 500])
s = np.sum(arr)
print("Sum of all elements:", s)
cumulative_sum = np.cumsum(arr)
print("Cumulative sum of elements:", cumulative_sum)

# Finding Unique Elements & Counting Occurrences 
arr = np.array([4, 4, 4, 2, 3, 1, 2, 3]) 
 
unique_elements, counts = np.unique(arr, return_counts=True) 
print("Unique elements:", unique_elements) 
print("Counts:", counts) 

# Sorting an Array 
arr = np.array([3, 1, 4, 1, 5, 9]) 

# Sorting in ascending order
print("Sorted array:", np.sort(arr)) 
print("Indices of sorted elements:", np.argsort(arr))

# Sorting in descending order
print("Sorted array:", np.sort(arr)[::-1]) 
print("Indices of sorted elements:", np.argsort(arr)[::-1])

# Finding Percentiles & Quantiles 
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) 
 
print("25th percentile:", np.percentile(data, 25)) 
print("50th percentile (median):", np.percentile(data, 50)) 
print("75th percentile:", np.percentile(data, 75)) 
print("90th percentile:", np.percentile(data, 90))

