# NumPy Arrays are either Vectors or Matrices
# Vectors are strictly 1-d arrays and matrices are 2-d, but
# matrices can still only have one row or one column

import numpy as np

# Vector
my_list = [1,2,3]
arr = np.array(my_list)

# Matrices
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
np.array(my_mat)

# numpy creating Arrays
np.arange(0,10)


np.zeros(3)
np.ones(5)

# Matrix r x c
np.zeros((5,5))

# range 1st & 2nd arg
# third is number of points desired
np.linspace(0,5,10)
