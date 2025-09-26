import numpy as np

# Problem 3: Compute one element manually (row 0 × col 0)
A = np.array([[-1, 2, 3], [4, -5, 6], [7, 8, -9]])
B = np.array([[0, 2, 1], [0, 2, -8], [2, 9, -1]])

c00 = (A[0,0]*B[0,0]) + (A[0,1]*B[1,0]) + (A[0,2]*B[2,0])
print("C[0,0] =", c00)
