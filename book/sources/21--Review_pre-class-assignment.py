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

# # 21 Pre-Class Assignment: Solve Linear Systems of Equations

# ### Goals for today's pre-class assignment 
#
#
# 1. [Linear Systems](#Linear-Systems)
# 2. [Under Defined Systems](#Under-Defined-Systems)
# 3. [Invertible Systems](#Invertible-Systems)
# 4. [Overdefined systems](#Overdefined-systems)
# 5. [System Properties](#System-Properties)
# 6. [Assignment wrap up](#Assignment-wrap-up)
#
#

#
#
#
# ---
# <a name=Linear-Systems></a>
# ## 1. Linear Systems
#
#
#
#
#
# In this course, we learned how to represent linear systems which basically consists of equations added sums of multiple numbers in the form:
#
# $$b = a_1x_1+a_2x_2+a_3x_3 + \ldots a_mx_m$$
#
# Systems of linear equations are multiple equations of the above form with basically the same unknowns but different values of $a$ and $b$. 
#
# $$b_1 = a_{11}x_1+a_{12}x_2+a_{13}x_3 + \ldots a_{1n}x_n$$
# $$b_2 = a_{21}x_1+a_{22}x_2+a_{23}x_3 + \ldots a_{2n}x_n$$
# $$b_3 = a_{31}x_1+a_{32}x_2+a_{33}x_3 + \ldots a_{3n}x_n$$
# $$\vdots$$
# $$b_m = a_{m1}x_1+a_{m2}x_2+a_{m3}x_3 + \ldots a_{mn}x_n$$
#
# The above equations can be represented in matrix form as follows:
#
# $$ 
# \left[ 
# \begin{matrix}
#     b_1 \\ 
#     b_2 \\
#     b_3 \\
#     \vdots \\
#     b_m
#  \end{matrix}
# \right] 
# =
# \left[ 
# \begin{matrix}
#  a_{11} & a_{12} & a_{13} &   & a_{1n} \\ 
#  a_{21} & a_{22} & a_{23} &  \ldots & a_{2n} \\ 
#   a_{31} & a_{32} & a_{33} &   & a_{3n} \\ 
#   & \vdots &   & \ddots & \vdots \\ 
#  a_{m1} & a_{m2} & a_{m3} &   & a_{mn} 
# \end{matrix}
# \right] 
# \left[ 
# \begin{matrix}
#     x_1 \\ 
#     x_2 \\
#     x_3 \\
#     \vdots \\
#     x_n
# \end{matrix}
# \right] 
# $$
#
# Which can also be represented in "augmented" form as follows:
#
# $$ 
# \left[ 
# \begin{matrix}
#  a_{11} & a_{12} & a_{13} &   & a_{1n} \\ 
#  a_{21} & a_{22} & a_{23} &  \ldots & a_{2n} \\ 
#   a_{31} & a_{32} & a_{33} &   & a_{3n} \\ 
#   & \vdots &   & \ddots & \vdots \\ 
#  a_{m1} & a_{m2} & a_{m3} &   & a_{mn} 
# \end{matrix}
#  \, \middle\vert \,
# \begin{matrix}
#     b_1 \\ 
#     b_2 \\
#     b_3 \\
#     \vdots \\
#     b_m
# \end{matrix}
# \right] 
# $$

# The above systems can be modified into equivelent systems using combinations of the following operators. 
#
# 1. Multiply any row of a matrix by a constant
# 2. Add the contents of one row by another row.
# 3. Swap any two rows. 
#
# Often the 1st and 2nd operator can be combined where a row is multipled by a constanet and then added (or subtracted) from another row. 

# &#9989; **<font color=red>QUESTION:</font>**  Consider the matrix $A= \left[ 
# \begin{matrix} 1 & 3 \\ 0 & 2 \end{matrix}\right]$. What operators can you use to put the above equation into it's reduced row echelon form? 

# Put your answer to the above question here.

# ---
# <a name=Under-Defined-Systems></a>
# ## 2. Under Defined Systems
#
#
#
#
# An under-defined system is one that is non-invertible and the number of unknowns is more than the number of knowns. These system often have infinite numbers of possible solutions and solving them involves finding a set of simplified equations that represent all solutions. 
#
# Often the simplest way to solve an under-defined systems of equations is to extract the solution directly from the reduced row echelon form.  

