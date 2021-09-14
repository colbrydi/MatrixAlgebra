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

# # 07 In-Class Assignment: Transformations
#
# <img src="https://people.gnome.org/~mathieu/libart/art-affines.png">
#
# Image from: https://people.gnome.org/~mathieu/libart/libart-affine-transformation-matrices.html
#     

# ### Agenda for today's class (80 minutes)
#
# 1. [(20 minutes) Review of Pre-Class Assignment](#Review_of_Pre-Class_Assignment)
# 1. [(20 minutes) Affine Transforms](#Affine_Transforms)
# 1. [(20 minutes) Fractals](#Fractals)

# ----
# <a name="Review_of_Pre-Class_Assignment"></a>
# ## 1. Review of Pre-Class Assignment
#
# * [07--Transformations_pre-class-assignment](07--Transformations_pre-class-assignment.ipynb)

# ----
# <a name="Affine_Transforms"></a>
# ## 2. Affine Transforms
#
# In this section, we are going to explore different types of transformation matrices. 
# The following code is designed to demonstrate the properties of some different transformation matrices.  
#
# &#9989; **<font color=red>DO THIS:</font>** Review the following code.  

#Some python packages we will be using
# %matplotlib inline
import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D # Lets make 3D plots
import numpy as np
import sympy as sym
sym.init_printing(use_unicode=True) # Trick to make matrixes look nice in jupyter

# +
# Define some points
x = [0.0,  0.0,  2.0,  8.0, 10.0, 10.0, 8.0, 4.0, 3.0, 3.0, 4.0, 6.0, 7.0, 7.0, 10.0, 
     10.0,  8.0,  2.0, 0.0, 0.0, 2.0, 6.0, 7.0,  7.0,  6.0,  4.0,  3.0, 3.0, 0.0]
y = [0.0, -2.0, -4.0, -4.0, -2.0,  2.0, 4.0, 4.0, 5.0, 7.0, 8.0, 8.0, 7.0, 6.0,  6.0,
     8.0, 10.0, 10.0, 8.0, 4.0, 2.0, 2.0, 1.0, -1.0, -2.0, -2.0, -1.0, 0.0, 0.0]
con = [ 1.0 for i in range(len(x))] 

p = np.matrix([x,y,con])


mp = p.copy()

#Plot Points
plt.plot(mp[0,:].tolist()[0],mp[1,:].tolist()[0], color='green');
plt.axis('scaled');
plt.axis([-10,20,-15,15]);
plt.title('Start Location');
# -

# ### Example Scaling Matrix

# +
#Example Scaling Matrix

#Define Matrix
scale = 0.5  #The amount that coordinates are scaled.
S = np.matrix([[scale,0,0], [0,scale,0], [0,0,1]])

#Apply matrix

mp = p.copy()
mp = S*mp

#Plot points after transform
plt.plot(mp[0,:].tolist()[0],mp[1,:].tolist()[0], color='green')
plt.axis('scaled')
plt.axis([-10,20,-15,15])
plt.title('After Scaling')

#Uncomment the next line if you want to see the original.
# plt.plot(p[0,:].tolist()[0],p[1,:].tolist()[0], color='blue',alpha=0.3);

sym.Matrix(S)
# -

# ### Example Translation Matrix

# +
#Example Translation Matrix

#Define Matrix
dx = 1  #The amount shifted in the x-direction
dy = 1  #The amount shifted in the y-direction
T = np.matrix([[1,0,dx], [0,1,dy], [0,0,1]])

#Apply matrix

mp = p.copy()

mp = T*mp

#Plot points after transform
plt.plot(mp[0,:].tolist()[0],mp[1,:].tolist()[0], color='green')
plt.axis('scaled')
plt.axis([-10,20,-15,15])
plt.title('After Translation')

#Uncomment the next line if you want to see the original.
# plt.plot(p[0,:].tolist()[0],p[1,:].tolist()[0], color='blue',alpha=0.3);

sym.Matrix(T)
# -

# ### Example Reflection Matrix

# +
#Example Reflection Matrix

#Define Matrix
Re = np.matrix([[1,0,0],[0,-1,0],[0,0,1]]) ## Makes all y-values opposite so it reflects over the x-axis.

#Apply matrix

mp = p.copy()

mp = Re*mp

#Plot points after transform
plt.plot(mp[0,:].tolist()[0],mp[1,:].tolist()[0], color='green')
plt.axis('scaled')
plt.axis([-10,20,-15,15])

#Uncomment the next line if you want to see the original.
# plt.plot(p[0,:].tolist()[0],p[1,:].tolist()[0], color='blue',alpha=0.3);

sym.Matrix(Re)
# -

# ### Example Rotation Matrix

# +
#Example Rotation Matrix

#Define Matrix
degrees = 30
theta = degrees * np.pi / 180  ##Make sure to always convert from degrees to radians. 

