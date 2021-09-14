# -*- coding: utf-8 -*-
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

# # 02 In-Class Assignment: Vectors
#
# What can you solve with $Ax=b$?
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Linear_subspaces_with_shading.svg/650px-Linear_subspaces_with_shading.svg.png" alt="Visual image of three planes intersecting. This is a common image used in linear algebra and will be explained in detail laater in the semester.  It is included here mostly as a visual anchor that can help students when they review their notes. ">
#
# Image from [http://wikipedia.org/](http://wikipedia.org/)
#
# Vector mathematics are used in physics all of the time.  Consider the picture at the beginning of this notebook.  While the space shuttle is attached to the Airplane they have the same velocity vector.  This vector likely has three components; the velocity in the x direction, y direction and z direction.  In fact this velocity is just a combination of multiple components such as thrust from the engines, wind speed and drag. 
#
#
# In this notebook we will be discussing basic vector mathematics and practicing our Python.  We will be using the commands in this notebook all semester so make sure you have have some mastery before moving on.  
#

# ### Agenda for today's class (80 minutes)
#
# 1. [(20 minutes) Example linear System](#Example)
# 1. [(20 minutes) Review pre-class assignment](#Pre-class_assignment_review)
# 1. [(20 minutes) Vectors in Python](#Vectors_in_Python)

# ---
# <a name="Example"></a>
# ## 1. Example linear System:
#
# Suppose that we have three objects on a balanced beam. Also suppose we know that one has a mass of 2 kg, and we want to find the two unknown masses. Experimentation with a (assume weightless) meter stick produces these two balances. (diagram not to scale)
#  
# <img src="https://lh6.googleusercontent.com/S-glvU6hZySH682ocl1T_2jNWL7S2MUCQeyDFgEZM8GPZ4xLjEkeD9KKsU5otJF0zfgcQtT-zQ=w740" align="center" width="70%" alt="Image showing two balanced beams, each with three weights. In the top beam is unknown weight A is a distance of 40 to the left of the fulcrum, unknown weight B is a distance of 15 to the left of the fulcrum and a weight of 2 is 50 to the right of the fulcrum. In the bottom beam is the same unknown weights.  Weight A is now a distance of 50 to the right of the fulcrum, weight B is a distance of 25 to the left of the fulcrum and the weight of 2 is a distance of 25 to the right of the fulcrum.">
#
# For the masses to balance we must have the sum of the moments on the left equal to the sum of the moments on the right, where the moment of an object is its mass times its distance from the balance point.   That gives a system of two  equations:
#
# $$ 40A + 15B = 50 \times 2$$
# $$25B = 25 \times 2 + 50A$$
#

# &#9989; **<span style="color:red">Do This:</span>** Find a solution for the above systems of equations and place your solution in the following cell. Make sure you delete the instructional text in the cell first. 

# +
# Put your answer to the above question here
# -

# &#9989; **<span style="color:red">Do This:</span>** Using Python as a calculator, verify that the solution you have found is correct.  
#
#

# +
# Put your answer to the above question here
# -

# &#9989; **<span style="color:red">Do This:</span>** Now lets consider a system where we have three unknown masses instead of two. Experimentation with a meter stick produces the two balanced states shown below (diagram not to scale). Write the equations for this system.
#
# <img src="https://lh5.googleusercontent.com/lw_dWSYcWURCr552UwgFmCKqPWByDDUDicBuq0UT7vllHzJm7uG_S9f6K8p70ix9J6SRD2UdWQ=w740" width="70%" alt="Image showing two balanced beams, each with four weights. In the top beam is unknown weight A which is a distance of 35 to the left of the fulcrum, unknown weight B is a distance of 21 to the left of the fulcrum, unknown weight C is a distance of 11 to the right of the fulcrum and a weight of 2 is 50 to the right of the fulcrum. In the bottom beam is the same unknown weights.  Weight A is now a distance of 10 to the right of the fulcrum, weight B is a distance of 24 to the right of the fulcrum, weight C is a distance of 25 to the left of the fulcrum and the weight of 2 is still at a distance of 50 to the right of the fulcrum.">
#

# Put your answer to the above question here

# &#9989; **<span style="color:red">Do This:</span>** Find a solution to the second set of equations and report the mass for objects A, B and C.

# +
# Put your answer to the above question here
# -

# &#9989; **<span style="color:red">Do This:</span>** Using Python as a calculator, verify that the solution you have found is correct.

# +
# Put your answer to the above question here
# -

# ---
# <a name="Pre-class_assignment_review"></a>
# ## 3. Pre-class assignment review
#
#
# - [02--Vectors_pre-class-assignment.ipynb](02--Vectors_pre-class-assignment.ipynb)

