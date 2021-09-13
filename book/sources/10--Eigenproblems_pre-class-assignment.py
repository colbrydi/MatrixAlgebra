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

# # 10 Pre-Class Assignment: Eigenvectors and Eigenvalues

# ### Readings for this topic (Recommended in bold)
#  * [Heffron Chapter  5 II.3 pg 397-407](http://joshua.smcvt.edu/linearalgebra/book.pdf)
#  * [Beezer Chapter E pg 367-369](http://linear.ups.edu/download/fcla-3.50-tablet.pdf)
#

# ### Goals for today's pre-class assignment 
#
# 1. [Eigenvectors and Eigenvalues](#Eigenvectors_and_Eigenvalues)
# 2. [Solving Eigenproblems - A 2x2 Example](#Solving_Eigenproblems)
# 3. [Introduction to Markov Models](#Markov_Models)
#

# ----
#
# <a name="Eigenvectors_and_Eigenvalues"></a>
#
# ## 1. Eigenvectors and Eigenvalues
#
# Understanding Eigenvector and Eigenvalues can be very challenging. These are complex topics with many facets.  Different textbooks approach the problem from different directions.  All have value.  These facets include:
#
# - Understanding the mathematical definition of Eigenvalues.
# - Being able to calculate an Eigenvalue and Eigenvector.
# - Understanding what Eigenvalues and Eigenvectors represent. 
# - Understanding how to use Eigenvalues and Eigenvectors to solve problems. 
#
# In this course we consider it more important to understand what eigenvectors and eigenvalues represent and how to use them. However, often this understanding comes from first learning how to calculate them.  

# > Eigenvalues are a special set of scalars associated with a **square matrix** that are sometimes also known as characteristic roots, characteristic values (Hoffman and Kunze 1971), proper values, or latent roots (Marcus and Minc 1988, p. 144).
#
# > The determination of the eigenvalues and eigenvectors of a matrix is extremely important in physics and engineering, where it is equivalent to matrix diagonalization and arises in such common applications as [stability analysis](https://en.wikipedia.org/wiki/Von_Neumann_stability_analysis), the [physics of rotating bodies](http://www.physics.princeton.edu/~mcdonald/examples/ph101_1996/ph101lab5_96.pdf), and [small oscillations of vibrating systems](http://lpsa.swarthmore.edu/MtrxVibe/MatrixAll.html), to name only a few.
#
# > The decomposition of a square matrix $A$ into eigenvalues and eigenvectors is known in this work as eigen decomposition, and the fact that this decomposition is always possible as long as the matrix consisting of the eigenvectors of $A$ is square. This is known as the eigen decomposition theorem.
#
#
# From: http://mathworld.wolfram.com/Eigenvalue.html

# The following video provides an intuition for eigenvalues and eigenvectors.  

from IPython.display import YouTubeVideo
YouTubeVideo("ue3yoeZvt8E",width=640,height=360, cc_load_policy=True)

# ### Definition
#
# Let $A$ be an $n\times n$ matrix.  Find a vector $x$ in $R^n$ such that:
#
# $$Ax=\lambda x$$
#
# The above can be rewritten as the following homogeneous equation:
#
# $$(A-\lambda I_n)x = 0$$
#
# The trivial solution is $x=0$. 
#
# However, if we define eigenvectors to be nonzero vectors then $|A-\lambda I_n| = 0$. 
# Nonzero (i.e. non-trivial) solutions to this system of equations can only exist if the matrix of coefficients is singular, i.e. the determinant of $|A - \lambda I_n| = 0$. 
# Therefore, solving the equation $|A - \lambda I_n| = 0$ for $\lambda$ leads to all the eigenvalues of $A$.
#
# **Note:** the above logic is key.  Make sure you understand. If not, ask questions. 

# &#9989; **<font color=red>QUESTION:</font>** Explain why nonzero solutions to a system of homogeneous systems require the matrix to be singular.

# Put your answer here

