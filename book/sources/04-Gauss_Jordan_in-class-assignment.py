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

# [Link to this document's Jupyter Notebook](04-Gauss_Jordan_in-class-assignment.ipynb)

#

# # 04 In-Class Assignment: Linear Algebra and Python
#
# <img src="https://i.ytimg.com/vi/fSCz7jH_vHI/maxresdefault.jpg" width="70%" alt="Image showing an instructor writing on the board instruction for Gauss-Jordan.  These include 1) 1 Row 1 column 1 2) Kill the rest of the column 3) 1 Row 2 Column 2 4) Kill the rest of the column 4) Answer as a point (x,y).  Although not really an algorithm these instructions give a general idea of how Gauss-Jordan works">
#
# Image from:  Mathbyfives @[YouTube](https://www.youtube.com/watch?v=fSCz7jH_vHI)
#     
#
#     

# ### Agenda for today's class (80 minutes)
#
# 1. (20 minutes) [Pre Class Review](#Pre-Class-Review)
# 2. (20 minutes) [Solving Systems of Linear Equations](#Solving-Systems-of-Linear-Equations)
# 3. (20 minutes) [Underdetermined Systems](#Underdetermined-Systems)
# 4. (20 minutes) [Practice   Curve Fitting Example](#Practice---Curve-Fitting-Example)
#

#
# ---
# <a name=Pre-Class-Review></a>
# ## 1. Pre Class Review
#
#
#
# Today we will go over our quiz from last week.

# Here are some libraries you may need to use
# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import sympy as sym
import math
sym.init_printing()

#
#
# ---
# <a name=Solving-Systems-of-Linear-Equations></a>
# ## 2. Solving Systems of Linear Equations
#
#
# Remember the following set of equations from the mass weight example:
#
# <img src="https://lh4.googleusercontent.com/48AcnVEBkzXJ_heu4fR0DbP5BBunyRlzPsTeK8WSBsMTSjZ5QNhdhtnVsdAw7wD0NBITIiSmh9Jn0gTPABkxqDa-LrhRicZGdpfbYakgWjJetZfOPk636Eu-vjmj=w740" align="center" width="70%" alt="Image showing two balanced beams, each with three weights. In the top beam is unknown weight A is a distance of 40 to the left of the fulcrum, unknown weight B is a distance of 15 to the left of the fulcrum and a weight of 2 is 50 to the right of the fulcrum. In the bottom beam is the same unknown weights.  Weight A is now a distance of 50 to the right of the fulcrum, weight B is a distance of 25 to the left of the fulcrum and the weight of 2 is a distance of 25 to the right of the fulcrum.">
# $$40A + 15B = 100$$
# $$25B = 50 + 50A$$
#

# As you know, the above system of equations can be written as an Augmented Matrix in the following form:
#
#
# $$ 
# \left[
# \begin{matrix}
#     40  & 15  \\
#     -50 & 25  
#  \end{matrix}
# \, \middle\vert \,
# \begin{matrix}
# 100 \\ 50 
# \end{matrix}
# \right] 
# $$
#
#

# &#9989; **<font color=red>QUESTION:</font>**  Split apart the augmented matrix  ($ 
# \left[
# \begin{matrix}
#     A
#  \end{matrix}
# \, \middle\vert \,
# \begin{matrix}
# b
# \end{matrix}
# \right] 
# $) into it's left size ($2 \times 2$) matrix $A$ and it's right ($2x1$) matrix $b$. Define the matrices $A$ and $b$ as ```numpy``` matrices:

# +
#Put your code here

# +
from answercheck import checkanswer

checkanswer.matrix(A,'f5bfd7c52824d5ac580d0ce1ab98fe68');

# +
from answercheck import checkanswer

checkanswer.matrix(b,'c760cd470439f5db82bb165edf4dc3f8');
# -

# &#9989; **<font color=red>QUESTION:</font>**  solve the above system of equations using the ```np.linalg.solve``` function and store the value in a vector named x:

# +
# Put your code to the above question here

# +
from answercheck import checkanswer

checkanswer.vector(x,'fc02fe6d0577c4452ee70252e1e17654');
# -