# &#9989; **<font color=red>QUESTION:</font>**  What is the reduced row echelon form of the matrix $A= \left[ 
# \begin{matrix} 1 & 3 \\ 2 & 6 \end{matrix}\right]$.

# +
##ADD example of solving an underdefined system.
# -

# &#9989; **<font color=red>QUESTION:</font>**  What are the solutions to the above systems of equations if $b= \left[ 
# \begin{matrix} 10\\ 3 \end{matrix}\right]$?

# +
#put your answer to the above quesiton here.
# -

#
# ---
# <a name=Invertible-Systems></a>
# ## 3. Invertible Systems
#
# An invertible system has a square $A$ that is invertible such that all the following properties are true:
#
# 1. $ A^{-1}A = AA^{-1} = I $
# 1. $(A^{-1})^{-1} = A$
# 2. $(cA)^{-1} = \frac{1}{c}A^{-1}$
# 3. $(AB)^{-1} = B^{-1}A^{-1}$
# 4. $(A^n)^{-1} = (A^{-1})^n$
# 1. $(A^\top)^{-1} = (A^{-1})^\top$  here $A^\top$ is the transpose of the matrix $A$.

# Consider the following system of equations:
#
# $$\begin{bmatrix}5&-2&2 \\ 4 & -3 &4 \\ 4& -6 &7 \end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=\begin{bmatrix}1\\2\\3\end{bmatrix}$$
#
#

import numpy as np
import sympy as sym

A = np.matrix([[5, -2, 2], [4, -3, 4], [4,-6,7]])
b = np.matrix([[1],[2],[3]])
display(sym.Matrix(A))
display(sym.Matrix(b))

# **Iterative algorithms (Gauss-Seidel and Jacobian):** 
# + They may require many iterations
# + Gauss-Seidel is faster than Jacobian
# + They do not work for all square invertible systems. 

# **Non-iterative algorithms:** 
# + Gauss elimination (rref)
# + LU decomposition
# + Find the inverse of the matrix $A$ and $x= A^{-1}b$

# &#9989; **<font color=red>DO THIS:</font>** Pick at least two methods to solve the system of equations and compare them. 

# +
#put your answer here
# -

#
# ---
# <a name=Overdefined-systems></a>
# ## 4. Overdefined systems
#
#
#
# We also learned solutions to overdefined systems (more equations than unknowns) often do not exist. However, we can estimate a solution using Least Squares fit.  

# Consider the following system of equations:
#
# $$\begin{bmatrix}5&-2&2 \\ 4 & -3 &4 \\ 4& -6 &7 \\ 6 & 3 & -3\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=\begin{bmatrix}1\\2\\3\\-1\end{bmatrix}$$
#
# &#9989; **<font color=red>DO THIS:</font>** Solve the above using LSF. 
#

# +
#Put your answer to the above question here.
# -

#
#
# ---
# <a name=System-Properties></a>
# ## 5. System Properties
#
#
#
# The above methods for solving systems of linear equations is only part of the story. We also explored ways to understand properties of linear systems.  Properties such as rank, determinate, eigenvectors and eigenvalues all provide insight into the matrices that are at the core of the systems.  
#
# One problem is that as systems get really large the computational cost of finding a solution can also become large and intractable (i.e. difficult to solve).  We use our understanding of matrix properties and "decompositions" to transform systems into simpler forms so that solving the problem also becomes simple. 
#
# In class tomorrow we will review all of these concepts by looking at methods to solve linear systmes of the form $Ax=b$ using $QR$ decomposition.  When we solve for $Ax=b$ with QR decomposition. We have the following steps:
# + Find the $QR$ decomposition of $A$ such that:
#     + $R$ is square upper-triangular matrix
#     + The Columns of $Q$ are orthonormal
# + From $QRx=b$, we obtain $Rx =Q^\top b$ 
# + Solve for $x$ using back substitution.
#

# &#9989; **<font color=red>DO THIS:</font>** Search for a video describing the $QR$ decomposition of a matrix. Try to pick a video that you think does a good job in a short amount of time.  

# Put a link to the video you found here.

# ---
# <a name=Assignment-wrap-up></a>
# ## 6. Assignment wrap up

# &#9989; **<font color=red>Assignment-Specific QUESTION:</font>** What is the URL you found that describes how to do a QR decomposition. 

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
