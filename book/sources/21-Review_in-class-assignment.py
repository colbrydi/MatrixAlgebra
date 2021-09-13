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

# # 21 In-Class Assignment: Solve Linear Systems of Equations using QR Decomposition
#
# <img alt="Image of a multi-headed Hydra. Designed to represent parallel codes" src="https://upload.wikimedia.org/wikipedia/commons/2/24/Hydra1.gif">
#
# Image From: https://en.wikipedia.org/wiki/Hydra

# ### Agenda for today's class (80 minutes)
#
# </p>
#
# 1. [(20 minutes) Pre-class_Review](#Pre-class_Review)
# 2. [(20 minutes) Solve Linear Systems](#Solve_Linear_Systems)
# 3. [(30 minutes) Overdetermined Systems](#Overdetermined_Systems)
# 4. [(30 minutes) Underdetermined Systems](#Underdetermined_Systemss)

import numpy as np
import sympy as sym

# In this assignment, we try to solve the linear systems $Ax  =  b$ in three different categories. 
# + $A$ is a square matrix. Unique solution when $A$ is invertible
# + overdetermined (more equations than unknowns): If $A$ has full column rank, the system has an unique solution when $b$ is in the column space of $A$, otherwise no solution. 
# + underdetermined (more unknowns than equations): If $A$ has full row rank, there are infinite many solutions. 

# ---
# <a name="Pre-class_Review"></a>
#
# ## 1. Pre-Class Review
#
# * [21--Review_pre-class-assignment.ipynb](21--Review_pre-class-assignment.ipynb)

# ----
# <a name="Solve_Linear_Systems"></a>
# ## 2. Solve Linear Systems
#
# When we have the same number of equations as unknowns, we have the following system 
# $$Ax= b$$
# with a squre matrix $A$. 
# In this section, we assume that the matrix $A$ has full rank. That is the system has an unique solution. We talked about many ways to solve this system of equations. Some examples are:
#
# + Jacobian iteration/ Gauss-Seidel iteration
# + $x = A^{-1} b$
# + Gaussian elimination
# + LU decomposition
#
# In this assignment, we will show that we can solve it by QR decomposion. 

# Consider the following system of equations:
#
# $$\begin{bmatrix}5&-2&2 \\ 4 & -3 &4 \\ 4& -6 &7 \end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=\begin{bmatrix}1\\2\\3\end{bmatrix}$$
#
#

A = np.matrix([[5, -2, 2], [4, -3, 4], [4,-6,7]])
b = np.matrix([[1],[2],[3]])
display(sym.Matrix(A))
display(sym.Matrix(b))


# **Back substitution.** Let's first implement the back substitution in Python.  The back substitution function `back_subst` solves the system 
# $$R x = b$$
# where $R$ is an upper-triangular matrix. 
#
# When we solve for $x$, we start with $x_n$: 
# $$x_n = {b_n\over R_{n,n}}$$
# Then we solve for $x_{n-1}$ as 
# $$x_{n-1} = {b_{n-1}-R_{n-1,n}x_n\over R_{n-1,n-1}}$$
# $$x_{n-2} = {b_{n-2}-R_{n-2,n-1}x_{n-1}-R_{n-2,n}x_n\over R_{n-2,n-2}}$$
# Then we can find $x_{n-2},\cdots,x_1$.
# We can solve for all components of $x$ in the reserved order. So this is call back substitution.
#

# &#9989; **<font color=red>DO THIS:</font>**  Complete the following code for back substitution.

def back_subst(R,b):
    n = R.shape[0]; x = np.zeros(n);
    for i in reversed(range(n)):
        x[i] = b[i]
        for j in range(i+1,n):            
## Your code starts ##            
            x[i] =   # Complet this line of code.
## Your code ends ##            
        x[i] = x[i]/R[i,i]
    return np.matrix(x).T


#

# &#9989; **<font color=red>DO THIS:</font>**  When we solve for $Ax=b$ with QR decomposition. We have the following steps:
# + Find the QR decomposition of $A$
# + From $QRx=b$, we obtain $Rx =Q^\top b$ 
# + Solve for $x$ using back substitution.
#
# Use these steps to solve $Ax=b$ with the given $A$ and $b$. Compare the result with `np.linalg.solve`.

## Your code starts ##
x =  
## Your code ends ##
print(type(x))   # x is a column vector in the np.matrix type
np.allclose(x, np.linalg.solve(A,b))

