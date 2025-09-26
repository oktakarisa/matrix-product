import numpy as np

# Problem 5: Error checking
def safe_matrix_multiply(A, B):
    if A.shape[1] != B.shape[0]:
        print("Error: Cannot multiply. Columns of A must equal rows of B.")
        return None
    
    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape
    C = np.zeros((rows_A, cols_B), dtype=int)
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i, j] += A[i, k] * B[k, j]
    return C

if __name__ == "__main__":
    D = np.array([[-1, 2, 3], [4, -5, 6]])
    E = np.array([[-9, 8, 7], [6, -5, 4]])
    print("Trying invalid multiplication:")
    print(safe_matrix_multiply(D, E))
