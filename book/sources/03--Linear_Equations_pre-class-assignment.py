# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

#

# # 03 Pre-Class Assignment: Linear Equations

# ### Readings for this topic (Recommended in bold)
#  * [Heffron Chapter 1.I, pg 1-2](http://joshua.smcvt.edu/linearalgebra/book.pdf)
#  * [Beezer Chapter SLE pg 1-7](http://linear.ups.edu/download/fcla-3.50-tablet.pdf)
#

# ---
# ### Assignment Overview
# 1. [System of Linear Equations](#System_of_Linear_Equations)
# 1. [Visualizing the problem](#Visualizing_the_problem)
# 1. [Multidimentional Spaces](#Multidimentional_Spaces)
# 1. [Matrixes Notation](#Matrix_Notation)
# 1. [Assignment wrap-up](#Assignment_wrap-up)

# ---
# <a name="System_of_Linear_Equations"></a>
# ## 1. System of Linear Equations
#
# In this course we will spend a lot of time working with systems of linear equations.  A linear equation is in the form:
#
# $$a_1x_1 + a_2x_2 + a_3x_3 + \ldots + a_nx_n = b$$
#
# Where $a_1, a_2, a_3, \ldots a_n$ and $b$ are known constants and $x_1, x_2, x_3, \ldots x_n$ are unknown values.  Typically we have systems of equations with different values of $a$s and $b$s but the unknowns are the same.  For example.  Consider the example of linear equations in the following video. 
#
# &#9989; **<font color=red>TODO:</font>**  Watch the video and follow along in the notebook.

from IPython.display import YouTubeVideo
YouTubeVideo("CH68cc7sH4A",width=640,height=360, cc_load_policy=True)

# > Giselle works as a carpenter and as a blacksmith. She earns 20 dollars per hour as a carpenter and 25 dollars 
# > per hour as a blacksmith. Last week, Giselle worked both jobs for a total of 30 hours, and earned a total of 690 dollars. How long did Giselle work as a carpenter last week, and how long did she work as a blacksmith?
# >
# > - [Brainly.com](https://brainly.com/question/2202719)
#
# This problems gives us two equations and two unknowns:
#
# $$ c + b = 30 $$
# $$ 20c + 25b = 690 $$
#
# How would we solve this in linear algebra?  
#
# $$ c + b = 30$$
# $$ 20c + 25b = 690$$
#
# First, we can multiply the first equation by -20 and add to the second equation.  This is often called a "linear combination" of the two equations. The operation does not change the answer:
#
# $$ -20c - 20b = -600$$
# $$ 20c + 25b = 690$$
# $$----$$
# $$ 0c + 5b = 90$$
#
# This is our new system of equations:
# $$ c + b = 30$$
# $$ 0c + 5b = 90$$
#
# Now we can easily divide the second equation by 5 and get the value for $b$:
#
# $$b = 90/5 = 18$$
#
# If we substitute 18 for $b$ into the first equation we get:
# $$ c + 18 = 30$$
#
# And solving for $c$ gives us $c = 30-18=12$.  Let's check to see if this works by substituting $b=18$ and $c=12$ into our original equations:
#
# $$ 12 + 18 = 30$$
# $$ 20(12) + 25(18) = 690$$

# Let's check the answer using Python:

b = 18
c = 12

c + b == 30

20*c + 25*b == 690

# &#9989; **<font color=red>QUESTION:</font>**  The above video described three (3) elementary operators that can be applied to a system of linear equations and not change their answer.  What are these three operators?  

# **_Erase the contents of this cell and put your answer to the above question here_**

# ---
# <a name="Visualizing_the_problem"></a>
# ## 2.  Visualizing the problem
# We can visualize the solution to a system of linear equations in a graph. If we make $b$ the "$y$"-axis and $c$ the "$x$"-axis. For each equation, we calculate the $b$ value for each $c$, and two equations give us two lines. 
#
# **Note:** This is sometimes called the "Row Picture." I will ask you why it has this name in class so think about it.
#
#
# &#9989; **<font color=red>QUESTION:</font>**  The above video described three (3) elementary operators that can be applied to a system of linear equations and not change their answer.  What are these three operators? 
#

from IPython.display import YouTubeVideo
YouTubeVideo("BSxWO6FGib0",width=640,height=360, cc_load_policy=True)

# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np

c = np.linspace(0,20)
c

b1 = 30-c
b2 = (690-20*c)/25

# ### Row Picture

plt.plot(c,b1)
plt.plot(c,b2)
plt.xlabel('c (hours worked as carpenter)')
plt.ylabel('b (hours worked as blacksmith)')
plt.scatter(12,18);

#
# Now, consider the next set of equations which do not have a solution
#
# $$-2x+y=3$$
# $$-4x+2y=2$$
#

x = np.linspace(-10,10)
y1 =  3+2*x
y2 = (2+4*x)/2
plt.plot(x,y1)
plt.plot(x,y2);