#
#
# ---
# <a name=Underdetermined-Systems></a>
# ## 3. Underdetermined Systems
#
#
#
#
# Sometimes we have systems of linear equations where we have more unknowns than equations, in this case we call the system "underdetermined." These types of systems can have infinite solutions.  i.e., we can not find an unique $x$ such that $Ax=b$. In this case, we can find a set of equations that represent all of the solutions that solve the problem by using Gauss Jordan and the Reduced Row Echelon form. Lets consider the following example:
#
#
# $$\begin{bmatrix}5&-2&2 & 1 \\ 4 & -3 &4 &2  \\ 4& -6 &7  & 4\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\\x_4\end{bmatrix}=\begin{bmatrix}1\\2\\3\end{bmatrix}$$
#
#
#
# &#9989; **<font color=red>QUESTION</font>** Define an augmented matrix $M$ that represents the above system of equations:

# +
#Put your code here
# -

# &#9989; **<font color=red>QUESTION</font>** What is the Reduced Row Echelon form for A?

# +
from answercheck import checkanswer

checkanswer.matrix(M,'efb9b2da0e44984a18f595d7892980e2');

# +
# Put your answer to the above question here

# +
from answercheck import checkanswer

checkanswer.matrix(RREF,'f1fa8baac1df4c378db20cff9e91ca5b');
# -

# Notice how the above RREF form of matrix A is different from what we have seen in the past.  In this case not all of our values for $x$ are unique. When we write down a solution to this problem by defining the variables by one or more of the undefined variables.  for example, here we can see that $x_4$ is undefined.  So we say $x_4 = x_4$, i.e. $x_4$ can be any number we want.  Then we can define $x_3$ in terms of $x_4$.  In this case $x_3 = \frac{11}{15} - \frac{4}{15}x_4$.  The entire solution can be written out as follows:
#
# $$
# \begin{align*} 
# x_1 &= \frac{1}{15} + \frac{1}{15}x_4 \\
# x_2 &= \frac{2}{5} + \frac{2}{5}x_4 \\
# x_3 &= \frac{11}{15} - \frac{4}{15}x_4 \\
# x_4 &= x_4 
# \end{align*}
# $$

# &#9989; **<font color=red>DO THIS</font>** Review the above answer and make sure you understand how we get this answer from the Reduced Row Echelon form from above. 

# Sometimes, in an effort to make the solution more clear, we introduce new variables (typically, $r,s,t$) and substitute them in for our undefined variables so the solution would look like the following:
#
#
# $$
# \begin{align*} 
# x_1 &= \frac{1}{15} + \frac{1}{15}r \\
# x_2 &= \frac{2}{5} + \frac{2}{5}r \\
# x_3 &= \frac{11}{15} - \frac{4}{15}r \\
# x_4 &= r 
# \end{align*}
# $$

# We can find a particular solution to the above problem by inputing any number for $r$.  For example, set r equal to zero and create a vector for all of the $x$ values.
#
#
# $$
# \begin{align*} 
# x_1 &= \frac{1}{15}\\
# x_2 &= \frac{2}{5}\\
# x_3 &= \frac{11}{15}  \\
# x_4 &= 0
# \end{align*}
# $$

# +
##here is the same basic math in python

r = 0
x = np.matrix([1/15+1/15*r, 2/5+2/5*r, 11/15-4/15*r, r]).T
x
# -

# &#9989; **<font color=red>DO THIS</font>** Define two more matrixes $A$, $b$ representing the above system of equations $Ax=b$:

# +
# put your answer to the above question here.

# +
from answercheck import checkanswer

checkanswer.matrix(A,'a600d0416a3fb9b4bde87b08caf068f1');

# +
from answercheck import checkanswer

checkanswer.vector(b,'4cfaa788e4dd6de04fdf6aea4a0e0e71');
# -

# Now let us check our answer by multipying matrix $A$ by our solution $x$ and see if we get $b$

np.allclose(A*x,b)

# &#9989; **<font color=red>DO THIS</font>** Now go back and pick a different value for $r$ and see that it also produces a valid solution for $Ax=b$.

