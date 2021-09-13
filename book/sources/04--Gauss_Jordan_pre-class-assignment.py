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

# [Link to this document's Jupyter Notebook](04--Gauss_Jordan_pre-class-assignment.ipynb)

# ###StartPreClass###

# # 04 Pre-Class Assignment: Python Linear Algebra Packages
#
#

# ### Recommended further readings for this pre-class assignment.
#
# * **_[Beezer - Section RREF pg 22-44](http://linear.ups.edu/download/fcla-3.50-tablet.pdf)_**
# * [Heffron - Chapter 1.I, pg 2-13](http://joshua.smcvt.edu/linearalgebra/book.pdf)
#

# ---
# ### Assignment Overview
# 1. [The Syntax for Systems of Linear Equations](#The-Syntax-for-Systems-of-Linear-Equations)
# 2. [Introduction to Gauss Jordan Elimination](#Introduction-to-Gauss-Jordan-Elimination)
# 3. [ Gauss Jordan Elimination and the Row Echelon Form](#-Gauss-Jordan-Elimination-and-the-Row-Echelon-Form)
# 4. [Gauss Jordan Practice](#Gauss-Jordan-Practice)
# 5. [Assignment wrap up](#Assignment-wrap-up)
#
#

#
#
#
# ---
# <a name=The-Syntax-for-Systems-of-Linear-Equations></a>
# ## 1. The Syntax for Systems of Linear Equations
#
#
#
#
# The following video explains the different syntax we use to describe linear systems.

from IPython.display import YouTubeVideo
YouTubeVideo("AQJeOg4ZoIk",width=640,height=360, cc_load_policy=True)

# The following is a summary of the syntax shown in the video:

# ### Linear Equation $$b = a_1x_1+a_2x_2+a_3x_3 + \ldots a_nx_n$$

# ### System of linear equations
# $$b_1 = a_{11}x_1+a_{12}x_2+a_{13}x_3 + \ldots a_{1n}$$
# $$b_2 = a_{21}x_1+a_{22}x_2+a_{23}x_3 + \ldots a_{2n}$$
# $$b_3 = a_{31}x_1+a_{32}x_2+a_{33}x_3 + \ldots a_{3n}$$
# $$\vdots$$
# $$b_m = a_{m1}x_1+a_{m2}x_2+a_{m3}x_3 + \ldots a_{mn}$$

# ### System of linear equations (Matrix format)

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
#     x_m
# \end{matrix}
# \right] $$
#
# $$b=Ax$$

# ### System of linear equations (Augmented Form)
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

#
#
# ---
# <a name=Introduction-to-Gauss-Jordan-Elimination></a>
# ## 1. Introduction to Gauss Jordan Elimination
#
#
# The following elementary row operations
# 1. Interchange two rows of a matrix
# 2. Multiply the elements of a row by a nonzero constant
# 3. Add a multiple of the elements of one row to the corresponding elements of another

from IPython.display import YouTubeVideo
YouTubeVideo("iGmtmF_hm2g",width=640,height=360, cc_load_policy=True)

# Consider the element $a_{2,1}$ in the following $A$ Matrix.  
# $$ 
# A = \left[
# \begin{matrix}
#     1 & 1 \\ 
#     20 & 25  
#  \end{matrix}
#  \, \middle\vert \,
# \begin{matrix}
#  30 \\ 
#  690
# \end{matrix}
# \right] 
# $$

# &#9989; **<font color=red>QUESTION:</font>** : Describe an elementary row operation that could be used to make element $a_{(2,1)}$ zero?  

# Put your answer here. 

# &#9989; **<font color=red>QUESTION:</font>** : What is the new matrix given the above row operation.  

# Modify the contents of this cell and put your answer to the above question here.  
# $$ 
# A = \left[
# \begin{matrix}
#     1 & 1 \\ 
#     0 & ??  
#  \end{matrix}
#  \, \middle\vert \,
# \begin{matrix}
#  30 \\ 
#  ??
# \end{matrix}
# \right] 
# $$
#
#
#
# **Hint**, we are using a formating language called Latex to display the above matrix. You should just be able to replace the ?? with your new numbers. If you can't figure out what is going on, try searching the web with "latex math and matrix." If it still doesn't make sense, format your answer in another way that will be clear to understand by the you and the instructor.

# The following function is a basic implementation of the Gauss-Jorden algorithm to an (m,m+1) augmented matrix:

#
# <a name=-Gauss-Jordan-Elimination-and-the-Row-Echelon-Form></a>
# ## 2.  Gauss Jordan Elimination and the Row Echelon Form
#
#

from IPython.display import YouTubeVideo
YouTubeVideo("v6RstFsrTJY",width=640,height=360, cc_load_policy=True)

# The above video left out a special case for Reduced Row Echelon form. There can be non-zero elements in columns that do not have a leading one. For example, All of the following are in Reduced Row Echelon form:
#
# $$ 
# \left[
# \begin{matrix}
#     1 & 2 & 0 & 3 & 0 & 4 \\ 
#     0 & 0 & 1 & 2 & 0 & 7 \\ 
#     0 & 0 & 0 & 0 & 1 & 6 \\ 
#     0 & 0 & 0 & 0 & 0 & 0  
# \end{matrix}
# \right] 
# $$
#
#
# $$ 
# \left[
# \begin{matrix}
#     1 & 2 & 0 & 0 & 4 \\ 
#     0 & 0 & 1 & 0 & 6 \\ 
#     0 & 0 & 0 & 1 & 5   
# \end{matrix}
# \right] 
# $$

# &#9989; **<font color=red>QUESTION:</font>** : What are the three steps in the Gauss-Jordan Elimination algorithm?

#  Put your answer here. 

#
#
# ---
# <a name=Gauss-Jordan-Practice></a>
# ## 3. Gauss Jordan Practice
#
#
#
#
# &#9989; **<font color=red>DO THIS:</font>**: Solve the following system of linear equations using the Gauss-Jordan algorithm.  Try to do this before watching the video!
#
# $$x_1 + x_3 = 3$$
# $$2x_2 - 2x_3 = -4$$
# $$x_2 - 2x_3 = 5$$

# Put your answer here

# In the following video, we solve the same set of linear equations. Watch the video after trying to do this on your own.  It is provided here in case you get stuck.  

from IPython.display import YouTubeVideo
YouTubeVideo("xT16yIVw_KE",width=640,height=360, cc_load_policy=True)

# &#9989; **<font color=red>QUESTION:</font>**: Something was unclear in the above videos.  Describe the difference between a matrix in "row echelon" form and "reduced row echelon" form. 

# **_Put your answer to the above question here_**

# ---
# <a name=Assignment-wrap-up></a>
# ## 4. Assignment wrap up

# &#9989; **<font color=red>Assignment-Specific QUESTION:</font>**  Describe the difference between a matrix in "row echelon" form and "reduced row echelon" form.

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>**   Summarize what you did in this assignment.

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>**   What questions do you have, if any, about any of the topics discussed in this assignment after working through the jupyter notebook?

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>**   How well do you feel this assignment helped you to achieve a better understanding of the above mentioned topic(s)?

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>**  What was the **most** challenging part of this assignment for you? 

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>**  What was the **least** challenging part of this assignment for you? 

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
