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

# # 13 In-Class Assignment: Projections
#
# <img alt="Graph showing how one vector can be projected onto another vector by forming a right triangle" src="https://upload.wikimedia.org/wikipedia/commons/9/98/Projection_and_rejection.png" width="50%">
#
# Image from: https://en.wikipedia.org/wiki/Vector_projection
#
#

# ### Agenda for today's class (80 minutes)
#
# 1. [(20 minutes) Pre-Class Review](#Quiz_4_Review)
# 1. [(30 minutes) Understanding Projections with Code](#Understanding_Projections_with_Code)
# 1. [(30 minutes) Gram-Schmidt Orthoganalization Process](#Gram-Schmidt_Orthoganalization_Process)
#

# ---
# <a name="Quiz_4_Review"></a>
# ## 1. Pre-class Review
#
# * [13--Projections_pre-class-assignment](13--Projections_pre-class-assignment.ipynb)

# ----
# <a name="Understanding_Projections_with_Code"></a>
# ## 2. Understanding Projections With Code
#
# In this in-class assignment, we are going to avoid some of the more advanced libraries ((i.e. no ```numpy``` or ```scipy``` or ```sympy```) to try to get a better understanding about what is going on in the math. 
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


def multiply(m1,m2):
    '''Calculate the matrix multiplication between m1 and m2 represented as list-of-list.'''
    n = len(m1)
    d = len(m2)
    m = len(m2[0])
    
    if len(m1[0]) != d:
        print("ERROR - inner dimentions not equal")
    result = [[0 for i in range(n)] for j in range(m)]
    for i in range(0,n):
        for j in range(0,m):
            for k in range(0,d):
                result[i][j] = result[i][j] + m1[i][k] * m2[k][j]
    return result


def add_vectors(v1,v2):
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i]+v2[i])
    return v3


def sub_vectors(v1,v2):
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i]-v2[i])
    return v3


def norm(u):
    '''Calculate the norm of vector u'''
    nm = 0
    for i in range(len(u)):
        nm += u[i]*u[i]
    return math.sqrt(nm)


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


# ### Projection function
#
# &#9989; **<font color=red>DO THIS:</font>** Write a function that projects vector $v$ onto vector $u$. 
# Do not use the numpy library. 
# Instead use the functions provided above:
#
# $$\mbox{proj}_u v = \frac{v \cdot u}{u \cdot u} u$$
#
# Make sure this function will work for any size of $v$ and $u$. 

def proj(v,u):
    ## Put your code here
    return pv


# Let's test your function. Below are two example vectors. Make sure you get the correct answers. 
# You may want to test this code with more than one set of vectors. 

u = [1,2,0,3]
v = [4,0,5,8]
print(proj(u,v))

# +
from answercheck import checkanswer

checkanswer.vector(proj(u,v),'53216508af49c616fa0f4e9676ce3b9d');
# -

# ### Visualizing projections
#
# &#9989; **<font color=red>DO THIS:</font>**See if you can design and implement a small function that takes two vectors ($a$ and $b$) as inputs and generates a figure similar to the one above.
#
#
# I.e. a black line from the origin to "$b$", a black line from origin to "$a$"; a green line showing the "$a$" component in the "$b$" direction and a red line showing the "$a$" component orthogonal to the green line. 
# Also see section titled "Projection of One Vector onto Another Vector" in Section 4.6 on page 258 of the book.
#
# When complete, show your solution to the instructor.

# +
# %matplotlib inline
import matplotlib.pylab as plt

b = [3,2]
a = [2,3]

def show_projection(a,b):
    plt.plot([0,a[0]], [0,a[1]], color='black')
    plt.annotate('b', b, 
            xytext=(0.9, 0.7), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
    plt.annotate('a', a, 
            xytext=(0.7, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
    plt.plot([0,b[0]], [0,b[1]], color='black')
    
#Finish your code here

    plt.axis('equal')
    
x = show_projection(a,b) ;


# -

# ----
#
# <a name="Gram-Schmidt_Orthoganalization_Process"></a>
#
# ## 3. Gram-Schmidt Orthoganalization Process
#
# &#9989; **<font color=red>DO THIS:</font>** Implement the Gram-Schmidt orthoganalization process from the [Hefron](http://joshua.smcvt.edu/linearalgebra/book.pdf) textbook (page 282). 
# This function takes a $m \times n$ Matrix $A$ with linearly independent columns as input and return a $m \times n$ Matrix $G$ with orthogonal column vectors. 
# The basic algorithm works as follows:
#
# - ```AT = transpose(A)``` (this process works with the columns of the matrix so it is easier to work with the transpose. Think about a list of list, it is easy to get a row (a list)).  
# - Make a new empty list of the same size as ```AT``` and call it ```GT``` (G transpose)
# - Loop index ```i``` over all of the rows in AT (i.e. columns of A) 
#
#     - ```GT[i] = AT[i]```
#     - Loop index ```j``` from 0 to ```i```
#         - ```GT[i] -= proj(GT[i], GT[j])```
#         
#         
# - ```G = transpose(GT)```
#
# Use the following function definition as a template:

def GramSchmidt(A):
    return G


# Here, we are going to test your function using the vectors:

A4 = [[1,4,8],[2,0,1],[0,5,5],[3,8,6]]
print(transpose(A4))
G4 = GramSchmidt(A4)
print(transpose(G4))

# +
from answercheck import checkanswer

checkanswer.matrix(G4,'a472a81eef411c0df03ae9a072dfa040');
# -

A2 = [[-4,-6],[3,5]]
print(transpose(A2))
G2 = GramSchmidt(A2)
print(transpose(G2))

# +
from answercheck import checkanswer

checkanswer.matrix(G2,'23b9860b72dbe5b84d7c598c08af9688');
# -

# &#9989; **<font color=red>QUESTION:</font>** What is the Big-O complexity of the Gram-Schmidt process? 

# Put your answer here

# ----
#
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
