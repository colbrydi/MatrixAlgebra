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

#
# # 15 In-Class Assignment: Diagonalization
#
# <img alt="Classig equation for diagonalizing a matrix. Will be discussed in class" src="https://wikimedia.org/api/rest_v1/media/math/render/svg/62ab0ef52ecb1e1452efe6acf096923035c75f62" width="50%">
#
# Image from: [https://en.wikipedia.org/wiki/Diagonalizable_matrix](https://en.wikipedia.org/wiki/Diagonalizable_matrix)
#
#     

# ### Agenda for today's class (80 minutes)
#
# 1. [(20 minutes) Pre-class Assignment Review](#Pre-class_Assignment_Review)
# 1. [(20 minutes) Diagonalization](#Diagonalization)
# 1. [(20 minutes) The Power of a Matrix](#The_Power_of_a_Matrix)
#

# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import sympy as sym
sym.init_printing()

# ---
# <a name="Pre-class_Assignment_Review"></a>
# ## 1. Pre-class Assignment Review

# * [15--Diagonalization_pre-class-assignment.ipynb](15--Diagonalization_pre-class-assignment.ipynb)

# ----
# <a name="Diagonalization"></a>
# ## 2. Diagonalization

# **_Reminder_**: The eigenvalues of triangular (upper and lower) and diagonal matrices are easy:
#
# * The eigenvalues for triangular matrices are the diagonal elements.
# * The eigenvalues for the diagonal matrices are the diagonal elements. 

# ### Diagonalization
#
#
# **Definition**: A square matrix $A$ is said to be *diagonalizable* if there exist a matrix $C$ such that $D=C^{-1}AC$ is a diagonal matrix.
#
# **Definition**: $B$ is a *similar matrix* of $A$ if we can find $C$ such that $B=C^{-1}AC$.
#
#
# Given an $n\times n$ matrix $A$, can we find another $n \times n$ invertable matrix $C$ such that when $D=C^{-1}AC$ is diagonal, i.e., $A$ is diagonalizable?

# * Because $C$ is inveritble, we have 
# $$C^{-1}AC=D \\ CC^{-1}AC = CD\\ AC = CD $$
#
#
# * Generate $C$ as the columns of $n$ linearly independent vectors $(x_1...x_n)$ We can compute $AC=CD$ as follows:
# $$ A\begin{bmatrix} \vdots  & \vdots  & \vdots  & \vdots  \\ \vdots  & \vdots  & \vdots  & \vdots  \\ { x }_{ 1 } & { x }_{ 2 } & \dots  & { x }_{ n } \\ \vdots  & \vdots  & \vdots  & \vdots  \end{bmatrix}=AC=CD=\begin{bmatrix} \vdots  & \vdots  & \vdots  & \vdots  \\ \vdots  & \vdots  & \vdots  & \vdots  \\ { x }_{ 1 } & { x }_{ 2 } & \dots  & { x }_{ n } \\ \vdots  & \vdots  & \vdots  & \vdots  \end{bmatrix}\begin{bmatrix} { \lambda  }_{ 1 } & 0 & 0 & 0 \\ 0 & { \lambda  }_{ 2 } & 0 & 0 \\ \vdots  & \vdots  & { \dots  } & \vdots  \\ 0 & 0 & 0 & { \lambda  }_{ n } \end{bmatrix}$$
# * Then we check the corresponding columns of the both sides. We have 
# $$Ax_1 = \lambda_1x_1\\\vdots\\Ax_n=\lambda x_n$$
#
# * $A$ has $n$ linear independent eigenvectors.
#
# * $A$ is saied to be *similar* to the diagonal matrix $D$, and the transformation of $A$ into $D$ is called a *similarity transformation*.

# ### A simple example
#
# Consider the following:
# $$ A = \begin{bmatrix}7& -10\\3& -4\end{bmatrix},\quad C = \begin{bmatrix}2& 5\\1& 3\end{bmatrix}$$

# &#9989;  **<font color=red>Do this:</font>** Find the similar matrix $D = C^{-1}AC$ of $A$.

