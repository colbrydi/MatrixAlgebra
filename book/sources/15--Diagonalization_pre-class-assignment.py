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

# # 15 Pre-Class Assignment: Diagonalization and Powers

# ### Readings for this topic (Recommended in bold)
#  * [Heffron Chapter 5 II1-2 pg 388-396](http://joshua.smcvt.edu/linearalgebra/book.pdf)
#  * [**_Beezer Section SD pg 403-415_**](http://linear.ups.edu/download/fcla-3.50-tablet.pdf)
#

# ### Goals for today's pre-class assignment 
#
# 1. [Eigenvalues and eigenvectors review](#Eigenvalues_and_eigenvectors_review)
# 1. [Diagonalizable Matrix](#Diagonalizable_Matrix)
# 1. [Assignment wrap-up](#Assignment_wrap-up)

# ----
# <a name="Eigenvalues_and_eigenvectors_review"></a>
# ## 1. Eigenvalues and eigenvectors review
#
# **Definition**: A non-zero vector $x$ in $R^n$ is called an *eigenvector* of a $n\times n$ matrix $A$ if $Ax$ is a scalar multiple of $x$. If $Ax = \lambda x$, then $\lambda$ is called the *eigenvalue* of $A$ corresponding to $x$.

# ### Steps for finding the eigenvalues and eigenvectors
#
# We want to find $\lambda$ and non-zero vector $x$ such that $Ax=\lambda x$ for a $n\times n$ matrix. 
# 1. We introduce an identity matrix $I$ of $n\times n$. Then the equation becomes
# $$Ax = \lambda I x$$
# $$Ax-\lambda I x = 0$$
# $$(A-\lambda I)x = 0$$
# 2. This suggests that we want to find $\lambda$ such that $(A-\lambda I)x=0$ has a non-trivial solution. 
# It is equivalent to that the matrix $A-\lambda I$ is singular, i.e., has a determinant of $0$.
# $$|A-\lambda I|=0$$
# 3. The determinant is polynomial in $\lambda$ (called the characteristic polynomial of $A$) with degree $n$. We solve this equation (called the characteristic equation) for all possible $\lambda$ (eigenvalues).
# 4. After finding the eigenvalues, we substitute them back into 
# $$(A-\lambda I)x=0$$
# and find the eigenvectors $x$. 
#

# Let's calculate eigenvalues for the following matrix: 
#
# $$ A=\begin{bmatrix} 0 & 0 & -2 \\ 1 & 2 & 1 \\ 1 & 0 & 3 \end{bmatrix}$$

# #### Find eigenvalues
# Looking at the above recipe, let's solve the problem symbollically using `sympy`. First lets create a matrix $B$ such that:
#
# $$B = A-\lambda I$$

# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import sympy as sym
sym.init_printing()

# +
#Most sympy requires defeing the variables as "symbols"
#Once we do this we can use the variables in place of numbers
lam = sym.symbols('lambda')

A = sym.Matrix([[0, 0 ,-2], [1, 2, 1], [1, 0, 3]])
I = sym.eye(3)

B = A - lam*I

B
# -

# Now, per step 2, the determinate of $B$ must be zero. Note that `sympy` calculates the determinate symbollically as follows:

B.det()

# &#9989; **<font color=red>Do This:</font>**  Using the ```sympy.solve``` function on the determinate of $B$ to solve for ```lam``` ($\lambda$). Verify that the solution to the last question produces the same eigenvalues as above. 

# +
# Put your code to solve for det(B) = 0 here
# -

# &#9989; **<font color=red>Do This:</font>**  First, let's use the built in funciton ```eigenvals``` function in ```sympy``` to calculate the eigenvalues. Find out the meaning of the output.

# +
# Put your code here
# -

# Explain your output here.

# #### Find eigenvectors
# Now we know the eigenvalues, we can substitue them back into the equation to find the eigenvectors.  
# We solve this symbollically using `sympy`. First let's make a vector of our eigenvalues (from above):

