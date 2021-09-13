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

# # 13 Pre-Class Assignment: Projections

# ### Readings for this topic (Recommended in bold)
#  * [Heffron Section VI pg 267-275](http://joshua.smcvt.edu/linearalgebra/book.pdf)
#  * [Beezer Subsections OV-GSP pg 154-161](http://linear.ups.edu/download/fcla-3.50-tablet.pdf)
#  * [**_Boyd Section 5.3-5.4 pg 95-102_**](http://vmls-book.stanford.edu/vmls.pdf)
#

# ### Goals for today's pre-class assignment 
#
# 1. [Orthogonal and Orthonormal](#Orthogonal_and_Orthonormal)
# 1. [Code Review](#Code_Review)
# 1. [Gram-Schmidt](#Gram-Schmidt)
# 1. [Assignment Wrap-up](#Assignment_Wrap-up)

# ----
# <a name="Orthogonal_and_Orthonormal"></a>
# ## 1. Orthogonal and Orthonormal
#
# **Definition:** A set of vectors is said to be **orthogonal** if every pair of vectors in the set is orthogonal (the dot product is 0). 
# The set is **orthonormal** if it is orthogonal and each vector is a unit vector (norm equals 1). 
#
# **Result:** An orthogonal set of nonzero vectors is linearly independent.
#
# **Definition:** A basis that is an orthogonal set is called an orthogonal basis.
# A basis that is an orthonormal set is called an orthonormal basis.
#
# **Result:** Let $\{u_1,\dots,u_n\}$ be an orthonormal basis for a vector space $V$. 
# Then for any vector $v$ in $V$, we have 
# $$v=(v\cdot u_1)u_1+(v\cdot u_2)u_2 +\dots + (v\cdot u_n)u_n$$
#
# **Definition:** A *square* matrix is **orthogonal** is $A^{-1}=A^\top$.
#
# **Result:** Let $A$ be a square matrix. The following three statements are equivalent.
#
# (a) $A$ is orthogonal. 
#
# (b) The column vectors of $A$ form an orthonormal set. 
#
# (c) The row vectors of $A$ form an orthonormal set.
#
# (d) $A^{-1}$ is orthogonal. 
#
# (e) $A^\top$ is orthogonal.
#
# **Result:** If $A$ is an orthogonal matrix, then we have $|A|=\pm 1$.

# Consider the following vectors $u_1, u_2$, and $u_3$ that form a basis for $R^3$. 
#
# $$ u_1 = (1,0,0)$$
# $$ u_2 = (0, \frac{1}{\sqrt(2)}, \frac{1}{\sqrt(2)})$$
# $$ u_3 = (0, \frac{1}{\sqrt(2)}, -\frac{1}{\sqrt(2)})$$

# &#9989; **<font color=red>DO THIS:</font>**  Show that the vectors $u_1$, $u_2$, and $u_3$ are linearly independent (**HINT:** see the pre-class for 0219-Change_Basis):

# Put your answer to the above here

# &#9989; **<font color=red>QUESTION 1:</font>** How do you show that $u_1$, $u_2$, and $u_3$ are orthogonal?

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION 2:</font>** How do you show that $u_1$, $u_2$, and $u_3$ are normal vectors?

# Put your answer to the above question here

# &#9989; **<font color=red>DO THIS:</font>**  Express the vector $v = (7,5,-1)$ as a linear combination of the $u_1$, $u_2$, and $u_3$ basis vectors:

# +
# Put your answer here
# -

# ----
# <a name="Code_Review"></a>
# ## 2. Code Review
#
# In the next in-class assignment, we are going to avoid some of the more advanced libraries ((i.e. no ```numpy``` or ```scipy``` or ```sympy```) to try to get a better understanding about what is going on in the math. 
# The following code implements some common linear algebra functions:

#Standard Python Libraries only
import math
import copy


def dot(u,v):
    '''Calculate the dot product between vectors u and v'''
    temp = 0;
    for i in range(len(u)):
        temp += u[i]*v[i]
    return temp


# &#9989; **<font color=red>DO THIS:</font>** Write a quick test to compare the output of the above ```dot``` function with the ```numpy``` dot function.

# +
# Put your test code here
# -

def multiply(m1,m2):
    '''Calculate the matrix multiplication between m1 and m2 represented as list-of-list.'''
    n = len(m1)
    d = len(m2)
    m = len(m2[0])
    
    if len(m1[0]) != d:
        print("ERROR - inner dimentions not equal")
    
    #make zero matrix
    result = [[0 for j in range(m)] for i in range(n)]
#    print(result)
    for i in range(0,n):
        for j in range(0,m):
            for k in range(0,d):
                #print(i,j,k)
                #print('result', result[i][j])
                #print('m1', m1[i][k])
                #print('m2', m2[k][j])
                result[i][j] = result[i][j] + m1[i][k] * m2[k][j]
    return result



# &#9989; **<font color=red>DO THIS:</font>** Write a quick test to compare the output of the above ```multiply``` function with the ```numpy``` multiply function.

# +
# Put your test code here
# -

# &#9989; **<font color=red>QUESTION:</font>** What is the big-O complexity of the above ```multiply``` function?

# Put your answer to the above question here.

# &#9989; **<font color=red>QUESTION:</font>** Line 11 in the provided ```multiply``` code initializes a matrix of the size of the output matrix as a list of lists with zeros. What is the big-O complexity of line 11?

# Put your answer to the above question here.

def norm(u):
    '''Calculate the norm of vector u'''
    nm = 0
    for i in range(len(u)):
        nm += u[i]*u[i]
    return math.sqrt(nm)


# &#9989; **<font color=red>DO THIS:</font>** Write a quick test to compare the outputs of the above ```norm``` function with the ```numpy``` norm function.

# +
#Put your test code here
# -

def transpose(A):
    '''Calculate the transpose of matrix A represented as list of lists'''
    n = len(A)
    m = len(A[0])
    AT = list()
    for j in range(0,m):    
        temp = list()
        for i in range(0,n):
            temp.append(A[i][j])
        AT.append(temp)
    return AT


# &#9989; **<font color=red>DO THIS:</font>** Write a quick test to compare the output of the above ```transpose``` function with the ```numpy``` transpose function.

# +
# Put your test code here
# -

# &#9989; **<font color=red>QUESTION:</font>** What is the big-O complexity of the above ```transpose``` function?

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>** Explain any differences in results between the provided functions and their ```numpy``` counterparts. 

# Put your answer to the above question here

# ----
# <a name="Gram-Schmidt"></a>
# ## 3. Gram-Schmidt
#
#
# Watch this video for the indroduction of Gram-Schmidt, which we will implement in class.

from IPython.display import YouTubeVideo
YouTubeVideo("rHonltF77zI",width=640,height=360, cc_load_policy=True)

# ----
#
# <a name="Assignment_Wrap-up"></a>
# ## 4. Assignment wrap-up

# &#9989; **<font color=red>Assignment-Specific QUESTION:</font>** How do you show that $u_1$, $u_2$, and $u_3$ are orthogonal?

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>**  Summarize what you did in this assignment.

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>**  What questions do you have, if any, about any of the topics discussed in this assignment after working through the jupyter notebook?

#
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