# +
#Put your answer to the above question here.

# + nbgrader={"grade": true, "grade_id": "cell-3cdb9915439d45fe", "locked": true, "points": 5, "schema_version": 3, "solution": false, "task": false}
from answercheck import checkanswer

checkanswer.matrix(D, '8313fe0f529090d6a8cdb36248cfdd6c');
# -

# &#9989;  **<font color=red>Do this:</font>** Find the eigenvalues and eigenvectors of $A$. Set variables ```e1``` and ```vec1``` to be the smallest eigenvalue and its associated eigenvector and ```e2, vec2``` to represent the  largest.

# +
#Put your answer to the above question here.

# + nbgrader={"grade": true, "grade_id": "cell-f4fda102502f50f9", "locked": true, "points": 5, "schema_version": 3, "solution": false, "task": false}
from answercheck import checkanswer
checkanswer.float(e1, "e4c2e8edac362acab7123654b9e73432");

# + nbgrader={"grade": true, "grade_id": "cell-88300f29b8aec498", "locked": true, "points": 5, "schema_version": 3, "solution": false, "task": false}
from answercheck import checkanswer
checkanswer.float(e2, "d1bd83a33f1a841ab7fda32449746cc4");

# + nbgrader={"grade": true, "grade_id": "cell-f26e2f5a3e41bdd8", "locked": true, "points": 5, "schema_version": 3, "solution": false, "task": false}
from answercheck import checkanswer
checkanswer.eq_vector(vec1, "d28f0a721eedb3d5a4c714744883932e", decimal_accuracy = 4)

# + nbgrader={"grade": true, "grade_id": "cell-a0ef501c592a3fcc", "locked": true, "points": 5, "schema_version": 3, "solution": false, "task": false}
from answercheck import checkanswer
checkanswer.eq_vector(vec2, "09d9df5806bc8ef975074779da1f1023", decimal_accuracy = 4)
# -

# **Theorem:** Similar matrices have the same eigenvalues.
#
# **Proof:** Assume $B=C^{-1}AC$ is a similar matrix of $A$, and $\lambda$ is an eigenvalue of $A$ with corresponding eigenvector $x$. That is, $$Ax=\lambda x$$ 
# Then we have $$B(C^{-1}x) = C^{-1}AC(C^{-1}x) = C^{-1}Ax = C^{-1}(\lambda x)= \lambda (C^{-1}x).$$
# That is $C^{-1}x$ is an eigenvector of $B$ with eigenvalue $\lambda$.     

# ### A second example
#
# &#9989;  **<font color=red>Do this:</font>** Consider 
# $$ A = \begin{bmatrix}-4& -6\\3& 5\end{bmatrix}.$$
# Find a matrix $C$ such that $C^{-1}AC$ is diagonal. (Hint, use the function `diagonalize` in `sympy`.)

# +
#Put your answer to the above question here. 

# + nbgrader={"grade": true, "grade_id": "cell-d9c7ff4aa895199e", "locked": true, "points": 5, "schema_version": 3, "solution": false, "task": false}
#Check the output type
assert(type(C)==sym.Matrix)

# + nbgrader={"grade": true, "grade_id": "cell-2c06b41f80b7a258", "locked": true, "points": 5, "schema_version": 3, "solution": false, "task": false}
from answercheck import checkanswer
checkanswer.matrix(C,'ba963b7fef354b4a7ddd880ca4bac071')
# -

# ### The third example
#
# &#9989;  **<font color=red>Do this:</font>** Consider 
# $$ A = \begin{bmatrix}5& -3\\3& -1\end{bmatrix}.$$
# Can we find a matrix $C$ such that $C^{-1}AC$ is diagonal?  (Hint: find eigenvalues and eigenvectors using `sympy`)

# + nbgrader={"grade": true, "grade_id": "cell-8eb9fd1f4a5a6136", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}
#Put your answer to the above question here. 
# -

