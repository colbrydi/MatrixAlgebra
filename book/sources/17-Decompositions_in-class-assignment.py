# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

#

#
#

# ----
# # 17 In-Class Assignment: Decompositions and Gaussian Elimination

# ### Agenda for today's class (80 minutes)
#
#
# 1. [(20 minutes) Pre-class Review](#Pre-class_Review)
# 1. [(10 minutes) Decompositions](#Decompositions)
# 1. [(50 minutes) LU Decomposition](#LU)

# ---
# <a name="Pre-class_Review"></a>
#
# ## 1. Pre-Class Review
#
# * [17--Decompositions_pre-class-assignment](17--Decompositions_pre-class-assignment.ipynb)
#
#
#
#

# ---
# <a name="Decompositions"></a>
#
# ## 2. Decompositions
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Diagonalization_as_rotation.gif" alt="image showing how a matris is just a change of basis ">
#
# Animiated Image from Wikipedia: https://wikipedia.org/
#
# In numerical linear algebra, we factorize matrices to facilitate efficient and/or accurate computations. There are many possible **matrix decompositions**. Some, e.g., the eigendecomposition, require the matrix to be square, while others, e.g., the $QR$ factorization, exist for arbitrary matrices. Among all possible decompositions (also called *factorizations*), some common examples include:
#
# - **QR Factorization** from Gram-Schmidt orthogonization: 
#     - $A = QR$
#     - $Q$ has orthonormal columns and $R$ is a upper-triangular matrix 
#     - If there are zero rows in $R$, we can reduce the number of columns in $Q$
#     - Exists for arbitrary matrices
# - **LU / LDU Decomposition** from Gauss Elimination: 
#     - $A = LU$ or $A = LDU$
#     - $L$ is lower-triangular, $U$ is upper-triangular, and $D$ is diagonal 
#     - Exists for **square** matrices
#     - Is *related to Gaussian Elimination* 
# - **Cholesky Decomposition**: 
#     - $A = R^TR\quad (= LDL^T)$
#     - $R$ is upper-triangular 
#     - Factorization of $A$ into $R^TR$ requires $A$ be *symmetric* and *positive-definite*. The latter simply requires $x^{T}Ax > 0$ for every $x \in \mathbb{R}^n$. Note that $x^{T}Ax$ is always a scalar value (e.g., note that $x^TA = y^T$ for some vector $y\in\mathbb{R}^n$, and $y^Tx$ is the dot product between $x$ and $y$ and, hence, a real scalar).
# - **Schur Decomposition**:   
#     - $A = UTU^{T}$
#     - $U$ is orthogonal and $T$ is upper-triangular 
#     - Exists for every square matrix and says every such matrix, $A$, is unitarily equivalent to an upper-triangular matrix, $T$ (i.e., there exists an orthonomal basis with respect to which $A$ is upper-triangular)
#     - Eigenvalues on diagonal of $T$
# - **Singular Value Decomposition**: 
#     - $A = U\Sigma V^{T}$
#     - $U$ is orthogonal, $V$ is orthogonal, and $\Sigma$ is diagonal 
#     - Exists for arbitrary matrices
# - **Eigenvalue Decomposition**: 
#     - $A = X\Lambda X^{-1}$
#     - $X$ is invertible and $\Lambda$ is diagonal 
#     - Exists for square matrices with linearly independent columns (e.g., full rank)
#     - Also called the eigendecomposition

