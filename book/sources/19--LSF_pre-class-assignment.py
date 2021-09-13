# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
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

# # 19 Pre-Class Assignment: Least Squares Fit (Regression)

# ### Readings for this topic (Recommended in bold)
#  * [Heffron Chapter 3 pg 287-292](http://joshua.smcvt.edu/linearalgebra/book.pdf)
#  * [**_Boyd Chapter 13 pg 225-239_**](http://vmls-book.stanford.edu/vmls.pdf)
#

#
# ### Goals for today's pre-class assignment 
#
# 1. [Least Squares Fit](#Least_Squares_Fit)
# 1. [Linear Regression](#Linear_Regression)
# 1. [One-to-one and Inverse transform](#One-to-one_and_Inverse_transform)
# 1. [Inverse of a Matrix](#Inverse_of_a_Matrix)
# 1. [Assignment Wrap-up](#Assignment_Wrap-up)

# ----
# <a name="Least_Squares_Fit"></a>
# ## 1. Least Squares Fit
#
# **Review Chapters Chapter 13 pg 225-239 of the Boyd textbook.**
#
# In this first part of this course, we try to solve the system of linear equations $Ax=b$ with an $m\times n$ matrix $A$ and a column vector $b$. 
#
# There are three possible outcomes: an unique solution, no solution, and infinite many solutions. 
# (Review the material on this part if you are no familiar with when the three types of outcomes happen.)
#
# When $m<n$, we call the matrix $A$ underdeterminated, because we can not have an unique solution for it. 
# When $m>n$, we call the matrix $A$ overdeterminated, becasue we may not have a solution with high probability. 
#
# However, if we still need to find a best $x$, even when there is no solution or infinite many solutions we use a technique called least squares fit (LSF). Least squares fit find $x$ such that $\|Ax-b\|$ is the smallest (i.e. we try to minimize the estimation error).

# + When there is no solution, we want to find $x$ such that $Ax-b$ is small (here, we want $\|Ax-b\|$ to be small).

# + If the null space of $A$ is just $\ {"incorrectly_encoded_metadata": "{0\\}$, we can find an unique $x$ to obtain the smallest $\\|Ax-b\\|$."}

# + If there is a unique solution $x^*$ for {"incorrectly_encoded_metadata": "$Ax=b$, then $x^*$ is the optimal $x$ to obtain the smallest $\\|Ax-b\\|$, which is 0."}

# + Because the null space of $A$ is just $\ {"incorrectly_encoded_metadata": "{0\\}$, you can not have infinite many solutions for $Ax=b$."}

# + If the null space of $A$ is not just $\ {"incorrectly_encoded_metadata": "{0\\}$, we know that we can always add a nonzero point $x_0$ in the null space of $A$ to a best $x^*$, and $\\|A(x^*+x_0)-b\\|=\\|Ax^*-b\\|$. Therefore, when we have multiple best solutions, we choose to find the $x$ in the rowspace of $A$, and this is unique."}

# **<font color=red>QUESTION 1:</font>** Let $$A=\begin{bmatrix}1\\2\end{bmatrix},\quad b=\begin{bmatrix}1.5 \\ 2\end{bmatrix}$$
# Find the best $x$ such that $\|Ax-b\|$ has the smallest value.

# Put your answer to the above question here.

# **<font color=red>QUESTION 2:</font>** Compute $(A^\top A)^{-1}A^\top b$.

# Put your answer to the above question here.

# ----
# <a name="Linear_Regression"></a>
# ## 2. Linear Regression
#
# Watch the video for using Least Squares to do linear regression.

from IPython.display import YouTubeVideo
YouTubeVideo("Lx6CfgKVIuE",width=640,height=360, cc_load_policy=True)

# **<font color=red>QUESTION 3:</font>** How to tell it is a good fit or a bad one?

# Put your answer to the above question here.

