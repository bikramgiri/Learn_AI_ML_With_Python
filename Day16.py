#  Day16:

import numpy as np 

# vector addition
v1 = np.array([1, 2]) 
v2 = np.array([3, 4])
v_sum = v1 + v2
print("Sum of vectors:", v_sum)

# scalar multiplication of a vector
s = 3
new_v = s * v1
print("Scaled vector:", new_v)

# dot product of vectors
dot_product = np.dot(v1, v2)
print("Dot product of vectors:", dot_product)

#  
v = np.array([1, 2, 3, 4,5, 8, 90, 100])
n_v = np.linalg.norm(v)
print(n_v)

# orthogonality and Projections 
v1 = np.array([55, -1, 3, 42])
v2 = np.array([2, 2, 2, 22])
is_ortho = (np.dot(v1, v2) == 0 )
print(is_ortho)

proj = (np.dot(v1, v2) / np.dot(v2, v2)) * v2
print(proj)

# Linear Combination
M = np.array([1, 2, 3], [3, 4, 4], [5, 6, 1])
c1, c2 = 1.5, 2
l_c = c1*M[0] + c2*M[2]
print(l_c)

# Linear Combination
v1 = np.array([1, 2, 3])
v2 = np.array([3, 4, 5])
M = np.stack([v1, v2], axis = 1)
r = np.linalg.matrix_rank(M)
is_independent = (r == M.shape[1])
if is_independent:
      print("The vectors are indenpendent.")
else:
      print("The vectors are denpendent.")


# Dimensionality Reduction: Example with PCA
from sklearn.decomposition import PCA
x = np.random.rand(5, 3) # -> 5 x 3 (R^3)
p = PCA(n_components = 2)
reduced = p.fit_transform(x)
print(reduced)
