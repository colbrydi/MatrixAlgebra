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

# # 02 Pre-Class Assignment: Vectors

# ### Readings for this topic (Recommended in bold)
#  * [Heffron Chapter 1.II.1 pg 35-42](http://joshua.smcvt.edu/linearalgebra/book.pdf)
#  * [Beezer Chapter V pg 74-88](http://linear.ups.edu/download/fcla-3.50-tablet.pdf)
#  * [**_Boyd Sections 1.1-1.3 pg 1-19_**](http://vmls-book.stanford.edu/vmls.pdf)
#

# ### Assignment Overview
#
# 1. [Introducing the Course Textbooks](#Textbooks)
# 1. [Todays Reading](#Reading)
# 1. [Scalars, Vector and Tensors](#Scalars_Vector_and_Tensors)
# 2. [Assignment wrap-up](#Assignment_wrap-up)

# ----
# <a name="Textbooks"></a>
# ## 1. Introducing the Course Textbooks
# Student self guided learning through assigned readings are required for students to be successful.  The course strives to use Open Educational Resources (OER) to help reduce financial burden on the students.  To this end we have selected the following textbooks for reading assignments and supplemental examples:  
#
#
# * [Introduction to Applied Linear Algebra](http://vmls-book.stanford.edu/) by Boyd and Vandenberghe
# * [Linear Algebra](http://joshua.smcvt.edu/linearalgebra/) by Jim Heffron
# * [A First Course in Linear Algebra](http://linear.ups.edu/) by Robert A. Beezer
#
#
# **_DO NOT WORRY_** You will not be expected to read all three textbooks in this course!  In fact, we try to keep the reading at a reasonable level and focus on problem solving.  However, most students benefit from seeing material in multiple ways (Reading, Lecture, Practice, etc).  Different students (and instructors) also prefer different writing styles and may learn better with different text (which is why we provide more than one).  
#
# Students are encouraged to review and become familiar with the style and layout of each text to act as a common reference for the course.  If you get stuck on a topic try looking it up and reviewing it in one of the other texts.  If you are still stuck you can search the Internet.  Do not be afraid to also ask your instructors questions and come to office hours. That is why we are here!!!
#
# &#9989; **<span style="color:red">Do This:</span>** Download a copy of each textbooks onto your preferred reading device and review the **_Table of Contents_** in each text.
#
#
# As you can see each textbook approaches Linear algebra in a slightly different way. This variety reflects the different philosophies of teaching and different ways of individual learning. One way to evaluate the focus of a particular textbook is to look at it's very first chapter.  For Example:
#
# * The **_Beezer_** and **_Heffron_** texts start out with "Systems of linear Equations" and "Linear Systems." These topics are basically the same idea with the focus of defining linear systems as just sets of "linear combinations".  Clearly this is a core concept and a good place to start.
# * The **_Boyd and Vandenberghe_** text choose to start with "Vectors".  In linear algebra the "vector" is a mathematical tool for which all of the mechanics of the math is built.  Again, not a bad place to start. 
#
# In the first few assignments this course we will be looking at both concepts.  You will want to learn and be able to identify linear systems and how to represent them as vectors. 

# &#9989; **<span style="color:red">Question:</span>** Find three additional topics (Besides Linear Systems and Vectors) that seem to be common between the three textbooks. You can probably assume that these topics will be important to our course as well.

# Put your answer to the above question here.

# ----
# <a name="Reading"></a>
# ## 2. Today's Reading
#
# Quite a bit of this pre-class assignment about vectors is motivated from Chapter 1 of the [Stephen Boyd and Lieven Vandenberghe Applied Linear algebra book](http://vmls-book.stanford.edu/).  This material may be review for some students and may be new for others. It is expected that students review the chapter to help them understand the material better.  
#
# &#9989; **<span style="color:red">Do This:</span>**  Review **_Sections 1.1, 1.2 and 1.3 in Boyd and Vandenberghe_** and become familiar with the contents and the basic terminology.  If you find this material is difficult make sure you take advantage of the survey at the end of this assignment to ask your instructor questions about things that are confusing.  
#
# **_HINT_** Many computers and smart phones have a "read to me feature". Some students find it helpful to download the pdf of the textbook and have the computer read to them out loud while they follow along. 