# ### Vector Addition Properties
# For any vectors ```x```, ```y```, and ```z``` of the same size/dimension, we have the following properties:
# 1. Vector addition is commutative: ```x + y = y + x```.
# 1. Vector addition is associative: ```(x + y) + z = x + (y + z)```. We can therefore write both as ```x + y + z```.
# 1. Adding the zero vector to a vector has no effect: ```x + 0 = 0 + x = x```.  (This is an example where the size of the zero vector follows from the context, i.e., its size must be the same as the size of ```x```)
# 1. ```x − x = 0```. Subtracting a vector from itself yields the zero vector. (Here too the size of 0 is the size of a.)
#

# ### Scalar-Vector Multiply Properties
# For any vectors ```x```, ```y```, and scalars ```a```, ```b```, we have the following properties
#
# * Scalar-vector multiply is commutative: ``` ax  = x * a```; This means that scalar-vector multiplication can be written in either order.
# * Scalar-vector multiply is associative: ```(ab)x = a(bx)``` 
# * Scalar-vector multiply is distributive: ```a(x + y) = ax + ay```, ```(x+y)a = xa + ya```, and ```(a+b)x = ax + bx```.

# ---
# <a name="Vectors_in_Python"></a>
#
# ## 4. Vectors in Python

# For those who are new to Python, there are many common mistakes happen in this course. Try to fix the following codes.
#
#
# ### SyntaxError   
# It means that the code does not make sense in Python. We would like to define a vector with four numbers.

# &#9989; **<font color=red>DO THIS:</font>** Fix the following code to create three vectors with four numbers.