#
# ---
# <a name=Practice---Curve-Fitting-Example></a>
# ## 4. Practice   Curve Fitting Example
#
# Consider the following polynomial with constant scalars $a$, $b$, and $c$, that falls on the $xy$-plane:
#
# $$f(x) = ax^2 + bx + c$$
#

# &#9989; **<font color=red>QUESTION:</font>**  Is this function linear? Why or why not?

# Put your answer to the above question here.

# Assume that we do not know the values of $a$, $b$ and $c$, but we do know that the points (1,2), (-1,12), and (2,3) are on the polynomial. We can substitute the known points into the equation above. For example, using point (1,2) we get the following equation:
#
# $$2 = a1^2 + b1 + c$$
# $$\text{or}$$
# $$2 = a + b + c$$
#
# &#9989; **<font color=red>QUESTION:</font>**  Generate two more equations by substituting points (-1,12) and (2,3) into the above equation:

# Put your answer to the above question here. (See if you can use latex as I did above)

# &#9989; **<font color=red>QUESTION:</font>**  If we did this right, we should have three equations and three unknowns ($a,b,c$).  Note also that these equations are linear (how did that happen?).  Transform this system of equations into two matrices $A$ and $b$ like we did above.

# +
#Put your answer to the above question here.

# +
from answercheck import checkanswer

checkanswer.matrix(A,'1896041ded9eebf1cba7e04f32dd1069');

# +
from answercheck import checkanswer

checkanswer.matrix(b,'01e594bb535b4e2f5a04758ff567f918');
# -

# &#9989; **<font color=red>QUESTION</font>** Write the code to solve for $x$ (i.e., ($a,b,c$)) using ```numpy```.

# +
#Put your answer to the above question here.

# +
from answercheck import checkanswer

checkanswer.vector(x,'1dab22f81c2c156e6adca8ea7ee35dd7');
# -

# &#9989; **<font color=red>QUESTION</font>** Given the value of your ```x``` matrix derived in the previous question, what are the values for $a$, $b$, and $c$?

#Put your answer to the above question here.
a = 0
b = 0
c = 0

# Assuming the above is correct, the following code will print your 2nd order polynomial and plot the original points:

# +
x = np.linspace(-3,3)
y = a*x**2 + b*x + c

#plot the function. (Transpose is needed to make the data line up).
plt.plot(x,y.transpose())

#Plot the original points
plt.scatter(1, 2)
plt.scatter(-1, 12)
plt.scatter(2, 3)
plt.xlabel('x-axis')
plt.ylabel('y-axis')


# -

# &#9989; **<font color=red>QUESTION</font>** The following program is intended to take four points as inputs ($p1, p2, p3, p4 \in R^2$) and calculate the coefficients $a$, $b$, $c$, and $d$ so that the graph of $f(x) = ax^3 + bx^2 + cx + d$ passes smoothly through the points.  Test the function with the following points (1,2), (-1,6), (2,3), (3,2) as inputs and print the values for $a$, $b$, $c$, and $d$.

def fitPoly3(p1,p2,p3,p4):
    A = np.matrix([[p1[0]**3, p1[0]**2, p1[0], 1],
                   [p2[0]**3, p2[0]**2, p2[0], 1],
                   [p3[0]**3, p3[0]**2, p3[0], 1],
                   [p4[0]**3, p4[0]**2, p4[0], 1]])
    
    b = np.matrix([p1[1],p2[1],p3[1],p4[1]]).T

    X = np.linalg.solve(A, b)
    a = X[0]
    b = X[1]
    c = X[2]
    d = X[3]
    #Try to put your figure generation code here for the next question 
    #####Start your code here #####
    
    
    #####End of your code here#####       
    return (a,b,c,d)

# +
#put your answer to the above question here
# -

# &#9989; **<font color=red>QUESTION</font>** Modify the above ```fitpoly3``` function to also generate a figure of the input points and the resulting polynomial in range ```x=(-3,3)```. 

# +
# Put the answer to the above question above or copy and paste the above function and modify it in this cell. 
# -

# &#9989; **<font color=red>QUESTION</font>** Give any four $R^2$ input points to ```fitPoly3```, is there always a unique solution?  Explain your answer. 

# Put your answer to the above question here.

# ----
#
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
