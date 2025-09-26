import numpy as np

# Problem 2: Matrix product using NumPy built-ins
A = np.array([[-1, 2, 3], [4, -5, 6], [7, 8, -9]])
B = np.array([[0, 2, 1], [0, 2, -8], [2, 9, -1]])

print("Using np.matmul:\n", np.matmul(A, B))
print("Using np.dot:\n", np.dot(A, B))
print("Using @ operator:\n", A @ B)
