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

# # 18 Pre-Class Assignment: Inner Product

# ## Goals for today's pre-class assignment 
#
# </p>
#
# 1. [Inner Products](#Inner_Products)
# 1. [Inner Product on Functions](#Inner_Product_on_Functions)
# 1. [Assignment wrap-up](#Assignment_wrap-up)

# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
sym.init_printing()

# ---
# <a name="Inner_Products"></a>
# ## 1. Inner Products
#
# **Definition:** An **inner product** on a vector space $V$ (Remember that $R^n$ is just one class of vector spaces) is a function that associates a number, denoted as $\langle u,v \rangle$, with each pair of vectors $u$ and $v$ of $V$. This function satisfies the following conditions for vectors $u, v, w$ and scalar $c$:
#
# - $\langle u,v \rangle = \langle v,u \rangle$ (symmetry axiom)
# - $\langle u+v,w \rangle = \langle u,w \rangle + \langle v,w \rangle$ (additive axiom) 
# - $\langle cu,v \rangle = c\langle v,u \rangle$ (homogeneity axiom)
# - $\langle u,u \rangle \ge 0 \text{ and } \langle u,u \rangle = 0 \text{ if and only if } u = 0$ (positive definite axiom) 
#
#
# The dot product of $R^n$ is an inner product. Note that we can define new inner products for $R^n$.
#
# ### Norm of a vector
#
# **Definition:** Let $V$ be an inner product space. The **norm** of a vector $v$ is denoted by $\| v \|$ and is defined by:
#
# $$\| v \| = \sqrt{\langle v,v \rangle}.$$
#
# ### Angle between two vectors
#
# **Definition:** Let $V$ be a real inner product space. The **angle $\theta$ between two nonzero vectors $u$ and $v$** in $V$ is given by:
#
# $$cos(\theta) = \frac{\langle u,v \rangle}{\| u \| \| v \|}.$$
#
# ### Orthogonal vectors
#
# **Definition:** Let $V$ be an inner product space.  Two vectors $u$ and $v$ in $V$ are **orthogonal** if their inner product is zero:
#
# $$\langle u,v \rangle = 0.$$
#
# ### Distance
# **Definition:** Let $V$ be an inner product space. The **distance between two vectors (points) $u$ and $v$** in $V$ is denoted by $d(u,v)$ and is defined by:
#
# $$d(u,v) = \| u-v \| = \sqrt{\langle u-v, u-v \rangle}$$
#
#

# #### Example:
# Let $R^2$ have an inner product defined by:
# $$\langle (a_1,a_2),(b_1,b_2)\rangle = 2a_1b_1 + 3a_2b_2.$$

# &#9989; **<font color=red>QUESTION 1:</font>** What is the norm of (1,-2) in this space?

# Put your answer to the above question here.

# &#9989; **<font color=red>QUESTION 2:</font>** What is the distance between (1,-2) and (3,2) in this space?

# Put your answer to the above question here.

# &#9989; **<font color=red>QUESTION 3:</font>** What is the angle between (1,-2) and (3,2) in this space?

# Put your answer to the above question here.

# &#9989; **<font color=red>QUESTION 4:</font>** Determine if (1,-2) and (3,2) are orthogonal in this space?

# Put your answer to the above question here.

# ---
# <a name="Inner_Product_on_Functions"></a>
# ## 2. Inner Product on Functions

from IPython.display import YouTubeVideo
YouTubeVideo("8ZyeHtgMBjk",width=640,height=360, cc_load_policy=True)

# #### Example
# Consider the following functions 
#
# $$f(x)=3x-1$$
# $$g(x)=5x+3$$
#
# $$\text{with inner product defined by }\langle f,g\rangle=\int_0^1{f(x)g(x)dx}.$$
#
# &#9989; **<font color=red>QUESTION 5:</font>** What is the norm of $f(x)$ in this space?

# Put your answer to the above question here. (Hint: you can use `sympy.integrate` to compute the integral)

# &#9989; **<font color=red>QUESTION 6:</font>** What is the norm of g(x) in this space?

# Put your answer to the above question here.

# &#9989; **<font color=red>QUESTION 7:</font>** What is the inner product of $f(x)$ and $g(x)$ in this space?

# Put your answer to the above question here.

# ----
#
# <a name="Assignment_wrap-up"></a>
# ## 3. Assignment wrap-up

# &#9989; **<font color=red>Assignment-Specific QUESTION:</font>** There is no Assignment specific question for this notebook. You can just say "none".

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