# Rotates the points 30 degrees counterclockwise.
R = np.matrix([[np.cos(theta),-np.sin(theta),0],[np.sin(theta), np.cos(theta),0],[0,0,1]]) 

#Apply matrix
mp = p.copy()

mp = R*mp

#Plot points after transform
plt.plot(mp[0,:].tolist()[0],mp[1,:].tolist()[0], color='green')
plt.axis('scaled')
plt.axis([-10,20,-15,15])

#Uncomment the next line if you want to see the original.
# plt.plot(p[0,:].tolist()[0],p[1,:].tolist()[0], color='blue',alpha=0.3);

sym.Matrix(R)
# -

# ### Example Shear Matrix

# ### Combine Transforms
#
# We have five transforms $R$, $S$, $T$, $Re$, and $SH$ 
#
# &#9989; **<font color=red>DO THIS:</font>** Construct a ($3 \times 3$) transformation Matrix (called $M$) which combines these five transforms into a single matrix. You can choose different orders for these five matrix, then compare your result with other students. 

# +
#Put your code here
# -

#Plot combined transformed points
mp = p.copy()
mp = M*mp
plt.plot(mp[0,:].tolist()[0],mp[1,:].tolist()[0], color='green');
plt.axis('scaled');
plt.axis([-10,20,-15,15]);
plt.title('Start Location');

# &#9989; **<font color=red>Questions:</font>** Did you can get the same result with others? You can compare the matrix $M$ to see the difference. If not, can you explain why it happens?

# Put your answer here

# ### Interactive Example

# +
from ipywidgets import interact,interact_manual

def affine_image(angle=0,scale=1.0,dx=0,dy=0, shx=0, shy=0):
    theta = -angle/180  * np.pi
    
    plt.plot(p[0,:].tolist()[0],p[1,:].tolist()[0], color='green')
    
    S = np.matrix([[scale,0,0], [0,scale,0], [0,0,1]])
    SH = np.matrix([[1,shx,0], [shy,1,0], [0,0,1]])
    T = np.matrix([[1,0,dx], [0,1,dy], [0,0,1]])
    R = np.matrix([[np.cos(theta),-np.sin(theta),0],[np.sin(theta), np.cos(theta),0],[0,0,1]])
    
    #Full Transform
    FT = T*SH*R*S;
    #Apply Transforms
    p2 =  FT*p;
    
    #Plot Output
    plt.plot(p2[0,:].tolist()[0],p2[1,:].tolist()[0], color='black')
    plt.axis('scaled')
    plt.axis([-10,20,-15,15])
    return sym.Matrix(FT)


# -

interact(affine_image, angle=(-180,180), scale_manual=(0.01,2), dx=(-5,15,0.5), dy=(-15,15,0.5), shx = (-1,1,0.1), shy = (-1,1,0.1)); ##TODO: Modify this line of code

# The following command can also be used but it may be slow on some peoples computers.

# +
#interact(affine_image, angle=(-180,180), scale=(0.01,2), dx=(-5,15,0.5), dy=(-15,15,0.5), shx = (-1,1,0.1), shy = (-1,1,0.1)); ##TODO: Modify this line of code
# -

# &#9989; **<font color=red>DO THIS:</font>**  Using the above interactive enviornment to see if you can figure out the transformation matrix to make the following image:
#
# <img src="https://lh6.googleusercontent.com/_0-jr5Z0DQzqVM3TD3Xa3QWC43PBT6ru5M-B-_7dfbib2SSvkNkxtioBFaU__jTvEJMMG9SAVg=w380">

# &#9989; **<font color=red>Questions:</font>** What where the input values?

#
# Put your answer here:
#
# r = 
#
# scale = 
#
# dx = 
#
# dy = 
#
# shx = 
#
# shy = 

# ----
# <a name="Fractals"></a>
# ## 3. Fractals
#

# In this section we are going to explore using transformations to generate fractals.  Consider the following set of linear equations.  Each one takes a 2D point as input, applies a $2 \times 2$ transform, and then also translates by a $2 \times 1$ translation matrix

# $$ 
# T_1:\left[ \begin{matrix}
#     x_1 \\
#     y_1 
#  \end{matrix}
# \right] 
# =
# \left[ \begin{matrix}
#     0.86 & 0.03  \\
#     -0.03 & 0.86 
#  \end{matrix}
# \right] 
# \left[ \begin{matrix}
#     x_0 \\
#     y_0 
#  \end{matrix}
# \right] +
# \left[\begin{matrix}
# 0\\
# 1.5
# \end{matrix}
# \right]
# : probability =  0.83 $$ 

# $$ 
# T_2: \left[ \begin{matrix}
#     x_1 \\
#     y_1 
#  \end{matrix}
# \right] 
# =
# \left[ \begin{matrix}
#     0.2 & -0.25  \\
#     0.21 & 0.23 
#  \end{matrix}
# \right] 
# \left[ \begin{matrix}
#     x_0 \\
#     y_0 
#  \end{matrix}
# \right] +
# \left[\begin{matrix}
# 0\\
# 1.5
# \end{matrix}
# \right]
# : probability =  0.08 $$ 

