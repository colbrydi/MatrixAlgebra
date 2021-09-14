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

# # 14 In-Class Assignment: Fundamental Spaces
#
# <img alt="Classic picture of the four fundamental spaces. Please see text for detailed description." src="https://kevinbinz.files.wordpress.com/2017/02/linear-algebra-fundamental-space-interpretation-6.png" width="100%">
#
# Image from: https://kevinbinz.com/2017/02/20/linear-algebra/
#
#     

# ### Agenda for today's class (80 minutes)
#
# 1. [(20 minutes) Pre-class assignment review](#Pre-class_assignment_review)
# 1. [(20 minutes) Four Fundamental Spaces](#Four_Fundamental_Subspaces)
# 1. [(20 minutes) Practice Example](#Practice_Example)

# ---
# <a name="Pre-class_assignment_review"></a>
#
# ## 1. Pre-class assignment review

# * [14--Fundamental_Spaces_pre-class-assignment.ipynb](14--Fundamental_Spaces_pre-class-assignment.ipynb)

# ---
# <a name="Four_Fundamental_Subspaces"></a>
# ## 2. Four Fundamental Subspaces

# ### The four fundamental subspaces
#
# * Columnspace, $\mathcal{C}(A)$
# * Nullspace, $\mathcal{N}(A)$
# * Rowspaces, $R(A)$
#     * All linear combinations of rows
#     * All the linear combinations of the colums of $A^\top$, $\mathcal{C}(A^\top)$
# * Nullspace of $A^\top$, $\mathcal{N}(A^\top)$ (the left nullspace of $A$)

# ### Where are these spaces for a $m\times n$ matrix $A$?
# * $\mathcal{R}(A)$ is in $R^n$
# * $\mathcal{N}(A)$ is in $R^n$
# * $\mathcal{C}(A)$ is in $R^m$
# * $\mathcal{N}(A^\top)$ is in $R^m$

# ### Calculating basis and dimension
#
# #### For $\mathcal{R}(A)$
# * If $A$ undergoes row reduction to row echelon form $B$, then $\mathcal{C}(B)\neq \mathcal{C}(A)$, but $\mathcal{R}(B) = \mathcal{R}(A)$ (or $\mathcal{C}(B^\top) = \mathcal{C}(A^\top))$
# * A basis for the rowspace of $A$ (or $B$) is the first $r$ rows of $B$
#     * So we row reduce $A$ and take the pivot rows and transpose them
# * The dimension is also equal to the rank $r$
#
# #### For $\mathcal{N}(A)$
# * The bases are the special solutions (one for every free variable, $n-r$)
# * The dimension is $n- r$
#
#
# #### For $\mathcal{C}(A) = \mathcal{R}(A^\top)$
# * Apply the row reduction on the transpose $A^\top$.
# * The dimension is the rank $r$
#
#
# #### For $\mathcal{N}(A^\top)$
# * It is also called the left nullspace, because it ends up on the left (as seen below)
# * Here we have $A^\top y = 0$
#     * $y^\top(A^\top)^\top = 0^\top$
#     * $y^\top A = 0^\top$
#     * This is (again) the special solutions for $A^\top$ (after row reduction)
# * The dimension is $m - r$

# ----
#
# <a name="Practice_Example"></a>
# ## 3.  Practice Example:
#
# Consider the linear transformation defined by the following matrix $A$.  
#
# $$A = 
# \left[
# \begin{matrix}
#     1 & 2 & 3 & 1  \\
#     1 & 1 & 2 & 1  \\
#     1 & 2 & 3 & 1 
#  \end{matrix}
# \right] 
# $$

# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import sympy as sym
sym.init_printing()

# **&#9989;  <font color=red>Question:</font>** What is the reduced row echelon form of $A$?  You can use sympy.

# +
#Put your answer to the above question here.
# -

# **&#9989;  <font color=red>Question:</font>** Now let's calculate the row space of $A$. 
# Note that the row space is defined by a linear combination of the non-zero row vectors in the reduced row echelon matrix:

# Put your answer to the above question here

# &#9989;  **<font color=red>Question:</font>** What is the rank of matrix $A$? You should know the rank by inspecting the reduced row echelon form. Find a ```numpy``` or ```sympy``` function that you can use to verify your answer?

# +
## Put code here to verify your answer.
# -

# &#9989;  **<font color=red>Question:</font>** Using the reduced row echelon form define the leading variables in terms of the free variables for the homogeneous equation. 

# Put your answer to the above question here

# &#9989;  **<font color=red>Question:</font>** The solution to the above question defines the nullspace of $A$ (aka the Kernel). Use the *sympy.nullspace* function to verify your answer.

# +
# Put your code here
# -

# &#9989;  **<font color=red> Question:</font>** Now let's calculate the range of $A$ (column space of $A$).  Note that the range is spanned by the column vectors of $A$. 
# Transpose $A$ and calculate the reduced row echelon form of the transposed matrix like we did above.

# +
## Put your code here
# -

# &#9989;  **<font color=red>Question:</font>** The nonzero row vectors of the above solution will give a basis for the range (or $\mathcal{C}(A)$). Write the range of $A$ as a linear combination of these nonzero vectors:

# Put your answer to the above question here.

# &#9989;  **<font color=red>Question:</font>** Finally, using the reduced row echelon form for $A^\top$ define the leading variables in terms of the free variables and define the null space of $A^\top$.

# Put your answer to the above question here.

# ----
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