x = [1 2 3.4 4]
y = [1, 2, 3, 5]]
z = [[1, 2, 3, 6.3]

# Although you may have been able to get rid of the error messages the answer to you problem may still not be correct.  Throughout the semester we will be using a python program called ```answercheck``` to allow you to check some of your answers.  This program doesn't tell you the right answer but it is intended to be used as a way to get immediate feedback and accelerate learning.
#
# &#9989; **<font color=red>DO THIS:</font>** First we will need to download ```answercheck.py``` to your current working directory.  You only really need to do this once.  However, if you delete this file by mistake sometime during the semester, you can come back to this notebook and download it again by running the following cell:

# +
from urllib.request import urlretrieve

urlretrieve('https://raw.githubusercontent.com/colbrydi/jupytercheck/master/answercheck.py', 
            'answercheck.py');
# -

# &#9989; **<font color=red>DO THIS:</font>** How just run the following command to see if you got ```x```, ```y``` and ```z``` correct when you fixed the code above. 

# +
from answercheck import checkanswer

checkanswer([x,y,z],'e80321644979a873b273aebbbcd0e450');
# -

# **_NOTE_** make sure you do not change the ```checkanswer``` commands.  The long string with numbers and letters is the secret code that encodes the true answer.  This code is also called the HASH.  Feel free to look at the ```answercheck.py``` code and see if you can figure out how it works?  

#
# ### Numpy   
# Numpy is a common way to represent vectors, and you are suggested to use ```numpy``` unless otherwise specified. The benefit of ```numpy``` is that it can perform the linear algebra operations listed in the previous section.  
#
# For example, the following code uses ```numpy.array``` to define a vector of four elements.

import numpy as np
x_np = np.array([-1, 0, 2, 3.1])
x_np

# #### Scalars versus 1-vectors
# In mathematics, 1-vector is considered as a scalar. But in Python, they are not the same. 

x = 2.4
y = [2.4]
x == y

x == y[0]

# #### Lists of vectors 
# We have a list of numpy arrays or a list of list. In this case, the vectors can have different dimensions. 

# &#9989; **<font color=red>DO THIS:</font>** Modify the print statement using indexing to only print the value 3 from the ```list_of_vectors``` defined below. 

# +
x_np = np.array([-1,0, 2 , 3.1])
y_np = np.array([1,-1,3])
z_np = np.array([0,1])
list_of_vectors = [x_np,y_np,z_np]

print(list_of_vectors)
# -

#
# #### Indexing   
# The index of a vector runs from 0 to $n-1$ for a $n$-vector.

# &#9989; **<font color=red>DO THIS:</font>**  The following code tries to get the third element of ```x_np```, which is the number ```2.0```. Fix this code to provide the correct answer.

print(x_np(3))

# &#9989; **<font color=red>DO THIS:</font>**  Replace only the third element of ```x_np``` with the number ```20.0``` such that the new values of ```x_np``` is [-1, 0, 20., 3.1]

# +
# Replace the third element using 20.0, then the resulting element is 
#####Start your code here #####

#####End of your code here#####
print(x_np)

# +
from answercheck import checkanswer

checkanswer(x_np,'993d5cbc6ddeb10776ed48159780a5d3');
# -

# There is a special index -1, which represents the last element in an array. 
# There are several ways to get more than one consecutive elements. 
# + x_np[1:3] gives the 2nd and 3rd elements only. It starts with the first index and ends before the second index. So the number of element is just the difference between these two numbers.  
# + x_np[1:-1] is the same as x_np[1:3] for a 4-vector.
# + If you want the last element also, then you do not need to put the index, e.g., x_n[1:] gives all elements except the first one. You can do the same thing as the first one. 
#

# &#9989; **<font color=red>DO THIS:</font>** you are given a vector (```x_np```) of $n$ elements, define a new vector (```d```) of size $n-1$ such that $d_i = x_{i+1}-x_i$ for $i=1,\dots,n-1$.  **_Hint_** try doing this without writing your own loop.  You should be able to use simple ```numpy``` indexing as described above. 

# +
x_np = np.array([1,8,3,2,1,9,7])

## Put your answer to the above question here.

# +
from answercheck import checkanswer

checkanswer(d,'14205415f0ed56e608d0a87e7253fa70');
# -

# ### Assignment versus copying
# Take a look at the following code. 
# + we create one numpy array ```x_np```
# + we let ```y_np = x_np```
# + we change the third element of ```y_np```
# + The third element of ```x_np``` is also changed
#
# This looks weired and may not make sense for those uses other languages such as MATLAB.
#
#
# The reason for this is that we are not creating a copy of ```x_np``` and name it as ```y_np```. What we did is that we give a new name ```y_np``` to the same array ```x_np```. Therefore, if one is changed, and the other one is also changed, because they refer to the same array. 

x_np = np.array([-1, 0, 2, 3.1])
y_np = x_np
y_np[2] = 20.0
x_np

# &#9989; **<font color=red>DO THIS:</font>** There is a method named ```copy``` that can be used to create a new array. You can search how it works and fix the code below. If this is done correctly the ```x_np``` vector should stay the same and the ```y_np``` you now be ```[-1 0 2 3.1]```.

## modify the following code to copy the x_np instead of just giving it a new name
x_np = np.array([-1, 0, 2, 3.1])
y_np = x_np
y_np[2] = 20.0
print(x_np)

# +
from answercheck import checkanswer

checkanswer(x_np,'0ba269d18692155ba252e6addedf37ad');

# +
from answercheck import checkanswer

checkanswer(y_np,'993d5cbc6ddeb10776ed48159780a5d3');
# -

# ### Vector equality in numpy and list
#
# The relational operator (```==```, ```<```, ```>```, ```!=```, etc.) can be used to check whether the vectors are same or not. However, they will act differently if the code is comparing ```numpy.array``` objects or a ```list```. In ```numpy```, In ```numpy``` relational operators checks the equality for each element in the ```array```. For ```list```, relational operators check all elements. 

# +
x = [-1, 0, 2, 3.1]
y = x.copy()
y[2] = 20.2

x_np = np.array(x)
y_np = np.array(y)
# -

x == y

np.array(x_np) == np.array(y_np)

# ### Zero vectors and Ones vectors in numpy
#
# + zeros(n) creates a vector with all 0s
# + ones(n) creates a vector with all 1s

# &#9989; **<font color=red>DO THIS:</font>** Create a zero vector (called ```zero_np```) with the same dimension as vector ```x_np```. Create a ones vector (called ```ones+np```) also with the same dimension as vector ```x_np```. 

x_np = np.array([-1, 0, 2, 3.1])
### Define zero_np and ones_np here 

# +
from answercheck import checkanswer

checkanswer([zero_np, ones_np],'7f874c2e446786655ff96f0bbae8a0c6');
# -

# ### Random vectors 
#
# + random.random(n) creates a random vector with dimension $n$. 

random_np = np.random.random(2)
print(random_np)

# ### Vector addition and subtraction
# In this section, you will understand why we use numpy for linear algebra opeartions. If x and y are numpy arrays of the same size, we can have x + y and x-y for their addition and subtraction, respectively.

# +
x_np = np.array([1,2,3])
y_np = np.array([100,200,300])

v_sum = x_np + y_np
v_diff = x_np - y_np

print (f'Sum of vectors: {v_sum}')
print (f'Difference of vectors: {v_diff}')
# -

# For comparison, we also put the addition of two lists below. Recall from the pre-class assignment, we have to define a function to add two lists for linear algebra. 
#
#
# &#9989; **<font color=red>DO THIS:</font>**  Modify the following code to properly add and subtract the two lists.  **_HINT_** it is perfectly okay NOT to write your own function try you should be able to cast the lists as arrays:

# +
x = [1,2,3]
y = [100,200,300]

v_sum = x + y
v_diff = x - y

print (f'Sum of vectors: {v_sum}')
print (f'Difference of vectors: {v_diff}')
# -

# ### Scalar-vector addition
# A scalar-vector addition means that the scalar (or a 1-vector) is added to all elements of the vector. 

# &#9989; **<font color=red>DO THIS:</font>** Add a scalar 20.20 to all elements of the following vector ```x_np ``` and store teh result back into ```x_np```

x_np = np.array([1.0,2.0,3.0])

# +
from answercheck import checkanswer

checkanswer(x_np,'2f8cbcce405fa12b8608422ff28544bb');
# -

# ### Scalar-vector multiplication and division
# When ```a``` is a scalar and ```x``` is ```numpy``` array. We can express the scalar-vector multiplication as ```a*x``` or ```x*a```. 
#
#
# We can also do scalar-vector division for ```x/a``` or ```a/x```. (note that ```x/a``` and ```a/x``` are different)

# &#9989; **<font color=red>DO THIS:</font>** Divide all elements of the following vector ```x_np``` by ```20.20``` and put it into ```y_np```

x_np = np.array([1,2,3])
#####Start your code here #####
y_np = 
#####End of your code here#####
print(y_np)

# +
from answercheck import checkanswer

checkanswer(y_np,'90c1b8639f9d350af1d971d89209a0c6');
# -

# ### Element-wise operations.
# As stated above relational operations on ```numpy``` arrays are performed element-wise. Examples we mentioned before are 
# + The ```==``` operator 
# + The addition ```+``` and subtraction ```-```
#
# **_Note_** for this to work the two vectors have to be the same dimensions. 
#
#
# If they are not have the same dimension, such as a scalar and a vector, we can think about expanding the scalar to have the same dimension as the vector and perform the operations. For example.
# + Vector-scalar addition and subtraction
# + Vector-scalar multiplication and division

# &#9989; **<font color=red>DO THIS:</font>** Assume that you invested three assets with initial values stored in ```p_initial```, and after one week, their values are stored in ```p_final```. Then what are the asset return ratio (```r```) for these three assets (i.e. price change over the initial value). 

p_initial = np.array([22.15, 89.32, 56.77])
p_final = np.array([23.05, 87.32, 53.13])

# +
from answercheck import checkanswer

checkanswer(r,'0e231e6cfbef65cf178208cf377af85c');
# -

# ### Linear combination 
#
# We have two vectors $x$ and $y$ we can get the linear combination of these two vectors as $ax + by$ where $a$ and $b$ are scalar coefficients.
#
# In the following example, we are given two vectors (```x_np``` and ```y_np```), and two scalars (```alpha``` and ```beta```), we obtain the linear combination ```alpha*x_np + beta*y_np```.

x_np = np.array([1,2])
y_np = np.array([3,4])
alpha = 0.5
beta = -0.8
c = alpha*x_np + beta*y_np
print(c)


# We can also define a function ```lincomb``` to performn the linear combination. 

# &#9989; **<font color=red>DO THIS:</font>** Finish the following code for lincomb and compare the results we just get.

def lincomb(coef, vectors): 
    n = len(vectors[0])  # get the dimension of the vectors. note they have to be of the same dimension
    comb = np.zeros(n)   # initial the value with all zeros.
    ### Add code here to calculate the linear combination of the input vecotrs and the coefficients. 
    return comb



# +
from answercheck import checkanswer

combination = lincomb([alpha, beta], [x_np,y_np])

checkanswer(combination,'8bab7329c94f3e3cda423add411685c2');
# -

# We can also test the functions ourselves by using values for which we know the answer. For example, the following tests are multiplying and adding by zero we know what these answers should be and can check them.

# +
combination = lincomb([0, 0], [x_np,y_np])

combination == np.zeros(combination.shape)

# +
combination = lincomb([2, 2], [combination,np.zeros(combination.shape)])

combination == 2*combination
# -

# If you want to check that all values in a ```numpy.array``` are the same you could convert it to a list or there is a method called ```alltrue``` which checks if everything is true. It is a good idea to use this method if vectors get big. 

# +
combination = lincomb([2, 2], [combination,np.zeros(combination.shape)])

np.alltrue(combination == 2*combination)
# -

# ----
# Written by Dr. Dirk Colbry, Michigan State University and Dr. Ming Yan, Michigan State University<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