# ----
# <a name="Scalars_Vector_and_Tensors"></a>
# ## 3. Scalars, Vector and Tensors
#
# The two primary mathematical entities that are of interest in linear algebra are the vector and the matrix. They are examples of a more general entity known as a tensor. The following video gives a basic introduction of scalars, vectors, and tensors. It is fine if you can not understand all of this video. We will learn most of it in this course. 
#
#
# _**NOTE:**_ The terms vectors and tensors can get fairly confusing. For the purpose of this class, we will not use the term _**Tensor**_ all that much.  Instead we will treat everything as **_vectors_** (more on this later).  
#
# * [Direct Link to YouTube Video](https://www.youtube.com/watch?v=ml4NSzCQobk)

from IPython.display import YouTubeVideo
YouTubeVideo("ml4NSzCQobk",width=640,height=360, cc_load_policy=True)

# Think of a **_scalar_** as a single number or variable that is an example of a 0th-order tensor. The following are all scalars:
#
# $$ 1, \frac{1}{2}, 3.1416$$
#
# Defining a **_scalar_** in Python is easy. For example

a = 8
a

# A **_vector_**, on the other hand, is an *ordered* list of values which we typically represent with lower case letters. Vectors are ordered arrays of single numbers and are an example of 1st-order tensor. The following are all vectors:
#
# **_Row Vector:_** 
# $$v = [ v_1, v_2, \dots, v_n ]$$
# here $v_1, v_2, \dots, v_n$ are single numbers.
#
# $$f = [1, 2, 3, 5, 8]$$
#
# Here $f$ in the above example is a vector of numbers, and it is the common way we think of vectors.
#
# Note, it is often more common to write vecors vertically. These are often called column vectors:
#
# **_Column Vector:_**
# $$
# v=
# \left[
# \begin{matrix}
#     v_1 \\ 
#     v_2 \\
#     \vdots \\
#     v_m
#  \end{matrix}
# \right]
# $$
# here $v_1, v_2, \dots, v_n$ are single numbers.
#
#
#
# ### 1.a: Introducing Vectors in Python
# In Python, there are multiple ways to store a vector.  Knowing how your vector is stored is very important (especially for debugging).  Probably the easiest way to store a vector is using a list, which are created using standard square brackets as follows:

f = [1, 2, 3, 5, 8]
f

# Another common way to store a vector is to use a tuple.  

b = (2, 4, 8, 16)
b

# You can access a particular scalar in your Python object using its index. Remember that Python index starts counting at zero. For example, to get the fourth element in ```f``` and ```b``` vectors, we would use the following syntax:

print(f[3])
print(b[3])

# Later in this course, we may discuss which data format is better (and introduce new ones). At this point let's not worry about it too much. You can always figure out a variable's data type using the ```type``` function. For example:

type(f)

type(b)

# Finally, I am not sure if you will need this but always remember, it is easy to convert from a tuple to a list and vice versa (this is called "casting"):

#Convert tuple to list
b_list = list(b)
b_list

#Convert list to tuple
f_list = tuple(f)
f_list

# ### 1.b: Vector size 
#
# A vector can be used to represent quantities or values in an application. The size (also called dimension or length) of the vector is the number of elements it contains.  The size of the vector determines how many quantities are in the vector.  We often refer to the size of a vector using the variable ```n```.  So an ```n-vector``` has ```n``` values.  A ```3-vector``` only has 3 values. 
#
# The length (```len```) function returns the size of a vector in Python:

len(f)

len(b)