from IPython.display import YouTubeVideo
YouTubeVideo("Z9gkovHDpIQ",width=640,height=360, cc_load_policy=True)

# Consider the next set of equations which have infinite many solutions
#
# $$4x-2y=6$$
# $$6x-3y=9$$
#

x = np.linspace(-10,10)
y1 =  (4*x-6)/2
y2 = (6*x-9)/3
plt.plot(x,y1)
plt.plot(x,y2)

# &#9989; **<font color=red>DO THIS:</font>**  Plot the following equations from -100 to 100
#
# $$ 18x+21y = 226$$
# $$ 72x-3y = 644$$

# +
# Put your python code here
# -

# &#9989; **<font color=red>QUESTION:</font>**  Using the graph, what is a visual estimation of the solution to these two equations?  Hint, you may want to change the $x$ range to "zoom" in on the intersection. 

# **_Put your answer to the above question here._**

# ### Column Picture
#
# I think a good programmer is a lazy person. Let's avoid writing all of the letters in the above equation by changing it into a column vector format as follows.
#

# $$ 
# c
# \left[
# \begin{matrix}
#     1 \\ 20  
#  \end{matrix}
# \right]
# +
# b
# \left[
# \begin{matrix}
#     1 \\ 5  
#  \end{matrix}
# \right]
# =
# \left[
# \begin{matrix}
#  30 \\ 330
# \end{matrix}
# \right]
# $$

# Notice that this still represents the same system of equations. We just write the constants as column vectors and we only have to write the unknowns once (Since they are the same for all equations). 

# Let's plot this "column picture", which shows how the above equation is a "linear combination" of the two column vectors.  
#
# One way to think about this is we can only move in straight lines in two directions. The first direction is (1,20) and the second is (1,5).  The solution to the problem is how far in each direction we need to move to arrive at our final destination of (30,330).
#
# The first column is a vector in the (1,20) direction. The variable $c$ is how far in the (1,20) direction we want to go.  Then $b$ is how far in the (1,5) direction we want to go to arrive at the point (30,330).
#
# We will use the ```matplotlib``` function ```arrow``` to plot the vectors.  The arrow function takes a starting point $[x,y]$ and a direction $[dx,dy]$ as inputs and draws an arrow from the starting point in the direction specified.

# First thing to do is plot the first column as a vector. From the origin (0,0) to $c\left[
# \begin{matrix}
#     1 \\ 20  
#  \end{matrix}
# \right]$
#
# **or** $x = c$ and $y = 20c$ with $c=12$

# +
c = 12

#hack to initialize bounds of plot (need this to get the arrows to work?)
plt.plot(0,0)
plt.plot(30,330)

# Plot the first arrow 
plt.arrow(0, 0, c*1, c*20,head_width=2, head_length=10, fc='blue', ec='blue')
# -

# Next thing to do is plot the second column as a vector by adding it to the first. This ```arrow``` will start at the end of the previous vector and "add" the second column vector:

# +
b = 18

#hack to initialize bounds of plot (need this to get the arrows to work?)
plt.plot(0,0)
plt.plot(30,330)

# Plot the first arrow
plt.arrow(0, 0, c*1, c*20,head_width=2, head_length=10, fc='blue', ec='blue')

#Plot the second arrow starting at the end of the first
plt.arrow(c, c*20, b*1, b*5, head_width=2, head_length=10, fc='red', ec='red')
# -

# The takeaway to this figure is that these two column vectors, when added together, end up at the point that represents the right hand side of the above equation (i.e. (30, 330)). 

# +
#hack to initialize bounds of plot (need this to get the arrows to work?)
plt.plot(0,0)
plt.plot(30,330)

# Plot the first arrow
plt.arrow(0, 0, c*1, c*20,head_width=2, head_length=10, fc='blue', ec='blue')

#Plot the second arrow starting at the end of the first
plt.arrow(c, c*20, b*1, b*5, head_width=2, head_length=10, fc='red', ec='red')

#Plot a righthand column vector as a point.
plt.arrow(0,0, 30, 330, head_width=2, head_length=10, fc='purple', ec='purple')
plt.xlabel('x');
plt.ylabel('y');
# -

# We say that the two column vectors "**span**" the $xy$-plane.  This means that any point on the x,y plane can be represented as a linear combination of the two vectors.  
#
# &#9989; **<font color=red>QUESTION:</font>** Give an example of two column vectors that do **NOT** span the $xy-$plane:

# **_Put your answer to the above question here._**

# ---
# <a name="Multidimentional_Spaces"></a>
# ## 4. Multidimentional Spaces

from IPython.display import YouTubeVideo
YouTubeVideo("A3fHytkJ010",width=640,height=320, cc_load_policy=True)

# &#9989; **<font color=red>QUESTION:</font>**  Describe in words, what the solution space would look like for three equations with three unknowns and no solutions.

# **_Erase the contents of this cell and put your answer to the above question here._**

