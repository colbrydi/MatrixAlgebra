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

# # 18 In-Class Assignment: Inner Products
#
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Pleiades_large.jpg/1200px-Pleiades_large.jpg" alt="Image of the pleiades star cluster" width="50%">
#
#
# Image from: https://www.wikipedia.org/
#     

# ### Agenda for today's class (80 minutes)
#
# 1. [(20 minutes) Pre-class Review](#Pre-class_Review)
# 1. [(30 minutes) Minkowski Geometry](#Minkowski_Geometry)
# 1. [(30 minutes) Function Approximation](#Function_Approximation)

# ---
# <a name="Pre-class_Review"></a>
# ## 1. Pre-class Review
#
# * [18--Inner_Product_pre-class-assignment.ipynb](18--Inner_Product_pre-class-assignment.ipynb)
#
# An inner product on a real vector space $V$ is a function that associates a number, denoted as $\langle u,v \rangle$, with each pair of vectors $u$ and $v$ of $V$. This function satisfies the following conditions for vectors $u, v, w$ and scalar $c$:
#
#
# $$\langle u,v \rangle = \langle v,u \rangle \text{ symmetry axiom}$$ 
#
# $$\langle u+v,w \rangle = \langle u,w \rangle + \langle v,w \rangle \text{ additive axiom}$$ 
#
# $$\langle cu,v \rangle = c\langle v,u \rangle \text{ homogeneity axiom}$$ 
#
# $$\langle u,v \rangle = \langle v,u \rangle \text{ Symmetry axiom}$$ 
#
# $$\langle u,u \rangle \ge 0 \text{ and } \langle u,u \rangle = 0 \text{ if and only if } u = 0 \text{ positive definite axiom}$$ 
#
#
# The dot product of $R^n$ is an inner product. However, we can define many other inner products.
#
# ### Norm of a vector
#
# Let $V$ be an inner product space. The norm of a vector $v$ is denoted $\lVert v \rVert$ and is defined by:
#
# $$\lVert v \rVert = \sqrt{\langle v,v \rangle}$$
#
# ### Angle between two vectors
#
# Let $V$ be a real inner product space. The angle $\theta$ between two nonzero vectors $u$ and $v$ in $V$ is given by:
#
# $$cos(\theta) = \frac{\langle u,v \rangle}{\lVert u \rVert \lVert v \rVert}$$
#
# ### Orthogonal Vectors
#
# Let $V$ be an inner product space.  Two vectors $u$ and $v$ in $V$ are orthogonal if their inner product is zero:
#
# $$\langle u,v \rangle = 0$$
#
# ### Distance
# Let $V$ be an inner product space. The distance between two vectors (points) $u$ and $v$ in $V$ is denoted $d(u,v)$ and is defined by:
#
# $$d(u,v) = \lVert u-v \rVert = \sqrt{\langle u-v, u-v \rangle}$$
#
#

# ---
# <a name="Minkowski_Geometry"></a>
# ## 2. Minkowski Geometry
# Consider the following pseudo inner-product which is used to model special relativity in $R^4$:
#
# $$\langle X,Y \rangle = -x_1y_1 - x_2y_2 -x_3y_3 + x_4y_4$$
#
# It has the following norms and distances:
#
# $$\lVert X \rVert = \sqrt{|\langle X,X \rangle|}$$
#
# $$ d(X,Y) = \lVert X - Y \rVert = \lVert ( x_1 - y_1, x_2-y_2, x_3 - y_3, x_4 - y_4) \rVert$$
#
# $$ = \sqrt{|-(x_1 - y_1)^2 - (x_2-y_2)^2 - (x_3 - y_3)^2 + (x_4 - y_4)^2|}$$

# &#9989;**<font color=red>QUESTION:</font>** The Minkowski Geometry is called pseudo inner product because it violates one of the inner product axioms. Discuss the axioms in your group and decide which one it violates.

# Put your answer to the above quesiton here

# ### The Physical Interpretation of Minkowski Geometry
#
#
# > The distance between two points on the path of an observer in Minkowski geometry corresponds to the time recorded by that observer in traveling between the two points. 
#
# We assume that Alpha Centauri lies in the $x_1$ direction from the Earch.  The twin on Earth advances in time $x_4$. There is no motion in either the $x_2$ or $x_3$ directions. Twin 2 on board the rocket advances in time and moves toward Alpha Centauri and back to the Earth. 
#
# Let $P=(0,0,0,0)$, $R=(4,0,0,5)$, and $Q=(0,0,0,10)$. 
#
# - $d(P, Q) =10$ means that Twin 1 ages 10 years from $P$ to $Q$. Because $x_1$ does not change and only the time $x_4$ changes. Twin 1 does not travel and stay on Earth for 10 years.
# - $d(P, R) =3$ means that Twin 2 ages 3 years in traveling from $P$ to $R$. When Twin 2 arrives at the $R$, the time on the earth has passed $5$ years, though the recored time by Twin 2 is only $3$ years.
# - $d(R, Q) =3$ means taht Twin 2 ages 3 years in traveling from $R$ to $Q$. When Twin 2 travels back to the Earth $P$, it records 3 years but the time at the Earch has passed 5 years.
# - The time from $P->R->Q$ is shorter than $P->Q$. 
#