#
# ---
# <a name="LU"></a>
# ## 3. Focus on LU
#
# In this assignment we will create algorithms that factorize invertible matrices (i.e., square matrices with linearly independent columns), $A$, into the following decomposition (**note**: the terms *decomposition* and *factorization* are used interchangeably in literature):
#
# - LU Decomposition: $A = LU$
#
# Each matrix in these decompositions is the *matrix product* of <a href="https://en.wikipedia.org/wiki/Elementary_matrix">elementary matrices</a>. Recall that *an elementary matrix differs from the identity matrix (the square matrix with $1$s on the diagonal and $0$s elsewhere) by an elementary row operation*.
#  
# The use of these matrix decompositions in Numerical Linear Algebra is motivated by computational efficiency or reduction of *computational complexity* (recall "**Big-O notation**" and **counting the loops in your matrix multiplication algorithm**) and *numerical stability*. Solving our old friend $Ax = b$ by computing the inverse of $A$, denoted $A^{-1}$, and taking the matrix-vector product $A^{-1}b = x$ is computational resource intensive and numerically unstable, in general. If the $LU$ decomposition of $A$ exists, then it will be less costly and more stable to:
# 1. Solve $Ly = b$ for $y$ by *forward-substitution*; and then
# 2. Solve $Ux = y$ for $x$ by *backward-substitution*
#
# A final note to relate this assignment to the beginning of the course: The algorithms presented here are of a different class than the **Jacobi Algorithm** and **Gauss-Siedel Algorithm**. These are *iterative algorithms*. As you now know, this means that the algorithmic procedure is applied once, twice, and so on, until the output is within a desired tolerance, or until the process has been executed a given number of times (e.g., 100 iterations).

#
# ### Gaussian Elimination & LU Decomposition
#
# Recall that Gaussian elimination converts an arbitrary matrix, $A$, into its *row echelon form*. For our purposes, let's suppose that $A$ is a square matrix and, therefore, an $n\times n$ matrix. To simplify our tasks, let us further impose the condition that $A$ is invertible. Thus, the columns of $A$ are linearly independent. This means that Gaussian elimination will yield an ***upper-triangular*** *matrix*. Let us denote this matrix $U$ for ***upper-triangular***.
#
# If there were a function, $f$ that could take $A$ and output $U$, we could think of Gaussian Elimination as the following process:
#
# $$f(A)=U$$
#
# With this information, we may now rewrite our equation from above as:
#
# $$L^{-1}A = U$$
#
# You may have noticed the superscript in $L^{-1}$. This just says that $L^{-1}$ is the inverse of some matrix $L$. And for any invertible matrix, $L$, we have that the matrix products:
#
# $$L^{-1}L = LL^{-1} = I$$
#
# This is analogous to (for every real number $a\neq 0$): 
#
# $$a^{-1}\times a = a\times a^{-1} = 1$$
#
# Using the rules of matrix multiplication, verify the formula above by computing the following:
#
# $$
# L_{1}^{-1}L_{1} = 
# \left(
#     \begin{array}{*5{c}}
#          1 &  0 &  0 &  0 &  0 \\
#          -l_{21} &  1 &  0 &  0 &  0 \\
#          -l_{31} &  0 &  1 &  0 &  0 \\
#          -l_{41} &  0 &  0 &  1 &  0 \\
#          -l_{51} &  0 &  0 &  0 &  1 \\
#       \end{array}
#   \right) \left(
#     \begin{array}{*5{c}}
#          1 &  0 &  0 &  0 &  0 \\
#          l_{21} &  1 &  0 &  0 &  0 \\
#          l_{31} &  0 &  1 &  0 &  0 \\
#          l_{41} &  0 &  0 &  1 &  0 \\
#          l_{51} &  0 &  0 &  0 &  1 \\
#       \end{array}
#   \right)
# = 
# \left(
#     \begin{array}{*5{c}}
#          1 &  0 &  0 &  0 &  0 \\
#          0 &  1 &  0 &  0 &  0 \\
#          0 &  0 &  1 &  0 &  0 \\
#          0 &  0 &  0 &  1 &  0 \\
#          0 &  0 &  0 &  0 &  1 \\
#       \end{array}
#   \right)
# = I
# $$
#
# $$
# L_{2}^{-1}L_{2} = 
# \left(
#     \begin{array}{*5{c}}
#          1 &  0 &  0 &  0 &  0 \\
#          0 &  1 &  0 &  0 &  0 \\
#          0 &  -l_{32} &  1 &  0 &  0 \\
#          0 &  -l_{42} &  0 &  1 &  0 \\
#          0 &  -l_{52} &  0 &  0 &  1 \\
#       \end{array}
#   \right) \left(
#     \begin{array}{*5{c}}
#          1 &  0 &  0 &  0 &  0 \\
#          0 &  1 &  0 &  0 &  0 \\
#          0 &  l_{32} &  1 &  0 &  0 \\
#          0 &  l_{42} &  0 &  1 &  0 \\
#          0 &  l_{52} &  0 &  0 &  1 \\
#       \end{array}
#   \right)
# = 
# \left(
#     \begin{array}{*5{c}}
#          1 &  0 &  0 &  0 &  0 \\
#          0 &  1 &  0 &  0 &  0 \\
#          0 &  0 &  1 &  0 &  0 \\
#          0 &  0 &  0 &  1 &  0 \\
#          0 &  0 &  0 &  0 &  1 \\
#       \end{array}
#   \right)
# = I
# $$
#
# $$
# L_{4}^{-1}L_{4} = 
# \left(
#     \begin{array}{*5{c}}
#          1 &  0 &  0 &  0 &  0 \\
#          0 &  1 &  0 &  0 &  0 \\
#          0 &  0 &  1 &  0 &  0 \\
#          0 &  0 &  0 &  1 &  0 \\
#          0 &  0 &  0 &  -l_{54} &  1 \\
#       \end{array}
#   \right) \left(
#     \begin{array}{*5{c}}
#          1 &  0 &  0 &  0 &  0 \\
#          0 &  1 &  0 &  0 &  0 \\
#          0 &  0 &  1 &  0 &  0 \\
#          0 &  0 &  0 &  1 &  0 \\
#          0 &  0 &  0 &  l_{54} &  1 \\
#       \end{array}
#   \right)
# = 
# \left(
#     \begin{array}{*5{c}}
#          1 &  0 &  0 &  0 &  0 \\
#          0 &  1 &  0 &  0 &  0 \\
#          0 &  0 &  1 &  0 &  0 \\
#          0 &  0 &  0 &  1 &  0 \\
#          0 &  0 &  0 &  0 &  1 \\
#       \end{array}
#   \right)
# = I
# $$
#
# To understand $L^{-1}$ more deeply, let's turn our attention back to Gaussian elimination for a moment. Take as a given that, for a "sufficiently nice" $n\times n$ matrix $A$, the matrix $L^{-1}$ that takes $A$ to its ***upper-triangular*** or ***row echelon form***, $U$, has the structure:
#
# $$L^{-1} = L_{n-1}L_{n-2}...L_{2}L_{1}$$
#
# Each of the $L_{i}$s above is an elementary matrix that zeros out the subdiagonal entries of the $i^{th}$ column of $A$. This is **the $i^{th}$ step of** ***Gaussian Elimination*** **applied to** ***the entire $i^{th}$ column of A below the $i^{th}$ diagonal element***.  
#
# Let's show this by computation of $L_i$ for a "nice" matrix $A$.