# ### Dimensions of eigenspaces and diagonalization
#
# **Definition**: The set of all eigenvectors of a $n\times n$ matrix corresponding to a eigenvalue $\lambda$, together with the zero vector, is a subspace of $R^n$. This subspace spaces is called *eigenspace*.
#
# * For the third example, we have that the characteristic equation $(\lambda-2)^2=0$.
# * Eigenvalue $\lambda=2$ has multiplicity 2, but the eigenspace has dimension 1, since we can not find two lineare independent eigenvector for $\lambda =2$. 
#
# > The dimension of an eigenspace of a matrix is less than or equal to the multiplicity of the corresponding eigenvalue as a root of the characteristic equation.
#
# > A matrix is diagonalizable if and only if the dimension of every eigenspace is equal to the multiplicity of the corresponding eigenvalue as a root of the characteristic equation.

# ### The fourth example
#
# &#9989;  **<font color=red>Do this:</font>** Consider 
# $$ A = \begin{bmatrix}2& -1\\1& 2\end{bmatrix}.$$
# Can we find a matrix $C$ such that $C^{-1}AC$ is diagonal?

# + nbgrader={"grade": true, "grade_id": "cell-3bc59d8f51537cae", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}
#Put your answer to the above question here. 
# -

# ---
#
# <a name="The_Power_of_a_Matrix"></a>
# ## 3. The Power of a Matrix
#
# * For a diagonalizable matrix $A$, we have $C^{-1}AC=D$. Then we have 
# $$A = C D C^{-1}$$
# * We have 
# $$A^2 = C D C^{-1} C D C^{-1} = C D^2 C^{-1}$$
# $$A^n = C D C^{-1} \dots C D C^{-1} = C D^n C^{-1}$$
# * Because the columns of $C$ are eigenvectors, so we can say that the eigenvectors for $A$ and $A^n$ are the same if $A$ is diagonalizable. 
# * If $x$ is an eigenvector of $A$ with the corresponding eigenvalue $\lambda$, then $x$ is also an eigenvector of $A^n$ with the corresponding eigenvalue $\lambda^n$.

# Here are some libraries you may need to use
# %matplotlib inline
import numpy as np
import sympy as sym
import networkx as nx
import matplotlib.pyplot as plt
sym.init_printing(use_unicode=True)

# ### Graph Random Walk
#
# * Define the following matrices:
#     * $I$ is the identity matrix
#     * $A$ is the adjacency matrix
#     * $D$ is diagonal matrix of degrees (number of edges connected to each node)
#     
# $$W=\frac{1}{2}(I + AD^{-1})$$
#
# * The **lazy random walk matrix**, $W$, takes a distribution vector of *stuff*, $p_{t}$, and diffuses it to its neighbors:
#
# $$p_{t+1}=Wp_{t}$$
#
# * For some initial distribution of *stuff*, $p_{0}$, we can compute how much of it would be at each node at time, $t$, by powering $W$ as follows:
#
# $$p_{t}=W^{t}p_{0}$$
#
# * Plugging in the above expression yields:
#
# $$p_{t}=\left( \frac{1}{2}(I+AD^{-1}) \right)^t p_{0}$$

# **<font color=red>DO THIS</font>**: Using matrix algebra, show that $\frac{1}{2}(I + AD^{-1})$ is **similar** to  $I-\frac{1}{2}N$, where $N=D^{-\frac{1}{2}}(D-A)D^{-\frac{1}{2}}$ is the normalized graph Laplacian. 

# + [markdown] nbgrader={"grade": true, "grade_id": "cell-1a93e034adef3eb1", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}
# **Your answer goes here** (follow along after attempting)
# -

# ### Random Walk on Barbell Graph
#
# To generate the barbell graph, run the following cell.

# +
n = 60 # number of nodes
B = nx.Graph() # initialize graph

## initialize empty edge lists
edge_list_complete_1 = [] 
edge_list_complete_2 = []
edge_list_path = []

## generate node lists
node_list_complete_1 = np.arange(int(n/3))
node_list_complete_2 = np.arange(int(2*n/3),n)
node_list_path = np.arange(int(n/3)-1,int(2*n/3))

