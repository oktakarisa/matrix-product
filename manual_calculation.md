# Problem 1: Manual Matrix Product Calculation

We want to compute the product:

C = A × B

where

```python
A = [
  [-1,  2,  3],
  [ 4, -5,  6],
  [ 7,  8, -9]
]

B = [
  [ 0,  2,  1],
  [ 0,  2, -8],
  [ 2,  9, -1]
]

Step 1: Formula

Each element of C is obtained by:

C[i, j] = (A[i,0] * B[0,j]) + (A[i,1] * B[1,j]) + (A[i,2] * B[2,j])


That is: row of A × column of B.

Step 2: Full Calculations
Row 0 of A × Columns of B
C[0,0] = (-1*0) + (2*0) + (3*2)   = 6
C[0,1] = (-1*2) + (2*2) + (3*9)   = 29
C[0,2] = (-1*1) + (2*-8) + (3*-1) = -20

Row 1 of A × Columns of B
C[1,0] = (4*0)  + (-5*0)  + (6*2)   = 12
C[1,1] = (4*2)  + (-5*2)  + (6*9)   = 52
C[1,2] = (4*1)  + (-5*-8) + (6*-1)  = 38

Row 2 of A × Columns of B
C[2,0] = (7*0)  + (8*0)  + (-9*2)   = -18
C[2,1] = (7*2)  + (8*2)  + (-9*9)   = -51
C[2,2] = (7*1)  + (8*-8) + (-9*-1)  = -48

Step 3: Final Result
C = [
  [   6,  29, -20],
  [  12,  52,  38],
  [ -18, -51, -48]
]