# &#9989;**<font color=red>QUESTION:</font>** The star cluster Pleiades in the constellation Taurus is 410 light years from Earth. A generational spaceship to the cluster traveling at constant speed ages 850 years on a round trip. By the time the spaceship returns to Earth, how many centuries will have passed on Earth? 

# Put your answer to the above quesiton here

# &#9989;**<font color=red>QUESTION:</font>** How fast was the spaceship going relative to earth?

# Put your answer to the above question here.

# ---
# <a name="Function_Approximation"></a>
# ## 3. Function Approximation
#
# **Definition:** Let $C[a,b]$ be a vector space of all possible continuous functions over the interval $[a,b]$ with inner product:
# $$\langle f,g \rangle = \int_a^b f(x)g(x) dx.$$
#
# Now let $f$ be an element of $C[a,b]$, and $W$ be a subspace of $C[a,b]$. The function $g \in W$ such that $\int_a^b \left[ f(x) - g(x) \right]^2 dx$ is a minimum is called the **least-squares approximation** to $f$.
#
#
#  The least-squares approximation to $f$ in the subspace $W$ can be calculated as the projection of $f$ onto $W$:
#  
#  $$g = proj_Wf$$
#  
#  If $\{g_1, \ldots, g_n\}$ is an orthonormal basis for $W$, we can replace the dot product of $R^n$ by an inner product of the function space and get:
#  
#  $$prog_Wf = \langle f,g_1 \rangle g_1 + \ldots + \langle f,g_n \rangle g_n$$
#  
#  
# ###  Polynomial Approximations
#
# An orthogonal bases for all polynomials of degree less than or equal to $n$ can be computed using Gram-schmidt orthogonalization process.  First we start with the following standard basis vectors in $W$
#
# $$ \{ 1, x, \ldots, x^n \}$$
#
# The Gram-Schmidt process can be used to make these vectors orthogonal. The resulting polynomials on $[-1,1]$ are called  **Legendre polynomials**.  The first six Legendre polynomial basis are:
#
# $$1$$
# $$x$$
# $$x^2 -\frac{1}{3}$$
# $$x^3 - \frac{3}{5}x$$
# $$x^4 - \frac{6}{7}x^2 + \frac{3}{35}$$
# $$x^5 - \frac{10}{9}x^3 + \frac{5}{12}x$$

# &#9989;**<font color=red>QUESTION:**</font> What is the least-squares linear approximations of $f(x) = e^x$ over the interval $[-1, 1]$. In other words, what is the projection of $f$ onto $W$, where $W$ is a first order polynomal with basis vectors $\{1, x\} (i.e. n=1)$. (Hint: You can give the answer in integrals without computing the integrals. Note the Legendre polynomials are not normalized.)

# Put your answer to the above question here.

# Here is a plot of the equation $f(x) = e^x$:

# +
# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np

#px = np.linspace(-1,1,100)
#py = np.exp(px)
#plt.plot(px,py, color='red');
import sympy as sym
from sympy.plotting import plot
x = sym.symbols('x')
f = sym.exp(x)
plot(f,(x,-1,1))
# -

# We can use `sympy` to compute the integral. The following code compute the definite integral of 
# $$\int_{-1}^1 e^x dx.$$
# In fact, `sympy` can also compute the indefinite integral by removing the interval.

sym.init_printing()
x = sym.symbols('x')
sym.integrate('exp(x)',(x, -1, 1))
#sym.integrate('exp(x)',(x))

# Use `sympy` to compute the first order polynomial that approximates the function $e^x$.
# The following calculates the above approximation written in ```sympy```:

g_0 = sym.integrate('exp(x)*1',(x, -1, 1))/sym.integrate('1*1',(x,-1,1))*1
g_1 = g_0 + sym.integrate('exp(x)*x',(x,-1,1))/sym.integrate('x*x',(x,-1,1))*x
g_1 

# Plot the original function $f(x)=e^x$ and its approximation.

p2 = plot(f, g_1,(x,-1,1))

# +
#For fun, I turned this into a function:
x = sym.symbols('x')

def lsf_poly(f, gb = [1,  x], a =-1, b=1):
    proj = 0
    for g in gb:
#        print(sym.integrate(g*f,(x,a,b)))
        proj = proj + sym.integrate(g*f,(x,a,b))/sym.integrate(g*g,(x,a,b))*g
    return proj

lsf_poly(sym.exp(x))
# -

# &#9989;**<font color=red>QUESTION:</font>** What would a second order approximation look like for this function? How about a fifth order approximation?  

# Put your answer to the above question here

#####Start your code here #####
x = sym.symbols('x')
g_2 = 
g_2
#####End of your code here#####


p2 = plot(f, g_2,(x,-1,1))

# ----
#
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
