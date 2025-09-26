import numpy as np

# Problem 4: Full scratch implementation
def matrix_multiply(A, B):
    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape
    
    # Initialize result with zeros
    C = np.zeros((rows_A, cols_B), dtype=int)
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i, j] += A[i, k] * B[k, j]
    return C

if __name__ == "__main__":
    A = np.array([[-1, 2, 3], [4, -5, 6], [7, 8, -9]])
    B = np.array([[0, 2, 1], [0, 2, -8], [2, 9, -1]])
    print("Result from scratch function:\n", matrix_multiply(A, B))