# ### 1.c: Special Vectors
# The following are special vectors with special names.
#
# #### Standard Unit Vectors
# Vectors with a single 1 and the rest of the values are zero have a special name called "Standard Unit Vectors". The number of different standard unit vectors there are is equal to the size of the vector. For example, a 3-vector has the following standard unit vectors:
#
# $$
# e_1 = 
# \left[
# \begin{matrix}
#     1 \\ 
#     0 \\
#     0
#  \end{matrix}
# \right]
# ,e_2 = 
# \left[
# \begin{matrix}
#     0 \\ 
#     1 \\
#     0
#  \end{matrix}
# \right],
# e_3 = 
# \left[
# \begin{matrix}
#     0 \\ 
#     0 \\
#     1
#  \end{matrix}
# \right]
# $$
#
# #### Zero Vectors
# Vectors with all values of zero also have a special name called "Zero Vectors". Typically we just use a zero to represent the zero vector. For example:
# $$
# 0 = 
# \left[
# \begin{matrix}
#     0 \\ 
#     0 \\
#     0
#  \end{matrix}
# \right]
# $$
#

# ### 1.d: Examples
#
#
# Vectors are used to represent all types of data that has structures.  Here are some simple examples from the [Boyd and Vandenberghe textbook](http://vmls-book.stanford.edu/):
#
#
# #### Location and displacement
# A 2-vector can be used to represent a position or location in a space.  The first value is the distance in one direction (from the origin) and the second value is the distance in a different direction.  Probably most students are famiar with the 2D Cartesian coordinate system where a location can be defined by two values in the ```x``` and ```y``` directions.  Here is a simple scatter plot in python which show the concept:

# +
# %matplotlib inline
import matplotlib.pylab as plt
p1 = [2, 1]
p2 = [1, 3]
p3 = [1, 1]

plt.plot(p1[0],p1[1],'*k')
plt.plot(p2[0],p2[1],'*k')
plt.plot(p3[0],p3[1],'*k')

## Add some labels (offset slightly)
plt.text(p1[0]+0.1,p1[1],'$p_1$')
plt.text(p2[0]+0.1,p2[1],'$p_2$')
plt.text(p3[0]+0.1,p3[1],'$p_3$')

## Fix the axis so you can see the points
plt.axis([0,4,0,4])
# -

# #### Color
# A 3-vector can represent a color, with its entries giving the Red, Green, and Blue (RGB) intensity values (often between 0 and 1). The vector (0,0,0) represents black, the vector (0, 1, 0) represents a bright pure green color, and the vector (1, 0.5, 0.5) represents a shade of pink. 
#
# The Python ```matplotlib``` library uses this type of vector to define colors.  For example, the following code plots a point at the origin of size 10000 (the size of the circle, and the value does not have exact meaning here) and color c = (0,1,0).  You can change the values for ```c``` and ```s``` to see the difference.

# +
import warnings
warnings.filterwarnings("ignore")

c = (0, 1, 0)
plt.scatter(0,0, color=c, s=10000);
# -

# Just for fun, here is a little interactive demo that lets you play with different color vectors. 
#
#
# > **_NOTE_** this demo uses the ```ipywidgets``` Python library which works by default in Jupyter notebook (which is installed on the MSU [jupyterhub](http://jupyterhub.egr.msu.edu))) but **_NOT_** in the newer jupyter lab interface which some students may have installed on their local computers.  To get these types of examples working in jupyter lab requires the installation of the ipywidgets plug-in. 

# +
# %matplotlib inline
import matplotlib.pylab as plt
from ipywidgets import interact, fixed

def showcolor(red,green,blue):
    color=(red,green,blue)
    plt.scatter(0,0, color=color, s=20000);
    plt.axis('off');
    plt.show();
    return color

color = interact(showcolor, red=(0.0,1.0), green=(0.0,1.0), blue=(0.0,1.0));
# -

# ### 1.e: Vector Addition
#
# Two vectors of the same size can be added together by adding the corresponding elements, to form another vector of the same size, called the sum of the vectors. For example:
#
# $$ 
# \left[
# \begin{matrix}
#     1  \\ 
#     20   
#  \end{matrix}
#  \right]
#  +
# \left[
# \begin{matrix}
#     22 \\ 
#     -3 
#  \end{matrix}
#  \right]
#   =
# \left[
# \begin{matrix}
#     23 \\ 
#     17 
#  \end{matrix}
# \right]
# $$

# #### Python Vector Addition
#
# Here is where things get tricky in Python.  If you try to add a list or tuple, Python does not do the vector addition as we defined above. In the following examples, notice that the two lists concatenate instead of adding by element: 