# ----
# <a name="Overdetermined_Systems"></a>
# ## 3. Overdetermined Systems
#
# When we have more equations than unknowns, we have the overdetermined system 
# $$Ax\approx b$$
# In this assignment, we assume that the matrix $A$ has full column rank. Therefore, the system may not be feasible, i.e., we can not find $x$ such that $Ax=b$. Then we want to find the $x$ to minimize $\|Ax-b\|^2$, which is the least squares problem. We mentioned in previous assignments that we can solve this least squares problem by finding the left inverse of the matrix $A$. That is 
# $$x=(A^\top A)^{-1}A^\top b$$
#
# In this assignment, we show that we can solve it by QR decomposion. 

# Consider the following system of equations:
#
# $$\begin{bmatrix}5&-2&2 \\ 4 & -3 &4 \\ 4& -6 &7 \\ 6 & 3 & -3\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=\begin{bmatrix}1\\2\\3\\-1\end{bmatrix}$$
#
# &#9989; **<font color=red>DO THIS:</font>** We solve the least squares problem in the following steps
#
# + Find the QR decomposition of the matrix $A$ such that $R$ is a square upper-triangular matrix. ($Q$ is not a square matrix any more) 
# + Use the `back_subst` function we defined before to solve $Rx = Q^\top b$

A = np.matrix([[5, -2, 2], [4, -3, 4], [4,-6,7], [6,3,-3]])
b = np.matrix([[1],[2],[3],[-1]])
display(sym.Matrix(A))
display(sym.Matrix(b))

## Your code starts ##
x =  
## Your code ends ##
print(type(x))   # x is a column vector in the np.matrix type
print(x)

# We can not use the `np.linalg.solve` because the matrix $A$ is not a square matrix (you can try if you do not believe it). However, we can use the `np.linalg.lstsq` function to find the least squares solution to minimize $\|Ax-b\|^2$. The next cell compares the result from `lstsq` and our result from the QR decomposition. (If everything is correct, you will expect a `True` result.)

np.allclose(x, np.linalg.lstsq(A,b)[0])

# &#9989; **<font color=red>DO THIS:</font>** Explain why we can use the QR decomposition to solve the least squares problem. 

# Put Your Answer Here

# ----
# <a name="Underdetermined_Systemss"></a>
# ## 4. Underdetermined Systems
#
# When we have more unknowns than equations, we have the underdeterminated system 
# $$Ax= b$$
# In this assignment, we assume that the matrix $A$ has full row rank. This system has infinite many solution, i.e., we can not find an unique $x$ such that $Ax=b$. Then we want to find the smallest $x$ (by smallest, we mean the smallest $\|x\|^2$) such that $Ax=b$, which is also the least squares problem. 
#
# In this assignment, we show that we can also solve it by QR decomposion. 

# Consider the following system of equations:
#
# $$\begin{bmatrix}5&-2&2 & 1 \\ 4 & -3 &4 &2  \\ 4& -6 &7  & 4\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\\x_4\end{bmatrix}=\begin{bmatrix}1\\2\\3\end{bmatrix}$$
#
# &#9989; **<font color=red>DO THIS:</font>** We solve the least squares problem in the following steps
#
# + Find the QR decomposition of the matrix $A^\top$ such that $R$ is a square upper-triangular matrix. 
# + Use the `forward_subst` function defined below to solve $x = Q (R^\top)^{-1}b$

A = np.matrix([[5, -2, 2, 1], [4, -3, 4, 2], [4,-6,7, 4]])
b = np.matrix([[1],[2],[3]])
display(sym.Matrix(A))
display(sym.Matrix(b))


def forward_subst(L,b):  # This function solves $L x= b$ when $L$ is the lower-trigular matrix
    n = L.shape[0]; x = np.zeros(n);
    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] = x[i] - L[i,j]*x[j]  
        x[i] = x[i]/L[i,i]
    return np.matrix(x).T


## Your code starts ##
x =  
## Your code ends ##
print(type(x))   # x is a column vector in the np.matrix type
print(x)

# We can not use the `np.linalg.solve` because the matrix $A$ is not a square matrix. However, we can use the `np.linalg.lstsq` function to find the least squares solution to minimize $\|Ax-b\|^2$ with underdeterminated systems. The next cell compares the result from `lstsq` and our result from the QR decomposition. (If everything is correct, you will expect a `True` result.)

np.allclose(x, np.linalg.lstsq(A,b)[0])

# &#9989; **<font color=red>DO THIS:</font>** Explain why we can use the QR decomposition to solve the least squares problem. (HINT: you may need the orhogonal decomposition to the four fundamental spaces of $Q$.) 

# Put Your Answer Here

# ----
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