# ---
# <a name="Matrix_Notation"></a>
# ## 5.  Matrix Notation
#
# Review **_Sections 6.1 - 6.3_** of the [Stephen Boyd and Lieven Vandenberghe Applied Linear algebra book](http://vmls-book.stanford.edu/) which introduces the concept of Matrices.  Some things to take away include:
#
# * Basic Matrix composition
# * Transpose Addition and norms
# * Zero and Identy matrix
#

from IPython.display import YouTubeVideo
YouTubeVideo("uC46qAjdE9w",height=360,width=640, cc_load_policy=True)

# A matrix is a rectangular array of numbers typically written between rectangular brackets such as:
#
# $$ A = 
# \left[
# \begin{matrix}
#     0 & -1 \\ 
#     3 & 4 \\
#     0 & 2
#  \end{matrix}
# \right]^{ 3\times 2}
# $$
#
# The $3 \times 2$ subscript is not always included but is handy notation to remember the size of a matrix.  The size of a matrix is always written $m \times n$ where $m$ is the number of rows and $n$ is the number of columns.  So in the above case Matrix $A$ is a $3 \times 2$  (read "three by two") matrix.  

# &#9989; **<font color=red>QUESTION:</font>**  What is the size of the following matrix?
#
#
# $$ B = 
# \left[
# \begin{matrix}
#     0 & -1 & 0\\ 
#     3 & 4 & 2\\
#  \end{matrix}
# \right]
# $$

# **_Erase the contents of this cell and put your answer to the above question here_**

# Each element in a matrix can be referenced by it's index location.  Similar to the size of a matrix the location of an element is described by two numbers, it's row followed by it's column.  Counting for the rows start at the top and the columns start on the left.  For example, in Matrix $B$ element $b_{1,2}$ is the number in row 1 column 2 which is -1.  

# &#9989; **<font color=red>QUESTION:</font>**  What is the value of element (2,1) in matrix $B$? 

# **_Erase the contents of this cell and put your answer to the above question here_**

# A linear system of equations can be written in matrix format.  For example, the equations in the original example can be written as the following "Augmented matrix"
#
# $$ 
# \left[
# \begin{matrix}
#     1 & 1 \\ 
#     20 & 25
#   \end{matrix}
# \, \middle\vert \,
# \begin{matrix}
#  30 \\ 
#  690
# \end{matrix}
# \right] 
# $$
#
# And the example which included silversmith can be written as follows:
# $$ 
# \left[
# \begin{matrix}
#     1 & 1 & 1 \\ 
#     50 & 20 & 25 \\
#     110 & 0 & 20
#   \end{matrix}
# \, \middle\vert \,
# \begin{matrix}
#  30 \\ 
#  690 \\
#  300
# \end{matrix}
# \right] 
# $$
# The above equations are represented as "augmented matrices" with the equal side represented as a vertical line.  

# The general matrix format for a system of linear equations can be written as follows:
#
# $$ 
# X = 
# \left[
# \begin{matrix}
#     x_{11}       & x_{12} & x_{13} & \dots  \\
#     x_{21}       & x_{22} & x_{23} & \dots \\
#     \ldots       & \ldots & \ldots & \ddots \\
#     x_{m1}       & x_{m2} & x_{m3} & \dots 
#  \end{matrix}
# \, \middle\vert \,
# \begin{matrix}
# x_{1n} \\ x_{2n} \\ \ldots \\ x_{mn}
# \end{matrix}
# \right] ^{mxn}
# $$
#
# where $x_{ij}$ is a scalar element in the matrix.

# Now consider the following system of linear equations:
#
# $$x_1 = 2.14159$$
# $$x_2 = 4$$
# $$x_3 = -7.2$$
# $$x_4 = 69$$
# $$x_5 = 84$$
# $$x_6 = 240$$
#
# Lets rewrite this equation as an augmented matrix:
#
#
# $$ 
# X = 
# \left[
# \begin{matrix}
#     1 & 0 & 0 & 0  & 0 & 0  \\
#     0 & 1 & 0 & 0  & 0 & 0  \\
#     0 & 0 & 1 & 0  & 0 & 0  \\
#     0 & 0 & 0 & 1  & 0 & 0  \\
#     0 & 0 & 0 & 0  & 1 & 0  \\
#     0 & 0 & 0 & 0  & 0 & 1  
#  \end{matrix}
# \, \middle\vert \,
# \begin{matrix}
# 2.14159 \\ 4 \\ -7.2 \\ 69 \\ 84 \\ 240
# \end{matrix}
# \right] ^{6x7}
# $$
#
# Notice the submatrix on the left hand side is just the $I_6$ identity matrix and the right hand side are the solutions. 

# ----
#
# <a name="Assignment_wrap-up"></a>
# ## 6. Assignment wrap-up

# &#9989; **<font color=red>Assignment-Specific QUESTION:</font>**  What are the three elementary operators that can be applied to systems of linear equations that do not change their answer?

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
