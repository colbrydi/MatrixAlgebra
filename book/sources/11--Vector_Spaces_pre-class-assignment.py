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

# # 11 Pre-Class Assignment: Vector Spaces

# ### Readings for this topic (Recommended in bold)
#  * [**_Heffron Chapter  2 II pg 77-86_**](http://joshua.smcvt.edu/linearalgebra/book.pdf)
#  * [Beezer Chapter VS pg 257-269](http://linear.ups.edu/download/fcla-3.50-tablet.pdf)
#

# ### Goals for today's pre-class assignment 
#
# 1. [Basis Vectors](#Basis_Vectors)
# 1. [Vector Spaces](#Vector_Spaces)
# 1. [Lots of Things Can Be Vector Spaces](#Examples)
# 1. [Assignment Wrap-up](#Assignment_Wrap-up)

# ----
# <a name="Basis_Vectors"></a>
# ## 1. Basis Vectors
#
# Below is a really good review of concepts such as: Linear combinatins, span, and basis vectors. 

from IPython.display import YouTubeVideo
YouTubeVideo("k7RM-ot2NWY",width=640,height=360, cc_load_policy=True)

# &#9989; **<font color=red>QUESTION:</font>** What is the **technical definition** of a basis?

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>** Write three basis vectors that span $R^3$.
#

# Put your answer to the above question here

# From the above video two terms we want you to really understand _**Span**_ and **_Linear Independent_**. Understanding these two will be really important when you think about basis.  Make sure you watch the video and try to answer the following questions as best you can using your own words.  

# &#9989; **<font color=red>QUESTION:</font>** Describe what it means for vectors to _**Span**_ a space?
#

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>** What is the span of two vectors that point in the same direction?
#

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>** Can the following vectors span $R^3$? Why?
#
# $(1,-2,3),\quad (-2,4,-6),\quad (0,6,4)$

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>**  Describe what it means for vectors to be _**Linearly Independent**_?

# Put your answer to the above question here

# If you have vectors that _**span**_ a space AND are _**Linearly Independent**_ then these vectors form a **_Basis_** for that space.  
#
#
# Turns out you can create a matrix by using basis vectors as columns. This matrix can be used to change points from one basis representation to another.  

# ----
#
# <a name="Vector_Spaces"></a>
# ## 2.  Vector Spaces
#
# Vector spaces are an abstract concept used in math. So far we have talked about vectors of real numbers ($R^n$). However, there are other types of vectors as well.  A vector space is a formal definition. If you can define a concept as a vector space then you can use the tools of linear algebra to work with those concepts.  
#
# A **Vector Space** is a set $V$ of elements called **vectors**, having operations of addition and scalar multiplication defined on it that satisfy the following conditions ($u$, $v$, and $w$ are arbitrary elements of $V$, and $c$ and $d$ are scalars.)
#
# ### Closure Axioms
#
# 1. The sum $u + v$ exists and is an element of $V$. ($V$ is closed under addition.)
# 2. $cu$ is an element of $V$. ($V$ is closed under multiplication.)
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
#

# ----
# <a name="Examples"></a>
# ## 3. Lots of Things Can Be Vector Spaces

from IPython.display import YouTubeVideo
YouTubeVideo("YmGWj9RrNMI",width=640,height=360, cc_load_policy=True)

# Consider the following two matrices $A\in R^{3x3}$ and $B\in R^{3x3}$, which consist of real numbers:

# +
# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import sympy as sym
sym.init_printing()

a11,a12,a13,a21,a22,a23,a31,a32,a33 = sym.symbols('a_{11},a_{12}, a_{13},a_{21},a_{22},a_{23},a_{31},a_{32},a_{33}', negative=False)
A = sym.Matrix([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
A
# -

b11,b12,b13,b21,b22,b23,b31,b32,b33 = sym.symbols('b_{11},b_{12}, b_{13},b_{21},b_{22},b_{23},b_{31},b_{32},b_{33}', negative=False)
B = sym.Matrix([[b11,b12,b13],[b21,b22,b23],[b31,b32,b33]])
B

# &#9989; **<font color=red>QUESTION:</font>** What properties do we need to show all $3\times 3$ matrices of real numbers form a vector space. 

# Put your answer here

# &#9989; **<font color=red>DO THIS:</font>** Demonstrate these properties using **sympy** as was done in the video. 

# +
#Put your answer here. 
# -

# &#9989; **<font color=red>QUESTION (assignment specific):</font>** Determine whether $A$ is a linear combination of $B$, $C$, and $D$?
#
# $$ A=
# \left[
# \begin{matrix}
#     7 & 6 \\
#     -5 & -3 
# \end{matrix}
# \right],
# B=
# \left[
# \begin{matrix}
#     3 & 0 \\
#     1 & 1 
# \end{matrix}
# \right],
# C=
# \left[
# \begin{matrix}
#     0 & 1 \\
#     3 & 4 
# \end{matrix}
# \right],
# D=
# \left[
# \begin{matrix}
#     1 & 2 \\
#     0 & 1 
# \end{matrix}
# \right]
# $$

# +
#Put your answer to the above question here
# -

# &#9989; **<font color=red>QUESTION:</font>**  Write a basis for all $2\times 3$ matrices and give the dimension of the space.

# Put your answer to the above question here.

# ----
#
# <a name="Assignment_Wrap-up"></a>
# ## 5. Assignment wrap-up

# &#9989; **<font color=red>Assignment-Specific QUESTION:</font>** Is matrix $A$ is a linear combination of $B$, $C$, and $D$ from above?

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
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
