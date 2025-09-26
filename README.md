# Matrix Product Assignment

---

### **Purpose**
- Practice with **NumPy** for matrix operations.  
- Deepen understanding of **matrix multiplication**.  
- Learn to implement multiplication **by hand, with NumPy, and from scratch**.  
- Handle **dimension errors** and use **transpose** to fix them.  

---

### **Problem Description**
- In linear algebra and machine learning, the **matrix product** is fundamental.  
- Here, we:  
  - Calculate matrix products manually,  
  - Use NumPy's built-in methods,  
  - Write a scratch implementation,  
  - Handle invalid multiplications,  
  - And apply transposition to make operations possible.  

---

## Assignments

### **[Problem 1] Manual Calculation**
Multiply the two matrices:

```
A = [[-1,  2,  3],
     [ 4, -5,  6],
     [ 7,  8, -9]]

B = [[ 0,  2,  1],
     [ 0,  2, -8],
     [ 2,  9, -1]]
```

Step through calculations in **Markdown explanation**.  
**Output:** Manual result matches later NumPy and scratch implementations.

---

### **[Problem 2] NumPy Matrix Product**
Compute A × B using:
- `np.matmul()`
- `np.dot()`
- `@` operator

**Output:** Identical results from all three methods.

---

### **[Problem 3] Single Element Calculation**
Compute element C[0,0] manually:
```
c₀₀ = a₀₀×b₀₀ + a₀₁×b₁₀ + a₀₂×b₂₀
```
Implement in Python without `matmul`/`dot`.  
**Output:** `C[0,0] = 6`

---

### **[Problem 4] Scratch Implementation**
Write a function to compute the **full matrix product** from scratch using nested loops.  
**Output:** 3×3 result matches NumPy's calculation.

---

### **[Problem 5] Invalid Multiplication Handling**
Example with:
```
D = [[-1,  2,  3],
     [ 4, -5,  6]]

E = [[-9,  8,  7],
     [ 6, -5,  4]]
```
Detect mismatch and show a **clear error message**.  
**Output:** `"Error: Cannot multiply. Columns of A must equal rows of B."`

---

### **[Problem 6] Transposition**
- Start with two incompatible matrices
- Show multiplication fails
- Fix by transposing one matrix (`B.T`)

**Output:** Valid multiplication result after transpose.

---

### **Tools Used**
- Python  
- NumPy  

---

### **How to Run**
1. Clone the repository or download the files
2. Navigate into the project directory
3. Run all problems at once using:
   ```bash
   python main.py
   ```

---

## Author
**Assignment:** Dummy Data Assignment  
**Name:** Victor Karisa  
**Date:** 25/09/2025