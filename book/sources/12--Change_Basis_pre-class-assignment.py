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

# # 12 Pre-Class Assignment: Matrix Spaces

# ### Readings for this topic (Recommended in bold)
#  * [Heffron Chapter 2 III pg 114-134](http://joshua.smcvt.edu/linearalgebra/book.pdf)
#  * [**_Beezer Subsection CBM pg 549-549_**](http://linear.ups.edu/download/fcla-3.50-tablet.pdf)
#  * [Boyd Section 5.1 pg 91-95](http://vmls-book.stanford.edu/vmls.pdf)
#

# ### Goals for today's pre-class assignment 
#
# 1. [Properties of Invertible Matrices](#Properties_of_invertible_Matrices)
# 1. [The Basis of a Vector Space](#The_Basis_of_a_Vector_Space)
# 1. [Change of Basis](#Change_of_Basis)
# 1. [Assignment wrap-up](#Assignment_wrap-up)

# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import sympy as sym
sym.init_printing(use_unicode=True)

# ----
# <a name="Properties_of_invertible_Matrices"></a>
#
# ## 1.  Review the Properties of Invertible Matrices
# Let $A$ be an $n \times n$ matrix. The following statements are equivalent.
#
# - The column vectors of $A$ form a basis for $R^n$
# - $|A| \ne 0$
# - $A$ is invertible.
# - $A$ is row equivalent to $I_n$ (i.e. it's reduced row echelon form is $I_n$)
# - The system of equations $Ax = b$ has a unique solution.
# - $rank(A) = n$
#

# Consider the following example. We claim that the following set of vectors form a basis for $R^3$:
#
# $$B = \{(2,1, 4), (-1,6, 0), (2, 4, -3) \}$$
#
# Remember for these two vectors to be a basis they need to obay the following two properties:
#
# 1. They must span $R^3$. 
# 2. They must be linearly independent.
#
# Using the above statements we can show this is true in multiple ways.  

#
# ### The column vectors of $A$ form a basis for $R^n$
#
# &#9989; **<font color=red>DO THIS:</font>** Define a numpy matrix ```A``` consisting of the vectors $B$ as columns:

# +
#Put your answer to the above question here

# +
from answercheck import checkanswer

checkanswer.matrix(A,'94827a40ec59c7d767afe6841e1723ce');
# -

# ### $|A| \ne 0$
#
#
# &#9989; **<font color=red>DO THIS:</font>** The first in the above properties tell us that if the vectors in $B$ are truly a basis of $R^3$ then $|A|=0$. Calculate the determinant of $A$ and store the value in ```det```.

# +
#Put your answer to the above question here
# -

#Verify that the determinate is in fact zero
if np.isclose(det,0):
    print("Since the Determinate is zero the column vectors do NOT form a Basis")
else:
    print("Since the Determinate is non-zero then the column vectors form a Basis.")

# ###  $A$ is invertible.
#
#
# &#9989; **<font color=red>DO THIS:</font>** Since the determinant is non-zero we know that there is an inverse to A.  Use python to calculate that inverse and store it in a matrix called ```A_inv```

# +
#put your answer to the above question here

# +
from answercheck import checkanswer

checkanswer.matrix(A_inv,'001aaddd4824f42ad9d2ccde21cf9d24');
# -

# ### $A$ is row equivalent to $I_n$ (i.e. it's reduced row echelon form is $I_n$)
#

# &#9989; **<font color=red>DO THIS:</font>** According to the property above the reduced row echelon form of an invertable matrix is the Identity matrix.  Verify using the python ```sympy``` library and store the reduced row echelone matrix in a variable called ```rref``` if you really need to check it.

# +
#put your answer to the above question here

# +
from answercheck import checkanswer

checkanswer.matrix(rref,'cde432847c1c4b6d17cd7bfacc457ed1');
# -

# ### The system of equations $Ax = b$ has a unique solution.
#
# Let us assume some arbitrary vector $b \in R^n$.  According to the above properties it should only have one solution.
#
# &#9989; **<font color=red>DO THIS:</font>** Find the solution to $Ax=b$ for the vector $b=(-10,200,3)$. Store the solution in a variable called ```x```

# +
from answercheck import checkanswer

checkanswer.vector(x,'161cfd16545b1b5fb13e35d2800f13df');
# -

# ### $rank(A) = n$
#
# The final property says that the rank should equal the dimension of $R^n$. In our example $n=3$.  Find a ```python``` function to calculate the rank of $A$. Store the value in a variable named ```rank``` to check your answer.
#