from IPython.display import YouTubeVideo
YouTubeVideo("PFDu9oVAE-g",width=640,height=360, cc_load_policy=True)

# ### Examples:
# Here are a few more examples of how eigenvalues and eigenvectors are used (You are not required to understand all):
#
# > [Using singular value decomposition for image compression](https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxuYXNsdW5kZXJpY3xneDpkMTI4OTI1NTc4YjRlOGE). 
# This is a note explaining how you can compress an image by throwing away the small eigenvalues of $A^TA$. 
# It takes an 88 megapixel image of an Allosaurus and shows how the image looks after compressing by selecting the largest singular values.
#
# > [Deriving Special Relativity]((https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxuYXNsdW5kZXJpY3xneDo2ZTAyNzA4NTZmOGZmNmU4) is more natural in the language of linear algebra. 
# In fact, Einstein's second postulate really states that "Light is an eigenvector of the Lorentz transform." 
# This document goes over the full derivation in detail.
#
# > [Spectral Clustering](https://en.wikipedia.org/wiki/Spectral_clustering). 
# Whether it's in plants and biology, medical imaging, buisness and marketing, understanding the connections between fields on Facebook, or even criminology, clustering is an extremely important part of modern data analysis. 
# It allows people to find important subsystems or patterns inside noisy data sets. 
# One such method is spectral clustering, which uses the eigenvalues of the graph of a network. 
# Even the eigenvector of the second smallest eigenvalue of the Laplacian matrix allows us to find the two largest clusters in a network.
#
# > [Dimensionality Reduction/PCA](https://en.wikipedia.org/wiki/Principal_component_analysis). 
# The principal components correspond to the largest eigenvalues of $A^\top A$, and this yields the least squared projection onto a smaller dimensional hyperplane, and the eigenvectors become the axes of the hyperplane. 
# Dimensionality reduction is extremely useful in machine learning and data analysis as it allows one to understand where most of the variation in the data comes from.
#
# > [Low rank factorization for collaborative prediction](http://cs229.stanford.edu/proj2006/KleemanDenuitHenderson-MatrixFactorizationForCollaborativePrediction.pdf). 
# This is what Netflix does (or once did) to predict what rating you'll have for a movie you have not yet watched. 
# It uses the singular value decomposition and throws away the smallest eigenvalues of $A^\top A$.
#
# > [The Google Page Rank algorithm](https://en.wikipedia.org/wiki/PageRank). 
# The largest eigenvector of the graph of the internet is how the pages are ranked.
#
# From: https://math.stackexchange.com/questions/1520832/real-life-examples-for-eigenvalues-eigenvectors

# ----
# <a name="Solving_Eigenproblems"></a>
# ## 2. Solving Eigenproblems - A 2x2 Example
#

from IPython.display import YouTubeVideo
YouTubeVideo("0UbkMlTu1vo",width=640,height=360, cc_load_policy=True)

# Consider calculating eigenvalues for any $2\times 2$ matrix. 
# We want to solve:
#
# $$|A - \lambda I_2 | = 0$$
#
# $$ 
# \left|
# \left[
# \begin{matrix}
#     a_{11} & a_{12} \\
#     a_{21} & a_{22}
# \end{matrix}
# \right] 
# - \lambda \left[
# \begin{matrix}
#     1 & 0 \\
#     0 & 1
# \end{matrix}
# \right] 
# \right|
# =
# \left|
# \left[
# \begin{matrix}
#     a_{11}-\lambda & a_{12} \\
#     a_{21} & a_{22}-\lambda
# \end{matrix}
# \right]
# \right|
# =0
# $$
#
# We know this determinant:
#
# $$(a_{11}-\lambda)(a_{22}-\lambda) - a_{12} a_{21}  = 0 $$
#
# If we expand the above, we get:
#
# $$a_{11}a_{22}+\lambda^2-a_{11}\lambda-a_{22}\lambda - a_{12} a_{21} = 0$$
#
# and
#
# $$\lambda^2-(a_{11}+a_{22})\lambda+a_{11}a_{22} - a_{12} a_{21} = 0$$
#
#
# This is a simple quadratic equation. 
# The roots pf $A\lambda^2+B\lambda+C = 0$ can be solved using the quadratic formula:
#
# $$ \frac{-B \pm \sqrt{B^2 - 4AC}}{2A}$$

