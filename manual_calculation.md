# Problem 1: Manual Matrix Product Calculation

We want to compute the product:

\[
C = A \times B
\]

where

\[
A =
\begin{bmatrix}
-1 & 2 & 3 \\
4 & -5 & 6 \\
7 & 8 & -9
\end{bmatrix}
,\quad
B =
\begin{bmatrix}
0 & 2 & 1 \\
0 & 2 & -8 \\
2 & 9 & -1
\end{bmatrix}
\]

---

## Step 1: Formula

Each element of \(C\) is obtained by:

\[
C[i, j] = (A[i,0] \times B[0,j]) + (A[i,1] \times B[1,j]) + (A[i,2] \times B[2,j])
\]

That is: **row of \(A\)** × **column of \(B\)**.

---

## Step 2: Full Calculations

### Row 0 of A × Columns of B
- \(C[0,0] = (-1 \times 0) + (2 \times 0) + (3 \times 2) = 0 + 0 + 6 = 6\)  
- \(C[0,1] = (-1 \times 2) + (2 \times 2) + (3 \times 9) = -2 + 4 + 27 = 29\)  
- \(C[0,2] = (-1 \times 1) + (2 \times -8) + (3 \times -1) = -1 -16 -3 = -20\)  

### Row 1 of A × Columns of B
- \(C[1,0] = (4 \times 0) + (-5 \times 0) + (6 \times 2) = 0 + 0 + 12 = 12\)  
- \(C[1,1] = (4 \times 2) + (-5 \times 2) + (6 \times 9) = 8 -10 + 54 = 52\)  
- \(C[1,2] = (4 \times 1) + (-5 \times -8) + (6 \times -1) = 4 + 40 - 6 = 38\)  

### Row 2 of A × Columns of B
- \(C[2,0] = (7 \times 0) + (8 \times 0) + (-9 \times 2) = 0 + 0 -18 = -18\)  
- \(C[2,1] = (7 \times 2) + (8 \times 2) + (-9 \times 9) = 14 + 16 -81 = -51\)  
- \(C[2,2] = (7 \times 1) + (8 \times -8) + (-9 \times -1) = 7 -64 + 9 = -48\)  

---

## Step 3: Final Result

\[
C =
\begin{bmatrix}
6 & 29 & -20 \\
12 & 52 & 38 \\
-18 & -51 & -48
\end{bmatrix}
\]