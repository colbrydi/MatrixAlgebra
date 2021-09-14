# -*- coding: utf-8 -*-
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

# # 05 In-Class Assignment: Gauss-Jordan
#  
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Sextic_Graph.svg/1200px-Sextic_Graph.svg.png" width='50%' alt="Simple xy graph with a high order polynomial representing a curve. In this assignment we will be covering curve fitting an the figure is just intended as a viaual motivation" >

#
#

# ### Today's Agenda (80 minutes)
#
# 1. [(20 minutes) Pre-class assignment review](#Pre-class_aassignment_review)
# 1. [(20 minutes) Generalize the procedure](#Generalize_the_procedure)
# 1. [(20 minutes) Basic Gauss Jordan](#Basic_Gauss_Jordan)
#
#

#Load Useful Python Libraries 
# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import sympy as sym
sym.init_printing(use_unicode=True)

# ----
# <a name="Pre-class_aassignment_review"></a>
# ## 1. Pre-class assignment review
#
# * [05--Gauss_Jordan2_pre-class-assignment.ipynb](05--Gauss_Jordan2_pre-class-assignment.ipynb)

# ----
# <a name="Generalize_the_procedure"></a>
# ## 2. Generalize the procedure
#
# We are going to think about Gauss-Jordan as an algorithm. First I want you to think about how you would generalize the procedure to work on any matrix.  Do the following before moving on to the next section. 
#
#
# &#9989;**<font color=red>DO THIS</font>**: Use the following matrix to think about how you would solve any system of equations using the Gauss-Jordan elimination algorithm.  Focus on the steps. 
#
#
# $$ 
# \left[
# \begin{matrix}
#     a & b & c  \\
#     e & f & g  \\
#     i & j & k 
#  \end{matrix}
# \, \middle\vert \,
# \begin{matrix}
# d \\ h \\ l
# \end{matrix}
# \right] 
# $$
#
#

# &#9989;**<font color=red>QUESTION</font>**: What are the first three mathematical steps you would do to put the above equation into a reduced row echelon form using Gauss-Jordan method?

# Put your answer here. 

# ### Psudocode
#
# &#9989;**<font color=red>QUESTION</font>**: Write down the steps you would complete to implement the Gauss-Jordan elimination algorithm as a computer programer. Some questions to answer:
#
# 1. What are the inputs?
# 2. What are the outputs?
# 3. How many and what types of loops would you have to guarantee success of your program?
#
# Once you have thought this though the instructor will work with you to build the algorithm.

# ----
#
# <a name="Basic_Gauss_Jordan"></a>
#
# ## 3. Basic Gauss Jordan

# The following is implementation of the Basic Gauss-Jordan Elimination Algorithm for Matrix $A^{m\times n}$ (Pseudocode):
# ```bash
# for i from 1 to m:
#     for j from 1 to m	
#         if i ≠ j:
#             Ratio = A[j,i]/A[i,i]
#             #Elementary Row Operation 3
#             for k from 1 to n:
#                 A[j,k] = A[j,k] - Ratio * A[i,k]
#             next k
#         endif
#     next j
#     
#     #Elementary Row Operation 2
#     Const = A[i,i]
#     for k from 1 to n:
#         A[i,k] = A[i,k]/Const
# next i
# ```

# &#9989;**<font color=red>DO THIS</font>**: using the Pseudocode provided above, write a ```basic_gauss_jordan``` function which takes a list of lists $A$ as input and returns the modified list of lists:

# +
# Put your answer here. 
# -

# Lets check your function by applying the ```basic_gauss_jordan``` function and check to see if it matches the answer from matrix $A$ in the pre-class video:

A = [[1, 1, 1, 2], [2, 3, 1, 3], [0, -2, -3, -8]]
answer = basic_gauss_jordan(A)
sym.Matrix(answer)

answer_from_video = [[1, 0, 0, -1], [0, 1, 0, 1], [0, 0, 1, 2]]
np.allclose(answer, answer_from_video)

# The above psuedocode does not quite work properly for all matrices. For example, consider the following augmented matrix:
#
# $$ 
# B = \left[
# \begin{matrix}
#     0 & 1 & 33\\ 
#     5 & 3 & 7 \\
#     6 & 69 & 4
#  \end{matrix}
#  \, \middle\vert \,
# \begin{matrix}
#  30 \\ 
#  90 \\
#  420
# \end{matrix}
# \right] 
# $$

# &#9989;**<font color=red>QUESTION</font>**: Explain why doesn't the provided ```basic_gauss_jordan``` function work on the matrix $B$? 

# Put your answer to the above question here.

# &#9989;**<font color=red>QUESTION</font>**: Describe how you could modify matrix $B$ so that it would work with ```basic_gauss_jordan``` AND still give the correct solution? 

# Put your answer to the above question here.

# +
# Put your code here
# -

# ----
#
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
