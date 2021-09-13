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

# # 14 Pre-Class Assignment: Fundamental Spaces
#
#
# <img alt="Classic picture of the four fundamental spaces. Please see text for detailed description." src="https://kevinbinz.files.wordpress.com/2017/02/linear-algebra-fundamental-space-interpretation-6.png" width="100%">
#
#
# Image from: https://kevinbinz.com/2017/02/20/linear-algebra/

# ### Readings for this topic (Recommended in bold)
#  * [**_Heffron Section VI.3 pg 277-283_**](http://joshua.smcvt.edu/linearalgebra/book.pdf)
#

#
# ### Goals for today's pre-class assignment 
#
# 1. [Orthogonal Complement](#Orthogonal_Complement)
# 1. [The Four Fundamental Spaces](#The_Four_Fundamental_Spaces)
# 1. [Independent Learning](#Independent_Learning)
# 1. [Assignment wrap-up](#Assignment_wrap-up)

# ----
# <a name="Orthogonal_Complement"></a>
# ## 1. Orthogonal Complement
#
# **Definition**: A vector $u$ is **orthogonal to a subspace** $W$ of $R^n$ if $u$ is orthogonal to any $w$ in $W$ ($u\cdot w=0$ for all $w\in W$).
#
# For example, consider the following figure, if we consider the plane to be a subspace then the perpendicular vector comming out of the plane is is orthoginal to any vector in the plane:
#
# <img alt="Image of a 2D plane with a vector pointing directly out of the surface." src="https://lh5.googleusercontent.com/KC1bkJgC9ihevnOCqeMn_efEdkvgcx5TeBkEVYniwo7T_KxmBu76irZKluAj5PNor9SWdCg4RMS6BZDpNSJOmmz6l6cY0mEc5pq6iR9Qu8AzvWb12lgOO-YUBqiu=w416">
#
# **Definition**: The **orthogonal complement** of $W$ is the set of all vectors that are orthogonal to $W$. The set is denoted as $W_{\bot}$. 

# &#9989; **<font color=red>QUESTION:</font>** Is $W_\bot$ a subspace of $R^n$? Justify your answer briefly.

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>** What are the vectors in both $W$ and $W_\bot$?

# Put your answer to the above question here

from IPython.display import YouTubeVideo
YouTubeVideo("5B8XluiqdHM",width=640,height=360, cc_load_policy=True)

# ### Projection of a Vector onto a Subspace
#
# Think of a projection onto a subspace is analogous to a shadow on a surface.  Aspects of an objects 3D space is represented in a 2D shadow but you can't take the shadow by itself and exactly recreate the 3D surface. 
#
# <img alt="Picture of a hand shadow puppet of a bird.  Used to represent a projection" src="https://upload.wikimedia.org/wikipedia/commons/f/f5/Hand_shadow_bird.jpg" width=30%>
#
# Image from https://commons.wikimedia.org
#
# The following is the matimatical defination of projection onto a subspace.
#
# **Definition**: Let $W$ be a subspace of $R^n$ of dimension $m$. Let $\{w_1,\cdots,w_m\}$ be an orthonormal basis for $W$. Then the projection of vector $v$ in $R^n$ onto $W$ is denoted as $\mbox{proj}_Wv$ and is defined as 
# $$\mbox{proj}_Wv = (v\cdot w_1)w_1+(v\cdot w_2)w_2+\cdots+(v\cdot w_m)w_m$$
#
#
# Another way to say the above defination is that the project of $v$ onto the $W$ is just the sumation of $v$ projected onto each vector in a basis of $W$
#
#
# **Remarks**: 
# > Recall in the lecture on *Projections*, we discussed the projection onto a vector, which is the case for $m=1$. We used the projection for $m>1$ in the Gram-Schmidt algorithm. 
#
# > The projection does not depend on which orthonormal basis you choose. 
#
# > If $v$ is in $W$, we have $\mbox{proj}_Wv=v$.