# +
## Import all necessary packages
# %matplotlib inline
import scipy.sparse as sparse #this helps to speed up the algorithms, but you will not use it. 
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
sym.init_printing(use_unicode=True)

## These will allow us to see a cool simulation of the Heat Equation problem (if we compute our answers correctly!)
from matplotlib import animation, rc
from IPython.display import HTML
# -

# ### Gaussian Elimination by Elementary Matrices, $L_i$
#
# Let $A$ be the following matrix:
#
# $$A = 
# \begin{bmatrix}
#     2 &  1 &  1 &  0 \\
#     4 &  3 &  3 &  1 \\
#     8 &  7 &  9 &  5 \\
#     6 &  7 &  9 &  8 \\
# \end{bmatrix}
# $$
#
# &#9989; **<font color=red>DO THIS:</font>** Create a $4 \times 4$ **unit lower-triangular** matrix, $L_1$ that eliminates all of the subdiagonal entries of the first column of $A$. Display the matrix $L_1$ using SymPy.

A = np.matrix([[2,1,1,0],[4,3,3,1],[8,7,9,5],[6,7,9,8]]) # Here is A for your convenience
As = sym.Matrix(A)
As

## Type your answer here ##
L1 = np.matrix([[1,,,],[,1,,],[,,1,],[,,,1]])