eig = [1,2]

# Now (per step 4 above) we need to solve the equation $(A-\lambda I)x=0$. One way to do this in `sympy` is as follows:

# +
x1,x2,x3 = sym.symbols(['x_1','x_2','x_3'])

x = sym.Matrix([[x1],[x2],[x3]])
x
# -

for lam in eig:
    vec = sym.solve((A - lam*I)*x,x)
    print(vec)

# &#9989; **<font color=red>QUESTION:</font>**  Explain your output here. (Hint, you can also try the `rref` to find the solutions)

# Put your answer here

# &#9989; **<font color=red>Do This:</font>**  Next, let's use the ```eigenvects```  function in ```sympy``` to find three linear independent eigenvectors for the matrix $A$?

# +
# Put your answer to the above question here
# -

# &#9989; **<font color=red>QUESTION:</font>**  Compare this answer to the eigenvectors we calculated above. Does this answer make sense?  What does the syntax tell us? 

# Put your answer here

# &#9989; **<font color=red>DO THIS:</font>** Find the eigenvalues and eigenvectors of the following matrix:
# $$ A2=\begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}$$

# &#9989; **<font color=red>QUESTION:</font>**  What are the eigenvalues for the matrix $A2$?

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>**  What are the eigenvectors for the matrix $A2$?

# Put your answer to the above question here

# ----
# <a name="Diagonalizable_Matrix"></a>
# ## 2. Diagonalizable Matrix
#
# In class we will be using matrix diagonalization to solve some problems.  
#
# Matrix $A$ is diagonalizable if there exists a diagonal matrix $D$ that is similar similar to $A$:
#
# $$ D = C^{-1}AC$$
#
# If matrix $A$ has linearly independent eigenvectors ($v_1, \ldots v_n$) then $A$ is diagonalizable with the following solution:
#
# $$C = \left[ v_1^T, \ldots, v_n^T \right]$$
#
# In other words, each column of $C$ is a linearly independent eigenvector of $A$. The diagonal matrix $D$ is
#
# $$ D = 
# \left[
# \begin{matrix}
#     \lambda_1  & 0  & 0 \\
#     0   & \ddots & 0  \\
#     0   & 0 & \lambda_n 
# \end{matrix}
# \right] 
# $$
#
# In other-other words, $D$ consists of the corresponding eigenvalues.

# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import sympy as sym
sym.init_printing(use_unicode=True)

# &#9989; **<font color=red>DO THIS:</font>** Using ```numpy```, Diagonalize (i.e. calculate  C and D) the following matrix:

A = np.matrix([[5, -2, 2], [4, -3, 4], [4,-6,7]])
sym.Matrix(A)

# +
# Put your answer here

# +
from answercheck import checkanswer

checkanswer.matrix(D,'56821475223b52e0b6e751da444a1441');
# -

# &#9989; **<font color=red>DO THIS:</font>** Verify that $A$ is in fact Diagonalizable by calculating $D2 = C^{-1}AC$ and comparing it to your original $D$ using ```np.allclose```.

# +
#Put your verificaiton code here.
# -

np.allclose(D,D2)

# ### Diagonalization of Symmetric Matrices
#
# One special case is Symmetric Matrices.  It can be shown that symmetric Matrices are Diagonalizable and the resulting eigenvectors are not only linearly independent but also orthogonal.    Since this is true, the equation changes to: 
#
#
# $$ D = C^{T}AC$$
#
# &#9989; **<font color=red>QUESTION:</font>** Why do we care if $C$ is orthogonal?  What advantages does the above equation give us?

# Put your answer to the above question here.

# ----
#
# <a name="Assignment_wrap-up"></a>
# ## 3. Assignment wrap-up

# &#9989; **<font color=red>Assignment-Specific QUESTION:</font>** Why do we care if $C$ is orthogonal?  What advantages does the above equation give us?

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

# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
