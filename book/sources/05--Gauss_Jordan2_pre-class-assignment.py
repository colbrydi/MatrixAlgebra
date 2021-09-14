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

# # 05 Pre-Class Assignment: Gauss-Jordan Elimination

# ### Recommended further readings for this pre-class assignment.
#  * **_[Boyd - Section 1.4-1.5 pg 19-24](http://vmls-book.stanford.edu/vmls.pdf)_**
#  * [Beezer - Subsection IP pg 149-152](http://linear.ups.edu/download/fcla-3.50-tablet.pdf)
#  * [Heffron - Chapter 1.II.2 pg 43-47](http://joshua.smcvt.edu/linearalgebra/book.pdf)

# ### Goals for today's pre-class assignment 
#
#
# 1. [Sympy RREF function](#Sympy-RREF-function)
# 2. [Calculating Vector Length, Normalization, Distance and Dot](#Calculating-Vector-Length,-Normalization,-Distance-and-Dot)
# 3. [Vector spaces in $R_n$](#Vector-spaces-in-Rn)
# 4. [Assignment wrap up](#Assignment-wrap-up)

#  Load Useful Python Libraries 
# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import sympy as sym
sym.init_printing(use_unicode=True)

#
#
# ---
# <a name=Sympy-RREF-function></a>
# ## 1. Sympy RREF function
#
#
#
#
#
#
#
# In class we talked about the Python ```sympy``` library which has a "reduced row echelon form" (rref) function that runs a much more efficient version of the Gauss-Jordan function.  To use the ```rref``` function you must first convert your matrix into a ```sympy.Matrix``` and then run the function. For example, lets do this for the following  matrix $B$:

B = np.matrix([[ 50, 13, 30 ], [100, 26, 60 ],  [20.5, 25, 650]])
sym.Matrix(B).rref()

# This function outputs two values (a matrix and a tuple).  For the purposes of this class we only care about the matrix.  I generally use the following syntax when using ```rref()```

sym.Matrix(B).rref()[0]

# &#9989;**<font color=red>QUESTION</font>**: Although we do not use it often in this course, what does the second output of the ```rref``` mean (i.e. what does ```(0,1)``` mean? **_hint_**: read the documentation for ```rref```. 

# **_Put your answer to the above question here_**

# How lets consider the multi-week example from a previous assignment, where:
#
# **Week 1:**
# $$ c + b = 30 $$
# $$ 20c + 25b = 690 $$
#
# **Week 2:**
# $$ c + b = 35 $$
# $$ 20c + 25b = 750 $$
#
# **Week 3:**
# $$ c + b = 30 $$
# $$ 20c + 25b = 650 $$

# &#9989;**<font color=red>DO THIS</font>**: Write a $2 \times 5$ augmented matrix representing the 6 equations above.  (you can just copy and paste this from the pre-class if you got it right there), Name your Matrix $G$ to verify your answer using the ```checkanswer``` function below.

# +
#Put your answer to the above question here. 
# -

# The following function will apply the rref function to the matrix $G$ and store it in a variable called, wait for it,  ```rref```:

rref,_ = sym.Matrix(G).rref()
rref

# &#9989;**<font color=red>QUESTION</font>**: Given the above,  How many hours did Giselle work as a capenter for the three weeks and how many hours did she work as a blacksmith.  Fill in your answers below to check if you are correct:

#Replace the zeros with your answers
carpenter_week1 = 0
carpenter_week2 = 0
carpenter_week3 = 0
blacksmith_week1 = 0
blacksmith_week2 = 0
blacksmith_week3 = 0

# +
from answercheck import checkanswer

hours = [[carpenter_week1, carpenter_week2, carpenter_week3],
         [blacksmith_week1, blacksmith_week2, blacksmith_week3]]
hours = np.matrix(hours).astype('float')

checkanswer.matrix(hours,'b2d4a73cac3c95204f5ed743b507093a');
# -