# We should now have the following:
#
# $$L_{1}A = A^{(1)} =
# \begin{bmatrix}
#     2 &  1 &  1 &  0 \\
#     0 &  u_{22} &  u_{23} &  u_{24} \\
#     0 &  x &  x &  x \\
#     0 &  x &  x &  x \\
# \end{bmatrix}
# =
# \begin{bmatrix}
#     u_{11} &  u_{12} &  u_{13} &  u_{14} \\
#     0 &  u_{22} &  u_{23} &  u_{24} \\
#     0 &  x &  x &  x \\
#     0 &  x &  x &  x \\
# \end{bmatrix}
# $$
#
# Since our first row remained unchanged, we know that our $u_{1i}$ (the first row entries of $U$) are now determined. Similarly, we have that the $u_{2i}$ (the second row entries of $U$) are determined as well. The $x$ elements are elements that have changed, but are not yet in their final form.  **Note**: Your $u_{ij}$ will be whole, or integer ($\mathbb{Z}$), numbers. 
#
# &#9989; **<font color=red>DO THIS:</font>** Left-multiply $A$ by $L_1$ to confirm that all of the subdiagonal entries of the first column of $A^{(1)}$ are zero. Display the result via SymPy.

# # Type your answer here ##


# Our next step will be to eliminate all nonzero entries from the second column of $A^{(1)} = L_{1}A$ by left multiplication of $L_{2}$. This should yield: 
#
# $$\begin{align}A^{(2)} &= L_{2}A^{(1)} \\
# &= L_{2}L_{1}A \\
# &=
# \begin{bmatrix}
#     u_{11} &  u_{12} &  u_{13} &  u_{14} \\
#     0 &  u_{22} &  u_{23} &  u_{24} \\
#     0 &  0 &  u_{33} &  u_{34} \\
#     0 &  0 &  x &  x \\
# \end{bmatrix}
# \end{align}
# $$
#
# &#9989; **<font color=red>DO THIS:</font>** Create a $4 \times 4$ **unit lower-triangular** matrix, $L_2$ that eliminates all of the subdiagonal entries of the second column of $A^{(1)}$ yielding $A^{(2)}$ as above. Display the matrix $L_2$ using SymPy.

## Type your answer here ##
L2 = np.matrix([[1,,,],[,1,,],[,,1,],[,,,1]]) # for your convenience

# &#9989; **<font color=red>DO THIS:</font>** Left-multiply $A^{(1)}$ by $L_2$ to confirm that all of the subdiagonal entries of column 2 of $A^{(2)}$ are zero. Display the result via SymPy. **Note**: Your $u_{ij}$ will be whole, or Integer ($\mathbb{Z}$), numbers. 

# # Type your answer here ##


# We should now have:
#
# $$
# \begin{align}A^{(2)} &= L_{2}A^{(1)} \\
# &= L_{2}L_{1}A \\
# &=
# \begin{bmatrix}
#     u_{11} &  u_{12} &  u_{13} &  u_{14} \\
#     0 &  u_{22} &  u_{23} &  u_{24} \\
#     0 &  0 &  u_{33} &  u_{34} \\
#     0 &  0 &  x &  x \\
# \end{bmatrix}
# \end{align}
# $$
#
# We now want to build the final matrix $L_{3}$ that will take our matrix $A^{(2)}$ to ***upper-triangular*** **form**. So, let's do that!
#
# &#9989; **<font color=red>DO THIS:</font>** Create a $4 \times 4$ **unit lower-triangular** matrix, $L_3$ that eliminates all of the subdiagonal entries of the third column of $A^{(2)}$ yielding: 
#
# $$
# \begin{align}A^{(3)} &= L_{3}A^{(2)} \\ 
# &= L_{3}L_{2}A^{(1)} \\
# &= L_{3}L_{2}L_{1}A \\
# &= U
# \end{align}
# $$. 
#
# Display the matrix $L_3$ using SymPy.

## Type your answer here ##
L3 = np.matrix([[1,,,],[,1,,],[,,1,],[,,,1]]) # for your convenience

# &#9989; **<font color=red>DO THIS:</font>** Left-multiply $A^{(2)}$ by $L_3$ to confirm that all of the subdiagonal entries of column 3 of $A^{(3)}$ are zero. Display the result via SymPy. **Note**: Your $u_{ij}$ will be whole, or integer ($\mathbb{Z}$), numbers. You should now notice that $A^{(3)} = U$ is in **row echelon form**, and, hence, $U$ is an **upper-triangular matrix** with $0$s below the diagonal!

# # Type your answer here ##