## generate edge sets for barbell graph
for u in node_list_complete_1:
    for v in np.arange(u+1,int(n/3)):
        edge_list_complete_1.append((u,v))
        
for u in node_list_complete_2:
    for v in np.arange(u+1,n):
        edge_list_complete_2.append((u,v))

for u in node_list_path:
    edge_list_path.append((u,u+1))

# G.remove_edges_from([(3,0),(5,7),(0,7),(3,5)])

## add edges
B.add_edges_from(edge_list_complete_1)
B.add_edges_from(edge_list_complete_2)
B.add_edges_from(edge_list_path)


## draw graph
pos=nx.spring_layout(B) # positions for all nodes

### nodes
nx.draw_networkx_nodes(B,pos,
                       nodelist=list(node_list_complete_1),
                       node_color='c',
                       node_size=400,
                       alpha=0.8)
nx.draw_networkx_nodes(B,pos,
                       nodelist=list(node_list_path),
                       node_color='g',
                       node_size=200,
                       alpha=0.8)
nx.draw_networkx_nodes(B,pos,
                       nodelist=list(node_list_complete_2),
                       node_color='b',
                       node_size=400,
                       alpha=0.8)


### edges
nx.draw_networkx_edges(B,pos,
                       edgelist=edge_list_complete_1,
                       width=2,alpha=0.5,edge_color='c')
nx.draw_networkx_edges(B,pos,
                       edgelist=edge_list_path,
                       width=3,alpha=0.5,edge_color='g')
nx.draw_networkx_edges(B,pos,
                       edgelist=edge_list_complete_2,
                       width=2,alpha=0.5,edge_color='b')


plt.axis('off')
plt.show() # display
# -

# &#9989;  **<font color=red>Do this</font>:** Generate the lazy random walk matrix, $W$, for the above graph.

# +

A = nx.adjacency_matrix(B)
A = A.todense()

d = np.sum(A,0) # Make a vector of the sums.
D = np.diag(np.asarray(d)[0])


# +
#Put your answer to the above question here.

# + nbgrader={"grade": true, "grade_id": "cell-fb79da016761443e", "locked": true, "points": 5, "schema_version": 3, "solution": false, "task": false}
from answercheck import checkanswer
checkanswer.matrix(W, "7af4a5b11892da6e1a605c8239b62093")
# -

# &#9989;  **<font color=red>Do this</font>:** Compute the eigenvalues and eigenvectors of $W$. Make a diagonal matrix $J$ with the eigenvalues on the diagonal. Name the matrix of eigenvectors $V$ (each column is an eigenvector).

# +
#Put your answer to the above question here. 
# -

# Now we make sure we constructed $V$ and $A$ correctly by double checking that $W = VJV^{-1}$

np.allclose(W, V*J*np.linalg.inv(V))

# &#9989;  **<font color=red>Do this</font>:** Let your $p_{0}=[1,0,0,\ldots,0]$. Compute $p_{t}$ for $t=1,2,\ldots,100$, and plot $||v_{1}-p_{t}||_{1}$ versus $t$, where $v_{1}$ is the eigenvector associated with the largest eigenvalue $\lambda_{1}=1$ and whose sum equals 1. (**Note**: $||\cdot||_{1}$ may be computed using ```np.linalg.norm(v_1-p_t, 1)```.)

# + nbgrader={"grade": true, "grade_id": "cell-9e691ac811c35e4d", "locked": false, "points": 5, "schema_version": 3, "solution": true, "task": false}
#Put your answer to the above question here. 
# -

# #### Compare to Complete Graph
#
# If you complete the above, do the same for a complete graph on the same number of nodes.
#
# &#9989;  **<font color=red>Question</font>:** What do you notice about the graph that is different from that above?

# + [markdown] nbgrader={"grade": true, "grade_id": "cell-9cadbdd3014757bc", "locked": false, "points": 5, "schema_version": 3, "solution": true, "task": false}
# Put your answer to the above question here.
# -

# ----
# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
