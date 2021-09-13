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

# # 09 In-Class Assignment: Determinants
#
# <img src="http://www.mathnstuff.com/math/algebra/gif/asys1.gif" alt="Depiction of Cramer's Rule with two equations and two variables">  
#
# Image from:[http://www.mathnstuff.com/](http://www.mathnstuff.com/)  
#  

# ### Agenda for today's class (80 minutes)
#
# 1. [(20 minutes) Review Pre-class Assignment](#Review_Pre-class_Assignment)
# 1. [(30 minutes) Algorithm to calculate the determinant](#Algorithm_to_calculate_the_determinant)
# 1. [(30 minutes) Using Cramer's rule to solve $Ax=b$](#Using_Cramers_rule)
#

# ----
#
# <a name="Review_Pre-class_Assignment"></a>
# ## 1. Review Pre-class Assignment
#
# * [09--Determinants_pre-class-assignment.ipynb](09--Determinants_pre-class-assignment.ipynb)

# ---
# <a name="Algorithm_to_calculate_the_determinant"></a>
# ## 2. Algorithm to calculate the determinant
# Consider the following recursive algorithm (algorithm that calls itself) to determine the determinate of a $n\times n$ matrix $A$ (denoted $|A|$), which is the sum of the products of the elements of any row or column. i.e.:
#
# $$i^{th}\text{ row expansion:     } |A| = a_{i1}C_{i1} + a_{i2}C_{i2} + \ldots + a_{in}C_{in} $$
# $$j^{th}\text{ column expansion:     } |A| = a_{1j}C_{1j} + a_{2j}C_{2j} + \ldots + a_{nj}C_{nj} $$
#
# where $C_{ij}$ is the cofactor of $a_{ij}$ and is given by:
#
# $$ C_{ij} = (-1)^{i+j}|M_{ij}|$$
#
# and $M_{ij}$ is the matrix that remains after deleting row $i$ and column $j$ of $A$.
#
# Here is some code that tries to implement this algorithm.  

## Import our standard packages packages
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
sym.init_printing(use_unicode=True)

# +
import copy
import random

def makeM(A,i,j):
    ''' Deletes the ith row and jth column from A'''
    M = copy.deepcopy(A)
    del M[i]
    for k in range(len(M)):
        del M[k][j]
    return M

def mydet(A):
    '''Calculate the determinant from list-of-lists matrix A'''
    if type(A) == np.matrix:
        A = A.tolist()   
    n = len(A)
    if n == 2:
        det = (A[0][0]*A[1][1] - A[1][0]*A[0][1]) 
        return det
    det = 0
    i = 0
    for j in range(n):
        M = makeM(A,i,j)
        
        #Calculate the determinant
        det += (A[i][j] * ((-1)**(i+j+2)) * mydet(M))
    return det


# -

# The following code generates an $n \times n$ matrix with random values from 0 to 10.  
# Run the code multiple times to get different matrices:

#generate Random Matrix and calculate it's determinant using numpy
n = 5
s = 10
A = [[round(random.random()*s) for i in range(n)] for j in range(n)]
A = np.matrix(A)
#print matrix
sym.Matrix(A)


# &#9989; **<font color='red'>DO THIS:</font>** Use the randomly generated matrix ($A$) to test the above ```mydet``` function and compare your result to the ```numpy.linalg.det``` function.

# +
# Put your test code here
# -

# &#9989; **<font color=red>QUESTION:</font>** Are the answers to ```mydet``` and ```numpuy.linalg.det``` exactly the same every time you generate a different random matrix?  If not, explain why.

# Put your answer here

# &#9989; **<font color=red>QUESTION:</font>** On line 26 of the above code, you can see that algorithm calls itself.  Explain why this doesn't run forever.

# Put your answer here

# ---
#
# <a name="Using_Cramers_rule"></a>
# ## 3. Using Cramer's rule to solve $Ax=b$
#
# Let $Ax = b$ be a system of $n$ linear equations in $n$ variables such that $|A| \neq 0$. the system has a unique solution given by:
#
# $$x_1 = \frac{|A_1|}{|A|}, x_2 = \frac{|A_2|}{|A|}, \ldots,  x_n = \frac{|A_n|}{|A|}$$
#
# where $A_i$ is the matrix obtained by replacing column $i$ of $A$ with $b$. The following function generates $A_i$ by replacing the $i$th column of $A$ with $b$:

def makeAi(A,i,b):
    '''Replace the ith column in A with b'''
    if type(A) == np.matrix:
        A = A.tolist()
    if type(b) == np.matrix:
        b = b.tolist()
    Ai = copy.deepcopy(A)
    for j in range(len(Ai)):
        Ai[j][i] = b[j][0]
    return Ai


# &#9989; **<font color=red>DO THIS:</font>** Create a new function called ```cramersRule```, which takes $A$ and $b$ and returns $x$ using the Cramer's rule. **Note:** Use ```numpy``` and NOT ```mydet``` to find the required determinants. ```mydet``` is too slow. 

# +
# Stub code. Replace the np.linalg.solve code with your answer

def cramersRule(A,b):
    detA = np.linalg.det(A)
    x = []    
    #####Start of your code here#####  
 

    #####End of your code here#####  
    
    return x
# -

# &#9989; **<font color=red>QUESTION:</font>** Test your ```cramersRule``` function on the following system of linear equations:
#
# $$ x_1 + 2x_2 = 3$$
# $$3x_1 + x_2 = -1$$

# +
#Put your answer to the above quesiton here
# -

# &#9989; **<font color=red>QUESTION:</font>** Verify the above answer by using the ```np.linalg.solve``` function:

# +
#Put your answer to the above quesiton here
# -

# &#9989; **<font color=red>QUESTION:</font>** Test your ```cramersRule``` function on the following system of linear equations and verify the answer by using the ```np.linalg.solve``` function: 
#
# $$ x_1 + 2x_2 +x_3 = 9$$
# $$ x_1 + 3x_2 - x_3 = 4$$
# $$ x_1 + 4x_2 - x_3 = 7$$

# +
#Put your answer to the above quesiton here
# -

# &#9989; **<font color=red>QUESTION:</font>** Cramer's rule is a $O(n!)$ algorithm and the Gauss-Jordan (or Gaussian) elimination is $O(n^3)$.  What advantages does Cramer's rule have over elimination?

# Put your answer here.

# ----
#
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