# ### Congratulations! 
#
# You have just decomposed your first matrix via the process below (and should now have a matrix, $U$, that looks like the one below):
#
# $$
# \begin{align}L^{-1}A &= L_{3}L_{2}L_{1}A \\
# &= L_{3}L_{2}A^{(1)} \\
# &= L_{3}A^{(2)} \\
# &= A^{(3)} \\
# &= U \\
# &=
# \begin{bmatrix}
#     2 & 1 & 1 & 0 \\
#     0 & 1 & 1 & 1 \\
#     0 & 0 & 2 & 2 \\
#     0 & 0 & 0 & 2
# \end{bmatrix}
# \end{align}
# $$

# &#9989; **<font color=red>DO THIS:</font>**
#
# Finally, let's explicitly generate the matrices $L^{-1}$ and $L$. Then, display them using SymPy.
#
# It will be helpful to use the following:
#
# $$\begin{align}L^{-1} &= L_{n-1}L_{n-2}...L_{2}L_{1}\end{align}$$
# and
# $$\begin{align}L &= (L^{-1})^{-1} \\
# &= (L_{n-1}L_{n-2}...L_{2}L_{1})^{-1} \\
# &= L_{1}^{-1}L_{2}^{-1}...L_{n-2}^{-1}L_{n-1}^{-1}
# \end{align}
# $$
#
# If you're stuck, refer to the paragraph at the beginning of this section for the explicit formula. Recall: $L^{-1}L = LL^{-1} = I$.

# # Type your answer here ##


# &#9989; **<font color=red>DO THIS:</font>** Look at all the matrices $L_i$ and see the connections between the final $L$. 

print(L1)
print(L2)
print(L3)
print(L)

# For our last bit of LU decomposition fun, let's confirm that your matrices $L$ and $U$ fulfill the equality:
#
# $$A = LU$$
#
# Indeed, there is a function in SymPy that will compute the LU decomposition for us.
#
# &#9989; **<font color=red>DO THIS:</font>** Run the following function and print its outputs: 
#
# $$\texttt{L_actual, U_actual, _ = As.LUdecomposition()}$$
#
# Then, compute:
#
# $$\texttt{L_actual*U_actual - As}$$
#
# and confirm that it outputs the zero matrix.

# # Type your answer here ##


# ### General LU Decomposition Algorithm 
#
# &#9989; **<font color=red>DO THIS:</font>**  Using the scaffolded code below, complete the LU decomposition algorithm. (It may be helpful to test your code on the matrix $A$ from above.)

# +
## Type your answer here ##
C = np.matrix([[2,1,1,0],[4,3,3,1],[8,7,9,5],[6,7,9,8]]) # to test

def LU_decomp(B):
    n = len(B)
    U = B.copy()
    L = np.identity(n)
    for k in np.arange(0,n-1):
        for j in np.arange(k+1,n):
            L[j,k] =
            U[j,k:n] = U[,:] - L[,]*U[,:]
    return np.mat(L), np.mat(U)

L1,U1 = LU_dec(C) # syntax for returning matrices
np.linalg.norm(L1*U1 - A) # Test: should return 0


# -

# ### Solve $Ax=b$ via LU Decomposition
#
# You may wish to refer to the introduction of this assignment for a general overview of how to use LU Decomposition to solve $Ax = b$.
#
# &#9989; **<font color=red>DO THIS:</font>**  Using the scaffolded code below, complete the LU solver algorithm. The algorithm should solve $Ly = b$ for $y$ via Forward-Substitution and then $Ux=y$ for $x$ by Backward-Substitution. (It may be helpful to test your code on a matrix $A$ and vector $b$ from homework 1 or another source.)

## Type your answer here ##
def LU_Axb_solve(A,b):
    L,U = LU_decomp(A)
    n = len(A)
    # Forward-Substitution: Ly = b for y
    y = np.zeros((,))
    for i in np.arange(0,n):
        y[i] = b[i].copy()
        for j in np.arange(0,i):
            y[] = y[] - L[,]*y[]
       
    # Backward-Substitution: Ux = y for x
    x = np.zeros((n,1))
    for i in np.arange(n-1,-1,-1):
        x[] = y[].copy()
        for j in np.arange(n-1,i,-1):
            x[] = x[] - U[,]*x[]
        x[] = x[]/U[,]
    
    return np.mat(x)


# ----
#
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