# ### The Orthogonal Decomposition Theorem
# **Theorem**: Let $W$ be a subspace of $R^n$. Every vector $v$ in $R^n$ can be written uniquely in the form 
# $$v= w+w_{\bot},$$
# where $w$ is in $W$ and $w_\bot$ is orthogonal to $W$ (i.e., $w_\bot$ is in $W_\bot$). 
# In addition, $w=\mbox{proj}_Wv$, and $w_\bot = v-\mbox{proj}_Wv$.
#
# **Definition**: Let $x$ be a point in $R^n$, $W$ be a subspace of $R^n$. The distance from $x$ to $W$ is defined to be the minimum of the distances from $x$ to any point $y$ in $W$.
# $$d(x,W)=\min \{\|x-y\|: \mbox{ for all }y \mbox{ in } W\}.$$
# The optimal $y$ can be achieved at $\mbox{proj}_Wx$, and $d(x,W)=\|x-\mbox{proj}_Wx\|$.

# &#9989; **<font color=red>QUESTION:</font>** Let $v=(3, 2, 6)$ and $W$ is the subspace consisting all vectors with the form $(a, b, b)$. Find the projection of $v$ onto $W$.

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>** Let $v=(3, 2, 6)$ and $W$ is the subspace consisting all vectors with the form $(a, b, b)$. Find the distance from $v$ to $W$.

# Put your answer to the above question here

# ---
# <a name="The_Four_Fundamental_Spaces"></a>
#
# ## 2. The Four Fundamental Spaces
# In the lecture on *Change Basis*, we talked about four subspaces based on a matrix $A$: 
# > *Row space of $A$*: linear combination of all rows of $A$
#
# > *Column space of $A$*: linear combination of all columns of $A$
#
# > *Null space or kernel of $A$*: all $x$ such that $Ax=0$
#
# > *Null space of $A^\top$*: all $y$ such that $A^\top y =0$
#
#
#
#
# In this course we represent a system of linear equations as $Ax=b$. 
# The matrix $A$ can be viewed as taking a point $x$ in the input space and projecting that point to $b$ in the output space.  
#
#
# It turns out, everything we need to know about $A$ is represented by four fundamental vector spaces.  Two of the four spaces are easily defined as follows:
#
# > *Row space of $A$*: linear combination of all rows of $A$
#
# > *Column space of $A$*: linear combination of all columns of $A$
#
# The other two fundamental spaces are defined by a concept called the *Null Space*. 
# The *Null space* is calculated by finding all the solutions to the homogeneous system $Ax=0$. The final two fundamental spaces are defined as follows:
#
# > *Null space or kernel of $A$*: all $x$ such that $Ax=0$
#
# > *Null space of $A^\top$*: all $y$ such that $A^\top y =0$

# ----
#
# <a name="Independent_Learning"></a>
# ## 3. Independent Learning
#
# &#9989; **<font color=red>DO THIS:</font>** Find a YouTube video that helps you understand the four fundamental spaces.  
#
# &#9989; **<font color=red>QUESTION:</font>** What is the URL for your video? 

# Put your answer to the above question here

# &#9989; **<font color=red>DO THIS:</font>**  Add the link to the video to the code below. Try embedding the link in the provided Python YouTubeVideo Function by replacing XXXXX with the video ID.

from IPython.display import YouTubeVideo
YouTubeVideo("XXXXXX",width=640,height=360, cc_load_policy=1)

# &#9989; **<font color=red>QUESTION:</font>** What criteria did you use in selecting your video?

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>** How long into a video did you go before deciding if it was good or bad?

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>** What did you like about the video you selected.

# Put your answer to the above question here

# &#9989; **<font color=red>QUESTION:</font>** What didn't you like about the video?

# Put your answer to the above question here

# ----
#
# <a name="Assignment_wrap-up"></a>
# ## 4. Assignment_wrap-up

# &#9989; **<font color=red>Assignment-Specific QUESTION:</font>** What is the URL for your video for the four Fundamental spaces? 

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

# -----
#
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
