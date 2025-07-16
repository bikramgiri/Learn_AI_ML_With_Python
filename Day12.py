#Day12: 
'''
NumPy Fundamentals :

Creating Numpy Arrays:
1. Creating a NumPy Array from a List 
2. Creating Multi-Dimensional Arrays 
3. Creating Special NumPy Arrays 
a) Creating an Array of Zeros and Ones
b) Creating an Identity Matrix
c) Creating an Array with a Range of Values and Evenly Spaced Values
d) Creating a Random Array 

Array Attributes
Array Indexing and Slicing 
1. Accessing Elements in a 1D and 2D Array 

'''

import numpy as np

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_3d)

# 3 x 3 matrix with all elements zero
zero_matrix = np.zeros((3, 3))
print(zero_matrix)

# 3 x 3 matrix with all elements one
one_matrix = np.ones((3, 3))
print(one_matrix)

# to create an identity matrix of size 5 x 5
identity_matrix = np.eye(5)
print(identity_matrix)

# we have to create array of first 50 numbers starting from 1
arr_1d = np.arange(1, 51)
#OR
arr_1d = np.arange(1, 51, 2)
print(arr_1d)

# print even number 1 to 100
even_numbers = np.arange(2, 101, 2)
print(even_numbers)

# we need an array having 5 values from 1 to 10 evenly spaced
evenly_spaced = np.linspace(1, 20, 5)
print(evenly_spaced)

# Creates a 4 x 4 matrix with all values ranging from 0 to 1
random_arr = np.random.rand(4, 4) # this will creates a 4 x 4 matrix with all values ranging from 0 to 1
print(random_arr)

# creates a 4 x 4 matrix with all values ranging from 1 to 10
random_arr = np.random.randint(1, 11, size =(3, 4)) 
print(random_arr)


#**Array Attributes:
arr = np.array([[10, 20, 30], [30, 40, 70], [3, 5, 7]], dtype="int16") # float > int, string > int
print(arr)
print(arr.shape)  # Returns the shape of the array
print(arr.ndim)   # Returns the number of dimensions of the array
print(arr.size)   # Returns the total number of elements in the array
print(arr.dtype)  # Returns the data type of the elements in the array
print(arr.itemsize)  # Returns the size in bytes of each element in the array
print(arr.nbytes)  # Returns the total number of bytes consumed by the elements of the


# Accessing Element in 1D Array
arr_1d = np.array([10, 20, 30, 40, 50])
print(arr_1d)
print(arr_1d[1:4])
print(arr_1d[::2])

# Accessing Element in 2D Array
arr_2d = np.array([[10, 20, 30],
                   [40, 50, 60], 
                   [70, 80, 90]])
print(arr_2d)
print(arr_2d[2, 2])
print(arr_2d[0, :])  # Accessing the first row
print(arr_2d[0:, 1])  # Accessing the first column from the second row onwards
print(arr_2d[:, 1])  # Accessing the second column
print(arr_2d[1:, 1:])  # Accessing the sub-array
print(arr_2d[0:2, 2])  # Accessing a specific sub-array
print(arr_2d[::2,0])  # Accessing a specific sub-array
print(arr_2d[1:, 1:])  # Accessing the sub-array from the second row and second column onwards
print(arr_2d[2, 1])  # Accessing the sub-array from the second row and second column onwards
print(arr_2d[1:3, 0:2])  # Accessing the sub-array from the second row and first two columns
print(arr_2d[:, 1])  # Accessing the sub-array from the second row and first two columns
print(arr_2d[1:3, 1:3])  # Accessing the diagnonal elements from the second row and first two columns
print("Diagonal elements:")
print(arr_2d.diagonal())  # Accessing the diagonal elements
anti = np.fliplr(arr_2d).diagonal()  # Flipping the array left to right
print(anti)  # Accessing the anti-diagonal elements
print(arr_2d[1,:])