# ---
# <a name=Calculating-Vector-Length,-Normalization,-Distance-and-Dot></a>
# ## 2. Calculating Vector Length, Normalization, Distance and Dot
#
# In this section we will cover some of the basic vector math we will use this semester. 
#
# &#9989;**<font color=red>DO THIS</font>**:  Watch the following summary video about calculation of vector length, Normalizing vectors and the distance between points then answer the questions.

from IPython.display import YouTubeVideo
YouTubeVideo("S0BIhbV6reI",width=640,height=360, cc_load_policy=True)

# ### Vector:
# $$(a_1, a_2, \dots a_n)$$

# $$(b_1, b_2, \dots b_n)$$

# ### Length:
# $$length = \sqrt{a_1^2 + a_2^2 + \dots + a_n^2}$$

# ### Normalization:
# $$\frac{1}{length}(a_1, a_2, \dots a_n)$$

# ### Distance:
# $$distance = \sqrt{(a_1 - b_1)^2 + (a_2 - b_2)^2 + \dots + (a_n - b_n)^2}$$

# &#9989;**<font color=red>QUESTION</font>**:   Calculate length of vector (4.5, 2.6, 3.3, 4.1)?

# +
#Put your answer to the above question here

# +
from answercheck import checkanswer

checkanswer.float(length,'695da96d4a240e54bd8c61e75ff5a3e2');
# -

# &#9989;**<font color=red>QUESTION</font>**: What is a normalized form of the vector (4.5, 2.6, 3.3, 4.1)?

# +
#Put your answer to the above question here

# +
from answercheck import checkanswer

checkanswer.vector(norm,'12c94f16ba11222987ca20006790182d');
# -

# &#9989;**<font color=red>QUESTION</font>**:  What is the distance between (4.5, 2.6, 3.3, 4.1) and (4, 3, 2, 1)?

# +
#Put your answer to the above question here

# +
from answercheck import checkanswer

checkanswer.float(distance,'d73defc9a514eb70434190e1757f5bb8');
# -

# ### Dot Product:
#
#
# $$dot(a,b) = a_1b_1 + a_2b_2 +\dots + a_nb_n$$
#
#
#
#
# &#9989;**<font color=red>DO THIS</font>**:  Review **_Sections 1.4 and 1.5 of the Boyd and Vandenberghe_** text and answer the questions below.

# &#9989;**<font color=red>QUESTION</font>**:   What is the dot product between $u = [ 1, 7, 9, 11]$ and $v = [ 7, 1, 2, 2]$  (Store the information in a variable called ```uv```)?

# Put your answer to the above question here


# +
from answercheck import checkanswer

checkanswer.float(uv,'48044bf058c2d7d21b311b173a0ca7e5');
# -

# &#9989;**<font color=red>QUESTION</font>**:  What is the norm of vector $u$ defined above (store this value in a variabled called ```n```)?

# +
#Put your answer to the above question here

# +
from answercheck import checkanswer

checkanswer.float(n,'96078eb552924d7bdb9e67f9ecab88c1');
# -

# &#9989;**<font color=red>QUESTION</font>**:  What is the distance between points $u$ and $v$ defined above. (put your answer in a variable named ```d```)

# +
#Put your answer to the above question here

# +
from answercheck import checkanswer

checkanswer.float(d,'71f49beeb28061bc60eb3d9966497416');
# -

