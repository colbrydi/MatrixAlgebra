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

# # 03 In-Class Assignment: Solving Linear Systems of equations
#
# In the movie Groundhog day the main character "Phil" repeats the same day over and over again.  This is an iterative process where Phil learns from past mistakes until he has a "perfect" day.  The Groundhog movie is a fun analogy of iterative methods for solving linear equations.  In this class we will write our own iterative method. 

# ### Agenda for today's class (80 minutes)
#
# </p>
#
# 1. [(30 minutes) Review pre-class assignment](#Pre-class_assignment_review)
# 1. [(30 minutes) Jacobi Method for solving Linear Equations](#Jacobi_Method_for_solving_Linear_Equations)
# 1. [(20 minutes) Numerical Error](#Numerical_Error)

# ---
# <a name="Pre-class_assignment_review"></a>
# ## 1. Pre-class assignment review
#
#
# [03--Linear_Equations_pre-class-assignment.ipynb](03--Linear_Equations_pre-class-assignment.ipynb)
#

# ---
# <a name="Jacobi_Method_for_solving_Linear_Equations"></a>
#
# ## 2. Jacobi Method for solving Linear Equations
#
# During class today we will write an iterative method (named after Carl Gustav Jacob Jacobi) to solve the following system of equations:
#
# $$ 6x + 2y - ~z = 4~$$
# $$~ x + 5y + ~z = 3~$$
# $$ 2x +~ y + 4z = 27$$
#
# Here is a basic outline of the Jacobi method algorithm:
#
# 1. Initialize each of the variables as zero ($x_0 = 0, y_0 = 0, z_0 = 0$) 
# 2. Calculate the next iteration using the above equations and the values from the previous iterations. For example here is the formula for calculating $x_i$ from $y_{(i-1)}$ and $z_{(i-1)}$ based on the first equation:
#     $$x_i = \frac{4 - 2y_{(i-1)} + z_{(i-1)}}{6} $$
#     Similarly, we can obtain the update for $y_i$ and $z_i$ from the second and third equations, respectively.
# 3. Increment the iteration counter $(i = i + 1)$ and repeat Step 2.
# 4. Stop when the answer "converges" or a maximum number of iterations has been reached. (ex. $i$ = 100)
#
# **IMPORTANT NOTE:** 
#
# > A sufficient (but not necessary) condition for the method to converge is that the matrix A is strictly or irreducibly [diagonally dominant](https://en.wikipedia.org/wiki/Diagonally_dominant_matrix). Strict row diagonal dominance means that for each row, the absolute value of the diagonal term is greater than the sum of absolute values of other terms. - From [Wikipedia](https://en.wikipedia.org/wiki/Jacobi_method)
#
# In other words, the Jacobi Methid will not work an all problems.  

# &#9989; **<font color=red>DO THIS:</font>** Write out the equations for $x_i$, $y_i$, and $z_i$ based on $x_{(i-1)}$, $y_{(i-1)}$, and $z_{(i-1)}$. 

# Put your answer to the above question here.

# &#9989; **<font color=red>DO THIS:</font>** Complete the following code by adding formulas for $y_i$ and $z_i$ to solve the above equations using the Jacobi method.  

# +
# %matplotlib inline
import matplotlib.pylab as plt

x = []
y = []
z = []

#step 1: inicialize to zero
x.append(0)
y.append(0)
z.append(0)

for i in range(1,100):
    xi = (4 - 2*y[i-1]+ z[i-1])/6
#####Start your code here #####
    yi = 0 #Change this line
    zi = 0 #Change this line
#####End of your code here#####        
    #Add latest value to history
    x.append(xi)
    y.append(yi)
    z.append(zi)

#Plot History of values
plt.plot(x, label='x')
plt.plot(y, label='y')
plt.plot(z, label='z')
plt.xlabel('Iteration')
plt.ylabel('Value')
plt.legend(loc=1);
# -

#  &#9989; **<font color=red>QUESTION:</font>**  What are the final values for $x$, $y$, and $z$?
#
# $$x = $$
# $$y = $$
# $$z = $$

# &#9989; **<font color=red>DO THIS:</font>** Write out each of the above equations and show that your final result is a solution to the system of equations:

# +
# Put your code here
# -

#  &#9989; **<font color=red>QUESTION:</font>**  By inspecting the graph, how long did it take for the algorithum to converge to a solution?  

# Put your answer to the above question here.

#  &#9989; **<font color=red>QUESTION:</font>**  How could you rewrite the above program to stop earlier.  

# Put your answer to the above question here.

# ---
# <a name="Numerical_Error"></a>
#
# ## 3. Numerical Error
#
# Consider the following python statement when answering the questions below:

0.1 + 0.2 == 0.3

#  &#9989; **<font color=red>QUESTION:</font>**  Why does Python return **False** even though the above statement is clearly true?

# Put your answer to the above question here.

#  &#9989; **<font color=red>DO THIS:</font>** Let's consider another example.  Run the following code which should return true.  

# +
import numpy as np
J = np.array([20])
L = [20]

pow(L[0],8) == pow(J[0],8)
# -

# If you have an older version of ```numpy``` installed (like 1.18.5) then the results of running the above cell may be false (did anyone get this result?).  This is because ```numpy```
# changed how it handles something called "roundoff error". here is another cell that may help you see better what is going on:

import numpy as np
J = np.array([20])
L = [20]
print(pow(20,8))
print(pow(L[0],8))
print(pow(J[0],8))


# The older version of ```numpy``` would return the following:
#
# ```
# 25600000000
# 25600000000
# -169803776
# ```
# We could say to always upgrade to the latest stable version (generally a good idea). But some other libraries that depend on numpy may not be up to date so sometimes python will install an older version to maintain compatibility. For example, one really popular program is tensorflow, which often requires an older version of numpy. 

#  &#9989; **<font color=red>QUESTION:</font>** If Python is sometimes wrong, why do we use it? 

# Put your answer to the above question here.

#  &#9989; **<font color=red>QUESTION:</font>** What are ways you can do to watch out for these types of errors?  

# Put your answer to the above question here.

#  &#9989; **<font color=red>QUESTION:</font>** Modify the following program to return **True** if the values are within some small number (```e```) of each other.

# +
def checktrue(a,b,e=0.001):
    return a == b

#Test function
checktrue(0.1+0.2, 0.3)
# -

#  &#9989; **<font color=red>QUESTION:</font>** What is a good value to set for ```e``` and why?

# Put your answer to the above question here.

# &#9989; **<font color=red>QUESTION:</font>** The errors seen in this example seem like they would be fairly common in Python.  See if you can find a function in ```Numpy``` that has the same purpose as  ```checktrue```:

# **_Put your answer to the above question here._**

# The class ```answercheck``` program will take into consideration round off error.  For example, the ```checkanswer.float``` command would consider both of the above correct:

# +
from answercheck import checkanswer

checkanswer.float(0.300,'e85b79abfd76b7c13b1334d8d8c194a5');
# -

checkanswer.float(0.1+0.2,'e85b79abfd76b7c13b1334d8d8c194a5')

# ----
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