## THIS IS WRONG
a = [1, 20]
b = [22,-3]
c = a+b
c

## THIS IS ALSO WRONG
a = (1, 20)
b = (22,-3)
c = a+b
c

# To do proper vector math you need either use a special function (we will learn these) or loop over the list.  Here is a very simplistic example:

a = (1, 20)
b = (22,-3)
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])
c


# For fun, we can define this operation as a function in case we want to use it later:

def vecadd(a,b):
    """Function to add two equal size vectors."""
    if (len(a) != len(b)):
        raise Exception('Error - vector lengths do not match')
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c


# +
#Lets test it

vecadd(a,b)
# -

# ### 1.f: Scalar-Vector multiplication
#
# You can also multiply a scalar by a vector, which is done by multiplying every element of the vector by the scalar. 
#
#
# $$ 
# 3
# \left[
# \begin{matrix}
#     3 \\ 
#     -7 \\
#     10
#  \end{matrix}
#  \right]
#   =
# \left[
# \begin{matrix}
#     9 \\ 
#     -21 \\
#     30
#  \end{matrix}
# \right]
# $$
#

# #### Scalar-Vector Multiplication in Python
# Again, this can be tricky in Python because Python lists do not do what we want.  Consider the following example that just concatenates three copies of the vector. 

##THIS IS WRONG## 
z = 3
a = [3,-7,10]
c = z*a
c

# Again, in order to do proper vector math in Python you need either use a special function (we will learn these) or loop over the list.  

# &#9989; **<span style="color:red">Do This:</span>**  See if you can make a simple function with a loop to multiply a scalar by a vector. Name your function ```sv_multiply``` and test it using the cells below:

# +
#put your sv_multiply function here
# -

#Test your function here
z = 3
a = [3,-7,10]
sv_multiply(z,a)

# Let us use the following code to test your functon further.  Note that this uses the ```answercheck``` function provided by your instructors. Please review [01--Python_Packages](01-Python_Packages.ipynb) for instructions on installing and using ```answercheck```.

from answercheck import checkanswer
checkanswer.vector(sv_multiply(10,[1,2,3,4]),'414a6fea724cafda66ab5971f542adf2')

from answercheck import checkanswer
checkanswer.vector(sv_multiply(3.14159,(1,2,3,4)),'f349ef7cafae77c7c23d6924ec1fd36e')

# ----
#
# <a name="Assignment_wrap-up"></a>
# ## 4. Assignment wrap-up
#
#

# &#9989; **<span style="color:red">Assignment-Specific QUESTION:</span>** Are you able to get the sv_multiply function working in part 1 of this assignment? If not, where did you get stuck?

# Put your answer to the above question here

# &#9989; **<span style="color:red">QUESTION:</span>** Summarize what you did in this assignment.

# Put your answer to the above question here

# &#9989; **<span style="color:red">QUESTION:</span>**  What questions do you have, if any, about any of the topics discussed in this assignment after working through the jupyter notebook?

# Put your answer to the above question here

# &#9989; **<span style="color:red">QUESTION:</span>**   How well do you feel this assignment helped you to achieve a better understanding of the above mentioned topic(s)?

# Put your answer to the above question here

# &#9989; **<span style="color:red">QUESTION:</span>**  What was the **most** challenging part of this assignment for you? 

# Put your answer to the above question here

# &#9989; **<span style="color:red">QUESTION:</span>**  What was the **least** challenging part of this assignment for you? 

# Put your answer to the above question here

# &#9989; **<span style="color:red">QUESTION:</span>**   What kind of additional questions or support, if any, do you feel you need to have a better understanding of the content in this assignment?

# Put your answer to the above question here

# &#9989; **<span style="color:red">QUESTION:</span>**  Do you have any further questions or comments about this material, or anything else that's going on in class?

# Put your answer to the above question here

# &#9989; **<span style="color:red">QUESTION:</span>**  Approximately how long did this pre-class assignment take?

# Put your answer to the above question here

# ----
#
# Written by Dr. Dirk Colbry, Michigan State University
#
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a>
#
# This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