# &#9989; **<font color=red>QUESTION:</font>** Using the above equation.  What are the eigenvalues for the following $2\times 2$ matrix. Try calculating this by hand and then store the lower value in a variable named```e1``` and the larger value in ```e2``` to check your answer:
#
# $$A =
# \left[
# \begin{matrix}
#     -4 & -6  \\
#     3 & 5
#  \end{matrix}
# \right] 
# $$

# +
# Put your answer here

# +
from answercheck import checkanswer

checkanswer.float(e1,'c54490d3480079138c8c027a87a366e3');

# +
from answercheck import checkanswer

checkanswer.float(e2,'d1bd83a33f1a841ab7fda32449746cc4');
# -

# &#9989; **<font color=red>DO THIS</font>** Find a ```numpy``` function that will calculate eigenvalues and verify the answers from above.

# +
# Put your answer here
# -

# &#9989; **<font color=red>QUESTION:</font>** What are the corresponding eigenvectors to the matrix $A$? This time you can try calculating by hand or just used the function you found in the previous answer.  Store the eigenvector associated with the ```e1``` value in a vector named ```v1``` and the eigenvector associated with the eigenvalue ```e2``` in a vector named ```v2``` to check your answer.  

# Put your answer to the above question here.

# +
from answercheck import checkanswer

checkanswer.eq_vector(v1,'35758bc2fa8ff4f04cfbcd019844f93d');

# +
from answercheck import checkanswer

checkanswer.eq_vector(v2,'90b0437e86d2cf70050d1d6081d942f4');
# -

# &#9989; **<font color=red>QUESTION:</font>**  Both **sympy** and **numpy** can calculate many of the same things. What is the fundamental difference between these two libraries?

# Put your answer to the above question here.

# ----
# <a name="Markov_Models"></a>
# ## 3.  Introduction to Markov Models
#
#
# >In probability theory, a Markov model is a stochastic model used to model randomly changing systems. 
# It is assumed that future states depend only on the current state, not on the events that occurred before it.
# >
# > <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Markovkate_01.svg/1126px-Markovkate_01.svg.png" alt="State space diagram. See text for description" width=25%>
# > A diagram representing a two-state Markov process, with the states labelled E and A. 
# Each number represents the probability of the Markov process changing from one state to another state, with the direction indicated by the arrow. 
# For example, if the Markov process is in state A, then the probability it changes to state E is 0.4, while the probability it remains in state A is 0.6.
#
# From: [Wikipedia](https://en.wikipedia.org/wiki/Markov_model)

# The above state model can be represented by a transition matrix. 
#
# At each time step ($t$) the probability to move between states depends on the previous state ($t-1$):
#
# $$A_{t} = 0.6A_{(t-1)}+0.7E_{(t-1)}$$
#
# $$E_{t} = 0.4A_{(t-1)}+0.3E_{(t-1)}$$
#
# The above state model ($S_t = [A_t, E_t]^T$) can be represented in the following matrix notation:
#
#
# $$S_t = PS_{(t-1)}$$
#

# &#9989;**<font color=red>DO THIS :</font>** Create a $2 \times 2$ matrix (```P```) representing the transition matrix for the above Markov space.

# +
#Put your answer to the above question here

# +
from answercheck import checkanswer

checkanswer.matrix(P,'de1c99f4b4a8d7ea541a084d836ba7e4');
# -

# ----
#
# <a name="T3"></a>
# ## 3. Assignment wrap-up

# &#9989; **<font color=red>Assignment-Specific QUESTION:</font>** Both **sympy** and **numpy** can calculate many of the same things. What is the fundamental difference between these two libraries?

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
