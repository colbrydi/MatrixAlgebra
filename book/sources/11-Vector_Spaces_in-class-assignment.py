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

# # 11 In-Class Assignment: Vector Spaces
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/3d_basis_transformation.svg/580px-3d_basis_transformation.svg.png" width="50%">
#
# Image from: [https://en.wikipedia.org/wiki/Change_of_basis](https://en.wikipedia.org/wiki/Change_of_basis)
#
#
#
#     

# ### Agenda for today's class (80 minutes)
#
# 1. (20 minutes) [Review Pre-Class Assignment](#Review)
# 2. (20 minutes) [Introduction to subspaces](#Introduction-to-subspaces)
# 3. (20 minutes) [Basis Vectors](#Basis-Vectors)
# 4. (20 minutes) [Vector Spaces](#Vector-Spaces)
#
#

# ----
#
# <a name="Review"></a>
#
# ## 1. Review Pre-class Assignment
#
# Like most days, your instructor will review and answer questions from your pre-class assignment.  This is your opportunity to ask any lingering questions before the quiz. 
#
#
#
# - [11--Vector_Spaces_pre-class-assignment.ipynb](11--Vector_Spaces_pre-class-assignment.ipynb)

#
# ---
# <a name=Introduction-to-subspaces></a>
# ## 2. Introduction to subspaces
#
#

#
#
# ---
# <a name=Basis-Vectors></a>
# ## 3. Basis Vectors
#
#

# Consider the following example. We claim that the following set of vectors form a baiss for $R^3$:
#
# $$B = \{(2,1, 3), (-1,6, 0), (3, 4, -10) \}$$

# If these vectors form a basis they must be _**linearly independent**_ and _**Span**_ the entire space of $R^3$

# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import sympy as sym
sym.init_printing(use_unicode=True)

# &#9989; **<font color=red>DO THIS:</font>** Create a $3 \times 3$ numpy matrix $A$ where the columns of $A$ form are the basis vectors. 

# +
#Put your answer to the above question here

# +
from answercheck import checkanswer

checkanswer.matrix(A,'68b81f1c1041158b519936cb1a2e4d6b');
# -

# &#9989; **<font color=red>DO THIS:</font>** Using python, calculate the determinant of matrix $A$.

# +
# Put your answer to the above question here. 
# -

# &#9989; **<font color=red>DO THIS:</font>** Using python, calculate the inverse of $A$.

# +
# Put your answer to the above question here.
# -

# &#9989; **<font color=red>DO THIS:</font>** Using python, calculate the rank of $A$.

# +
# Put your answer to the above question here.
# -

# &#9989; **<font color=red>DO THIS:</font>** Using python, calculate the reduced row echelon form of $A$.

# +
# Put your answer to the above question here. 
# -

# &#9989; **<font color=red>DO THIS:</font>** Using the above $A$ and the vector $b=(1,3,2)$.  What is the solution to $Ax=b$?  

# +
#Put your answer to the above question here.

# +
from answercheck import checkanswer

checkanswer.matrix(x,'8b0938260dfeaafc9f8e9fec0bc72f17');
# -

# Turns out a matrix where column vectors are formed from basis vectors a lot of interesting properties and the following statements are equivalent.
#
# - The column vectors of $A$ form a basis for $R^n$
# - $|A| \ne 0$
# - $A$ is invertible.
# - $A$ is row equivalent to $I_n$ (i.e. it's reduced row echelon form is $I_n$)
# - The system of equations $Ax = b$ has a unique solution.
# - $rank(A) = n$
#

# Not all matrices follow the above statements but the ones that do are used throughout linear algebra so it is important that we know these properties. 

#
#
# ---
# <a name=Vector-Spaces></a>
# ## 4. Vector Spaces
#
# A **Vector Space** is a set $V$ of elements called **vectors**, having operations of addition and scalar multiplication defined on it that satisfy the following conditions ($u$, $v$, and $w$ are arbitrary elements of $V$, and c and d are scalars.)
#
# ### Closure Axioms
#
# 1. The sum $u + v$ exists and is an element of $V$. ($V$ is closed under addition.)
# 2. $cu$ is an element of $V$. ($V$ is closed under scalar multiplication.)
#
# ### Addition Axioms
#
# 3. $u + v = v + u$ (commutative property)
# 4. $u + (v + w) = (u + v) + w$ (associative property)
# 5. There exists an element of $V$, called a **zero vector**, denoted $0$, such that $u+0 = u$
# 6. For every element $u$ of $V$, there exists an element called a **negative** of $u$, denoted $-u$, such that $u + (-u) = 0$.
#
# ### Scalar Multiplication Axioms
#
# 7. $c(u+v) = cu + cv$
# 8. $(c + d)u = cu + du$
# 9.  $c(du) = (cd)u$
# 10. $1u = u$
#
# ### Definition of a basis of a vector space
#
# > A finite set of vectors ${v_1,\dots, v_n}$ is called a **basis** of a *vector space* $V$ if the set *spans* $V$ and is *linearly independent*. 
# >i.e. each vector in $V$ can be expressed uniquely as a *linear combination* of the vectors in a basis.
#
#

# ## Vector spaces
#
# &#9989; **<font color=red>DO THIS:</font>** Let $U$ be the set of all circles in $R^2$ having center at the origin. 
# Interpret the origin as being in this set, i.e., it is a circle center at the origin with radius zero. 
# Assume $C_1$ and $C_2$ are elements of $U$. 
# Let $C_1 + C_2$ be the circle centered at the origin, whose radius is the sum of the radii of $C_1$ and $C_2$. 
# Let $kC_1$ be the circle center at the origin, whose radius is $|k|$ times that of $C_1$. 
# Determine which vector space axioms hold and which do not. 
#

# Put your answer here

# ### Spans:
#
# &#9989; **<font color=red>DO THIS:</font>** Let $v$, $v_1$, and $v_2$ be vectors in a vector space $V$. 
# Let $v$ be a linear combination of $v_1$ and $v_2$. 
# If $c_1$ and $c_2$ are nonzero real numbers, show that $v$ is also a linear combination of $c_1v_1$ and $c_2v_2$.

# Put your answer here

# &#9989; **<font color=red>DO THIS:</font>** Let $v_1$ and $v_2$ span a vector space $V$. 
# Let $v_3$ be any other vector in $V$. 
# Show that $v_1$, $v_2$, and $v_3$ also span $V$.

# Put your answer here

# ### Linear Independent:
# Consider the following matrix, which is in the reduced row echelon form.
#
#
# $$ 
# \left[
# \begin{matrix}
#     1   & 0 & 0 & 7  \\
#     0   & 1 & 0 & 4  \\
#     0   & 0 & 1 & 3
# \end{matrix}
# \right] 
# $$
#
# &#9989; **<font color=red>DO THIS:</font>** Show that the row vectors form a linearly independent set:
#

# Put your answer here

# &#9989; **<font color=red>DO THIS:</font>** Is the set of nonzero row vectors of any matrix in reduced row echelon form linearly independent? Discuss in your groups and include your thoughts below.

# Put your answer here

# &#9989; **<font color=red>DO THIS:</font>** A computer program accepts a number of vectors in $R^3$ as input and checks to see if the vectors are linearly independent and outputs a True/False statment. 
# Discuss in your groups, which is more likely to happen due to round-off error--that the computer states that a given set of linearly independent vectors is linearly dependent, or vice versa? 
# Put your groups thoughts below.

# Put your answer here

# ----
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