# +
#Put your answer to the above quesion here
# -

#Verify that the determinate is in fact zero
if np.isclose(rank,3):
    print("Rank is 3")
else:
    print("Rank is not 3. Did we do something wrong?")

# &#9989; **<font color=red>QUESTION (assignment-specific):</font>** Without doing any calculations (i.e. only using the above properties), how many solutions are there to $Ax=0$?  What is(are) the solution(s)?

# Put your answer to the above question here.

# ----
# <a name="The_Basis_of_a_Vector_Space"></a>
# ## 2. The Basis of a Vector Space
#
# Let $U$ be a vector space with basis $B=\{u_1, \ldots, u_n\}$, and let $u$ be a vector in $U$. 
# Because a basis "spans" the vector space, we know that there exists scalars $a_1, \dots, a_n$ such that:
#
# $$ u = a_1u_1 + \dots + a_nu_n$$
#
# Since a basis is a linearly independent set of vectors we know the scalars $a_1, \dots, a_n$ are unique.
#
# The values $a_1, \dots, a_n$ are called the **coordinates of $u$** relative to the basis ($B$) and is typically written as a column vector:
#
# $$ u_B = 
# \left[
# \begin{matrix}
#     a_1  \\
#     \vdots  \\
#     a_n 
#  \end{matrix}
# \right] 
# $$
#
# We can create a *transition matrix* $P$ using the inverse of the matrix with the basis vectors being columns. 
#
# $$P = [ u_1  \ldots  u_n ]^{-1}$$
#
# Now we will show that matrix $P$ will transition vector $u$ in the standard coordinate system to the coordinates relative to the basis $B$:
#
# $$ u_B = Pu$$

# **_EXAMPLE_**: Consider the vector $u = \left[ \begin{matrix} 5 \\ 3 \end{matrix} \right]$ and the basis vectors $B = \{(1,2), (3,-1)\}$. 
# The following code calculates the $P$ *transition matrix* from $B$ and then uses $P$ to calculate the values of $u_B$ ($a_1$ and $a_2$):
#

u = np.matrix([[5],[3]])
sym.Matrix(u)

B = np.matrix([[1,2],[3,-1]]).T
sym.Matrix(B)

# +
P = np.linalg.inv(B)
ub = P*u

sym.Matrix(ub)
# -

# Here we would like to view this from $R^n$. 
# Let $$B=[u_1 \dots u_n],$$
# then the values of $u_B$ can be found by solving the linear system $$u = B u_B.$$
# The columns of $B$ are a basis, therefore, the matrix $B$ is a $n\times n$ square matrix and it has an inverse. 
# Therefore, we can solve the linear system and obtain 
# $$u_B = B^{-1} u = Pu.$$
#

# Let's try to visualize this with a plot:

# +
ax = plt.axes();


#Blue arrow representing first Basis Vector
ax.arrow(0, 0, B[0,0],B[1,0], head_width=.2, head_length=.2, fc='blue', ec='blue');


#Green arrow representing Second Basis Vector
plt.plot([0,B[0,1]],[0,B[1,1]],color='green'); #Need this line to make the figure work. Not sure why.
ax.arrow(0, 0, B[0,1],B[1,1], head_width=.2, head_length=.2, fc='green', ec='green');

#Original point u as a red dot
ax.scatter(u[0,0],u[1,0], color='red');

plt.show()
#plt.axis('equal');

# -

# Notice that the blue arrow represents the first basis vector and the green arrow is the second basis vector in $B$. 
# The solution to $u_B$ shows 2 units along the blue vector and 1 units along the green vector, which puts us at the point (5,3). 
#
# This is also called a change in coordinate systems.

# &#9989; **<font color=red>QUESTION</font>**: What is the coordinate vector of $u$ relative to the given basis $B$ in $R^3$?
#
# $$u = (9,-3,21)$$
# $$B = \{(2,0,-1), (0,1,3), (1,1,1)\}$$
#
# Store this coordinate in a variable ```ub``` for checking:

# +
#Put your answer here

# +
from answercheck import checkanswer

checkanswer.vector(ub,'f72f62c739096030e0074c4e1dfca159');
# -

# **_Let's look more closely into the matrix $P$, what is the meaning of the columns of the matrix $P$?_**
#
# We know that $P$ is the inverse of $B$, therefore, we have $$BP=I.$$
# Then we can look at the first column of the $P$, say $p_{1}$, we have that $Bp_1$ is the column vector $(1,0,0)^\top$, which  is exactly the first component from the standard basis. 
# This is true for other columns. 
#
# It means that if we want to change an old basis $B$ to a new basis $B'$, we need to find out all the coordinates in the new basis for the old basis, and the transition matrix is by putting all the coordinates as columns.
#
# Here is the matrix $B$ again:

