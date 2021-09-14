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

# # 17 Pre-Class Assignment: Decompositions

# ### Readings for this topic (Recommended in bold)
#  * [**_Beezer Proof Technique DC pg 600-601_**](http://linear.ups.edu/download/fcla-3.50-tablet.pdf)
#

# ### Goals for today's pre-class assignment 
#
# 1. [Matrix Decomposition](#Matrix_Decompositions)
# 2. [Decompositions](#Decompositions)
# 4. [Assignment wrap-up](#Assignment_wrap-up)
#

# ----
# <a name="Matrix_Decompositions"></a>
# ## 1. Matrix Decomposition
#
# &#9989; **<font color=red>DO THIS:</font>** Watch the following video and answer the questions below.

from IPython.display import YouTubeVideo
YouTubeVideo("-_2he4J6Xxw",width=640,height=360, cc_load_policy=True)

# Consider the following code to calculate the $A = Q\Lambda Q^{-1}$ eivendecomposition. 

# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import sympy as sym
sym.init_printing(use_unicode=True)

# Here is our input matrix
A = np.matrix([[15,7,-7],[-1,1,1],[13,7,-5]])
sym.Matrix(A)

# Calculate eigenvalues and vectors using Numpy
e, Q = np.linalg.eig(A)
print(e)
sym.Matrix(Q)

#Turn eigenvalues into a diagonal matrix  (there is even a function for that!)
L = np.diag(e)
sym.Matrix(L)

# +
# Calculate A again from Q and L

A2 = Q*L*np.linalg.inv(Q)

sym.Matrix(A2)
# -

# &#9989; **<font color=red>DO THIS:</font>**  Using code, verify that A2 is the same as $A$.

# +
# Put your answer here
# -

# &#9989; **<font color=red>DO THIS:</font>**  Turn the above code into a function called `eigendecomp` which takes in a matrix A and returns Q and L.  

# +
# Put your code here
# -

# &#9989; **<font color=red>QUESTION:</font>** What other decompositions have we covered in the class so far? Make a list and write down a short description on why we use each decomposition.

# Put your answer to the above question here.

# ---
# <a name="Decompositions"></a>
#
# ## 2. Decompositions
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Diagonalization_as_rotation.gif" alt="image showing how a matris is just a change of basis ">
#
# Animiated Image from Wikipedia: https://wikipedia.org/
#
# In numerical linear algebra, we factorize matrices to facilitate efficient and/or accurate computations (they are also helpful in proofs). There are many possible **matrix decompositions**. Some, e.g., the eigendecomposition, require the matrix to be square, while others, e.g., the $QR$ factorization, exist for arbitrary matrices. Among all possible decompositions (also called *factorizations*), some common examples include:
#
# - **QR Factorization** from Gram-Schmidt orthogonization: 
#     - $A = QR$
#     - $Q$ has orthonormal columns and $R$ is a upper-triangular matrix 
#     - If there are zero rows in $R$, we can reduce the number of columns in $Q$
#     - Exists for arbitrary matrices 
# - **LU / LDU Decomposition** from Gauss Elimination: 
#     - $A = LU$ or $A = LDU$
#     - $L$ is lower-triangular, $U$ is upper-triangular, and $D$ is diagonal 
#     - Exists for all **square** matrices
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

# &#9989; **<font color=red>QUESTION:</font>** What decompositions have we covered in the class so far and how did we use them?

# **Your answer goes here**

# ----
#
# <a name="Assignment_wrap-up"></a>
# ## 3. Assignment wrap-up

# &#9989; **<font color=red>Assignment-Specific QUESTION:</font>** What other decompositions have we covered in the class so far?

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>**  Summarize what you did in this assignment.

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>**  What questions do you have, if any, about any of the topics discussed in this assignment after working through the jupyter notebook?

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>**  How well do you feel this assignment helped you to achieve a better understanding of the above mentioned topic(s)?

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>** What was the **most** challenging part of this assignment for you? 

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>** What was the **least** challenging part of this assignment for you? 

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>**  What kind of additional questions or support, if any, do you feel you need to have a better understanding of the content in this assignment?

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>**  Do you have any further questions or comments about this material, or anything else that's going on in class?

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>** Approximately how long did this pre-class assignment take?

# Put your answer to the above question here

# ----
#
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