# ----
# <a name="One-to-one_and_Inverse_transform"></a>
# ## 3. One-to-one and Inverse transform
#
# Read Section 4.9 of the textbook if you are not familiar with this part. 
#
# **Definition:** A transformation $T:U\mapsto V$ is said to be *one-to-one* if each element in the range is the image of just one element in the domain. That is, for two elements ($x$ and $y$) in $U$. $T(x)=T(y)$ happens only when $x=y$.
#
# **Theorem:** Let $T:U\mapsto V$ be a one-to-one linear transformation. If $\{u_1,\dots,u_n\}$ is linearly independent in $U$, then $\{T(u_1),\dots,T(u_n)\}$ is linearly independent in $V$. 
#
# **Definition:** A linear transformation $T:U\mapsto V$ is said to be *invertible* if there exists a transformation $S:V\mapsto U$, such that 
# $$S(T(u))=u,\qquad T(S(v))=v,$$
# for any $v$ in $V$ and any $u$ in $U$.

# **<font color=red>QUESTION 4:</font>** If linear transformation $T:U\mapsto V$ is invertible, and the dimension of $U$ is 2, what is the dimension of $V$? Why?

# Put your answer to the above question here.

# ----
# <a name="Inverse_of_a_Matrix"></a>
# ## 4. Inverse of a Matrix
#
# + Recall the four fundamental subspaces of a $m\times n$ matrix $A$

# + The rowspace and nullspace of $A$ in $R^n$

# + The columnspace and the nullspace of $A^\top$ in $R^m$


# + The two-sided inverse gives us the following
# $$ {A}{A}^{-1}=I={A}^{-1}{A} $$
# + For this we need {"incorrectly_encoded_metadata": "$r = m = n$, here $r$", "is": null, "matrix.": null, "of": null, "rank": null, "the": null}


# + For a left-inverse, we have the following

# + Full column rank, with {"incorrectly_encoded_metadata": "$r = n \\leq m$ (but possibly more rows)"}

# + The nullspace contains just the zero vector (columns are independent)

# + The rows might not all be independent

# + We thus have either no or only a single solution to {"incorrectly_encoded_metadata": "$Ax=b$."}

# + $A^\top $ will now also have full row rank

# + From $(A^\top A)^ {"incorrectly_encoded_metadata": "{-1}A^\\top A = I$ follows the fact that $(A^\\top A)^{-1}A^\\top$ is a left-sided inverse"}

# + Note that $(A^\top A)^ {"incorrectly_encoded_metadata": "{-1}A^\\top$ is a $n\\times m$ matrix and $A$ is of size $m\\times n$, theire mulitiplication $(A^\\top A)^{-1}A^\\top A$ results in a $n\\times n$ identity matrix"}

# + The $A(A^\top A)^ {"incorrectly_encoded_metadata": "{-1}A^\\top$ is a $m\\times m$ matrix. BUT $A(A^\\top A)^{-1}A^\\top\\neq I$ if $m\\neq n$. The matrix $A(A^\\top A)^{-1}A^\\top$ is the projection matrix onto the column space of $A$."}

# **<font color=red>QUESTION 5:</font>** What is the projection matrix that projects any vector onto the subspace spanned by $[1,2]^\top$. (What matrix will give the same result as projecting any point onto the vector $[1,2]^\top$.)

# Put your answer to the above question here.

# **<font color=red>QUESTION 6:</font>** If $m=n$, is the left inverse the same as the inverse?

# Put your answer to the above question here.

# **Theorem:** For a matrix $A$ with $r=n<m$, the columnspace of $A$ has dimension $r(=n)$. The linear transfrom $A: R^n\mapsto R^m$ is one-to-one. In addition, the linear transformation $A$ from $R^n$ to the columnspace of $A$ is one-to-one and onto (it means that for any element in the columnspace of $A$, we can find $x$ in $R^n$ such that it equals $Ax$.) 
# Then the left inverse of $A$ is a one-to-one mapping from the columnspace of $A$ to $R^n$, and it can be considered as an inverse transform of $A$. 

# ----
#
# <a name="Assignment_Wrap-up"></a>
# ## 3. Assignment wrap-up

# &#9989; **<font color=red>Assignment-Specific QUESTION:</font>** There is no Assignment specific question for this notebook. You can just say "none".

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