B = np.matrix([[2,0,-1],[0,1,3],[1,1,1]]).T
sym.Matrix(B)

# The first column of P should be the solution to $Bx=\left[ \begin{matrix} 1 \\ 0 \\ 0 \end{matrix} \right]$.  We can use the ```numpy.linalg.solve``` function to find this solution:

# The first column of P should be 
u1 = np.matrix([1,0,0]).T
p1 = np.linalg.solve(B,u1)
p1

# We can find a similar answer for columns $p_2$ and $p_3$:

# The second column of P should be 
u2 = np.matrix([0,1,0]).T
p2 = np.linalg.solve(B,u2)
p2

# The third column of P should be 
u3 = np.matrix([0,0,1]).T
p3 = np.linalg.solve(B,u3)
p3

# concatenate three column together into a 3x3 matrix
P = np.concatenate((p1, p2, p3), axis=1)
sym.Matrix(P)

# Find the new coordinate in the new basis
u = np.matrix([9,-3,21]).T
UB = P*u
print(UB)

# This should be basically the same answer as you got above. 

# ----
# <a name="Change_of_Basis"></a>
#
# ## 3. Change of Basis
#
# Now consider the following two bases in $R^2$:
#
# $$B_1 = \{(1,2), (3,-1)\}$$
# $$B_2 = \{(3,1), (5,2)\}$$
#
# The transformation from the "standard basis" to $B_1$ and $B_2$ can be defined as the column vectors $P_1$ and $P_2$ as follows:
#

# +
B1 = np.matrix([[1,2],[3,-1]]).T
P1 = np.linalg.inv(B1)

sym.Matrix(P1)

# +
B2 = np.matrix([[3,1],[5,2]]).T
P2 = np.linalg.inv(B2)

sym.Matrix(P2)
# -

# &#9989; **<font color=red>DO THIS</font>**: Find the transition matrix $T$ that will take points in the $B_1$ coordinate representation and put them into $B_2$ coordinates.  **_NOTE_** this is analogous to the robot kinematics problem.  We want to represent points in a different coordinate system.

# +
# Put your answer to the above question here.

# +
from answercheck import checkanswer

checkanswer.matrix(T,'dcc03ddff982e29eea6dd52ec9088986')

# -

# &#9989; **<font color=red>QUESTION</font>**: Given $u_{B_1} = \left[ \begin{matrix} 2 \\ 1 \end{matrix} \right]$ (a point named $u$ in the $B_1$ coordinate system) and your calculated transition matrix $T$, what is the same point expressed in the $B_2$ basis (i.e. what is $u_{B2}$)? Store your answer in a variable named ub2 for checking.

ub1 = np.matrix([[2],[1]])
sym.Matrix(ub1)

# +
##Put your code here

# +
from answercheck import checkanswer

checkanswer.vector(ub2,'9a5fe29254c07cf59ebdffcaba679917')
# -

# There are three bases $B_1$, $B_2$, and $B_3$. We have the transition matrix $P_{12}$ from $B_1$ to $B_2$ and the transition matrix $P_{23}$ from $B_2$ to $B_3$. 
# In $R^n$, we can compute the transition matrix as $$P_{12}=B_2^{-1}B_1,\quad P_{23}=B_3^{-1}B_2$$
#
# Then we can find all other transition matrices.
# $$P_{13} = B_3^{-1}B_1=B_3^{-1}B_2*B_2^{-1}B_1= P_{23}P_{12}$$
# $$P_{21} = B_1^{-1}B_2 = (B_2^{-1}B_1)^{-1}=P_{12}^{-1}$$
# $$P_{32} = B_2^{-1}B_3 = (B_3^{-1}B_2)^{-1}=P_{23}^{-1}$$
# $$P_{31} = B_1^{-1}B_3 = (B_3^{-1}B_1)^{-1}=P_{13}^{-1}=(P_{23}P_{12})^{-1}=P_{12}^{-1}P_{23}^{-1}$$
#
# The result is true for general vector spaces and can be extended to many bases.

# ----
#
# <a name="Assignment_wrap-up"></a>
# ## 4. Assignment wrap-up

# &#9989; **<font color=red>Assignment-Specific QUESTION:</font>** Without doing any calculations (i.e. only using the above properties), how many solutions are there to Ax=0? What is(are) the solution(s)?

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

#
#