# $$ 
# T_3 : \left[ \begin{matrix}
#     x_1 \\
#     y_1 
#  \end{matrix}
# \right] 
# =
# \left[ \begin{matrix}
#     0.15 & 0.27  \\
#     0.25 & 0.26 
#  \end{matrix}
# \right] 
# \left[ \begin{matrix}
#     x_0 \\
#     y_0 
#  \end{matrix}
# \right] +
# \left[\begin{matrix}
# 0\\
# 0.45
# \end{matrix}
# \right]
# : probability =  0.08 $$ 

# $$ 
# T_4: \left[ \begin{matrix}
#     x_1 \\
#     y_1 
#  \end{matrix}
# \right] 
# =
# \left[ \begin{matrix}
#     0 & 0  \\
#     0 & 0.17 
#  \end{matrix}
# \right] 
# \left[ \begin{matrix}
#     x_0 \\
#     y_0 
#  \end{matrix}
# \right] +
# \left[\begin{matrix}
# 0\\
# 0
# \end{matrix}
# \right] : probability =  0.01 $$

# We want to write a program that use the above transformations to "randomly" generate an image.  We start with a point at the origin (0,0) and then randomly pick one of the above transformation based on their probability, update the point position and then randomly pick another point.  Each matrix adds a bit of rotation and translation with $T_4$ as a kind of restart.    
#

# To try to make our program a little easier, lets rewrite the above equations to make a system of  "equivelent" equations of the form $Ax=b$ with only one matrix.   We do this by adding an additional variable variable $z=1$.  For example, verify that the following equation is the same as equation for $T1$ above:
#
# $$ 
# T_1: \left[ \begin{matrix}
#     x_1 \\
#     y_1 
#  \end{matrix}
# \right] 
# =
# \left[ \begin{matrix}
#     0.86 & 0.03 & 0 \\
#     -0.03 & 0.86 & 1.5
#  \end{matrix}
# \right] 
# \left[ \begin{matrix}
#     x_0 \\
#     y_0 \\
#     1
#  \end{matrix}
# \right] 
# $$ 
# Please NOTE that we do not change the value for $z$, and it is always be $1$.

# &#9989; **<font color=red>DO THIS:</font>** Verify the $Ax=b$ format will generate the same answer as the $T1$ equation above.

# The following is some pseudocode that we will be using to generate the Fractals:
#
# 1. Let $x = 0$, $y = 0$, $z=1$
# 2. Use a random generator to select one of the affine transformations $T_i$ according to the given probabilities.
# 3. Let $(x',y') = T_i(x,y,z)$.
# 4. Plot $(x', y')$
# 5. Let $(x,y) = (x',y')$
# 6. Repeat Steps 2, 3, 4, and 5 one thousand times. 

# The following python code implements the above pseudocode with only the $T1$ matrix:

# +
# %matplotlib inline

import numpy as np
import matplotlib.pylab as plt
import sympy as sym
sym.init_printing(use_unicode=True) # Trick to make matrixes look nice in jupyter

T1 = np.matrix([[0.86, 0.03, 0],[-0.03, 0.86, 1.5]])
#####Start your code here #####
T2 = T1 
T3 = T1
T4 = T1
#####End of your code here#####       

prob = [0.83,0.08,0.08,0.01]

I = np.matrix([[1,0,0],[0,1,0],[0,0,1]])

fig = plt.figure(figsize=[10,10])
p = np.matrix([[0.],[0],[1]])
plt.plot(p[0],p[1], 'go');
for i in range(1,1000):
    ticket = np.random.random();
    if (ticket < prob[0]):
        T = T1
    elif (ticket < sum(prob[0:2])):
        T = T2
    elif (ticket < sum(prob[0:3])):
        T = T3
    else:
        T = T4
    p[0:2,0] = T*p    
    plt.plot(p[0],p[1], 'go');
plt.axis('scaled');
# -

# &#9989; **<font color=red>DO THIS:</font>** Modify the above code to add in the $T2$, $T3$ and $T4$ transforms.  

# &#9989; **<font color=red>QUESTION:</font>**  Describe in words for the actions performed by $T_1$, $T_2$, $T_3$, and $T_4$. 

# $T_1$: Put your answer here

# $T_2$: Put your answer here

# $T_3$: Put your answer here

#
# $T_4$: Put your answer here

# &#9989; **<font color=red>DO THIS:</font>** Using the same ideas to design and build your own fractal.  You are welcome to get inspiration from the internet. Make sure you document where your inspiration comes from.  Try to build something fun, unique and different.  Show what you come up with with your instructors. 

# +
#Put your code here. 
# -

# ----
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