#
#
# ---
# <a name=Vector-spaces-in-Rn></a>
# ## 3. Vector spaces in $R^n$
#
#
# There are two properties that define a vector space these are:
#
# - Closed under addition
# - Closed under scalar multiplication 
#
# For now, we will consider vector spaces in $R^n$ which are just vectors of real numbers (ex: [10,20,3.2], [5,8,32], [8,-0.7], etc) where $n$ is just the length of the vector (ex: 3, 3, and 2 in the earlier example). In the general case a vector does not have to be composed of real numbers but can be almost any type of object as long as it maintains the two above properties, we will get into this concept later in the semester. In the case of real number the above concepts can be described as follows:
#
# - Closed under addition means that if we add any two real vectors vectors (i.e. $u,v \in R^n$) then the result is also in $R^n$). This is easy to understand if you think about adding any two real vectors there is no way to get a result that is not also a real vector. A way to say this mathematically is as follows:
#
# $$\text{if } u,v \in R^n$$
# $$\text{then } u+v \in R^n$$
#
# - Closed under scalar multiplication means that if we have any scalar number ($s \in R$) and we multiply it by a real vector ($v \in R^n$) then the result is also a vector in $R^n$.  Since multiplying a real number by a real number results in a real number this one is also true. Or we can say it as follows:
#
# $$\text{if } s \in R \text{ and } v \in R^n$$
# $$\text{then } sv \in R^n$$
#
# The following are some properties of vector addition and multiplication for vectors $u$ and $v$:
#
# 1. $u + v = v + u$ Commutative property
# 2. $u + (v + w) = (u + v) + w$ Associative property
# 3. $u+0 = 0 + u = u$ Property of zero vector
# 4. $u + (-u) = 0$ Property of the negative vector
# 5. $c(u+v) = cu + cv$ Distributive properties
# 6. $(c+d)u = cu+du$ Distributive Properties
# 7. $c(du) = (cd)u$ Distributed Properties
# 8. $1u = u$ Scalar multiplication by 1

# &#9989;**<font color=red>QUESTION</font>**: Compute the following linear combinations for $u = (1,2), v = (4,-1)$, and $w = (-3,5)$.
#
# **<font color=red>(a)</font>** $a = u+w$        

# Put your answer here

# +
from answercheck import checkanswer

checkanswer.vector(a,'af464d466ae982f2cd4461af494e86d6');
# -

# **<font color=red>(b)</font>** $a = 2u+v$        

# Put your answer here

# +
from answercheck import checkanswer

checkanswer.vector(a,'393468eff8c6ba5d27b7d0aa1b18f929');
# -

# **<font color=red>(c)</font>** $a = u+3w$        

# Put your answer here

# +
from answercheck import checkanswer

checkanswer.vector(a,'d5e5ca43a86501bcde09b1cbc0ba49b5');
# -

# ---
# <a name=Assignment-wrap-up></a>
# ## 4. Assignment wrap up

# &#9989; <font color=red>**Assignment-Specific QUESTION:**</font> What is the distance between (4.5, 2.6, 3.3, 4.1) and (4, 3, 2, 1)?

# Put your answer to the above question here

# &#9989; <font color=red>**QUESTION:**</font>  Summarize what you did in this assignment.

# Put your answer to the above question here

# &#9989; <font color=red>**QUESTION:**</font>  What questions do you have, if any, about any of the topics discussed in this assignment after working through the jupyter notebook?

# Put your answer to the above question here

# &#9989; <font color=red>**QUESTION:**</font>  How well do you feel this assignment helped you to achieve a better understanding of the above mentioned topic(s)?

# Put your answer to the above question here

# &#9989; <font color=red>**QUESTION:**</font> What was the **most** challenging part of this assignment for you? 

# Put your answer to the above question here

# &#9989; <font color=red>**QUESTION:**</font> What was the **least** challenging part of this assignment for you? 

# Put your answer to the above question here

# &#9989; <font color=red>**QUESTION:**</font>  What kind of additional questions or support, if any, do you feel you need to have a better understanding of the content in this assignment?

# Put your answer to the above question here

# &#9989; <font color=red>**QUESTION:**</font>  Do you have any further questions or comments about this material, or anything else that's going on in class?

# Put your answer to the above question here

# &#9989; <font color=red>**QUESTION:**</font> Approximately how long did this pre-class assignment take?

# Put your answer to the above question here

# ----
#
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

# ---------
# ### Congratulations, we're done!
#
# ###EndPreClass###

# ### Course Resources:
#
#
#
#
#

#
#
