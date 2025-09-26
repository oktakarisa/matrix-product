import numpy as np

# Problem 6: Transpose and multiply

# Define matrices that cannot be multiplied directly
A = np.array([[1, 2, 3],
              [4, 5, 6]])   # Shape (2, 3)

B = np.array([[7, 8, 9],
              [10, 11, 12]])  # Shape (2, 3)

print("Original shapes: A =", A.shape, ", B =", B.shape)

# Try multiplying without transpose (should fail)
try:
    print("A @ B:\n", A @ B)
except ValueError as e:
    print("Error when trying A @ B:", e)

# Fix using transpose of B
print("\nNow transposing B...")
print("Shapes after transpose: A =", A.shape, ", B.T =", B.T.shape)
print("A @ B.T:\n", A @ B.T)