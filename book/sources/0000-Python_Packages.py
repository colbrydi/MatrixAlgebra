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

# [Link to this document's Jupyter Notebook](0000-Python_Packages.ipynb)

# # Python Linear Algebra Packages
#
# This tutorial is designed to provide a review of the Python packages we will be using in this course.  
#
# I think even experienced Python programmers may learn something from the videos. However, feel free to run them at a faster speed.

# ---
# ### Assignment Overview
#
# 1. [AnswerCheck tool](#answercheck)
# 1. [Review of Python Math Package](#Math)
# 3. [Review of Python Numpy Package](#Numpy)
# 4. [Advanced Python Indexing](#Indexing)
# 5. [LaTeX Math](#Latex)
# 6. [Assignment wrap-up](#Assignment_wrap-up)

# ----
# <a name="answercheck"></a>
#
# ## 1. AnswerCheck tool
#
# The ```jupytercheck``` Package is intended to provide students with immediate feedback to check answers inside of a Jupyter notebook. This was written with a Linear Algebra class in mind so it tries to do a robust comparison and take into consideration different object types as well as round off errors.
#
# It works by providing a function called ```answercheck``` that takes in a variable to be checked and a "hash" which is a one-way function encoding the answer. The program generates a new hash based on the input variable and compares the two hash values. An output is provided that the answer appears correct or incorrect.
#
# The program is also designed to run without installing anything in python. However, it does require the download of the correct file.
#

# &#9989; **<font color=red>DO THIS:</font>** Two use ```answercheck``` we will need to download ```answercheck.py``` to your current working directory.  You only really need to do this once.  However, if you delete this file by mistake sometime during the semester, you can come back to this notebook and download it again by running the following cell:

# +
from urllib.request import urlretrieve

urlretrieve('https://raw.githubusercontent.com/colbrydi/jupytercheck/master/answercheck.py', 
            'answercheck.py');
# -

# Verify you have ```answercheck``` installed by running the following cell

from answercheck import checkanswer
checkanswer("Check Answer",'bd8337cd5327e54b2b4b15c6ec3703ed');

# For more information about how ```answercheck``` works watch the following video:
#
# [Direct Link](https://youtu.be/d4a9Xag-yc8) to the Youtube video.

from IPython.display import YouTubeVideo
YouTubeVideo("d4a9Xag-yc8",width=640,height=320, cc_load_policy=True)

# **_NOTE_** make sure you do not change the ```checkanswer``` commands.  The long string with numbers and letters is the secret code that encodes the true answer.  This code is also called the HASH.  Feel free to look at the ```answercheck.py``` code and see if you can figure out how it works?  

# ---
# <a name="Math"></a>
# ## 2. Review of Python Math Package
#
# &#9989; **<font color=red>DO THIS:</font>**   Watch the following video about the python Math package.

# [Direct Link](https://youtu.be/PBlKeuzUf5g) to the Youtube video.

from IPython.display import YouTubeVideo
YouTubeVideo("PBlKeuzUf5g",width=640,height=320, cc_load_policy=True)

# &#9989; **<font color=red>DO THIS:</font>**    In the following cell, load the math package and run the ```hypot``` function with inputs (3,4).  

# +
#Put your answer here
# -

# &#9989; **<font color=red>QUESTION:</font>**    What does the ```hypot``` function do?

# Put your answer to the above question here.

# ----
# <a name="Numpy"></a>
#
# ## 3. Review of Python Numpy Package
#
# &#9989; **<font color=red>DO THIS:</font>**   Watch the following video about the python Numpy package.

# [Direct Link](https://youtu.be/_hbWtNgstlI) to the Youtube video.

from IPython.display import YouTubeVideo
YouTubeVideo("_hbWtNgstlI",width=640,height=320, cc_load_policy=True)

# The Python Numpy library has a ```matrix``` object which can be initialized as follows:

import numpy as np
A = np.matrix([[1,1], [20,25]])
b = np.matrix([[30],[690]])
print("A="+str(A))
print("b="+str(b))

# Python can solve equations in the $Ax=b$ format with the ```numpy.linalg``` library.  For example:

# +
import numpy as np

x = np.linalg.solve(A, b)
print("x="+str(x))
# -

# The ```numpy.linalg``` library is just a subset of the ```scipy.linalg``` library.  

# +
import scipy.linalg as la

x = la.solve(A, b)
print("X="+str(x))
# -

# &#9989; **<font color=red>DO THIS:</font>**     Convert the following system of linear equations to numpy matrices and solve it sing a Python linear algebra solver (Store the solutions in a vector named ```x```).
# $$ 18x+21y = 226$$
# $$ 72x-3y = 644$$

# +
##Put your answer to the above question here.

# +
from answercheck import checkanswer

checkanswer.vector(x,'756ca9fa3951fad0e623b2a8315d5fd7');
# -

# ----
# <a name="Indexing"></a>
# ## 4. Advanced Python Indexing
#
# This one is a little long and reviews some of the information from the last video. However, I really like using images as a way to talk about array and matrix indexing in ```Numpy```.

# [Direct Link](https://youtu.be/XSyiafkKerQ) to the Youtube video.

from IPython.display import YouTubeVideo
YouTubeVideo("XSyiafkKerQ",width=640,height=360, cc_load_policy=True)

# +
# %matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import imageio

#from urllib.request import urlopen, urlretrieve
#from scipy.misc import imsave

url = 'https://res.cloudinary.com/miles-extranet-dev/image/upload/ar_16:9,c_fill,w_1000,g_face,q_50/Michigan/migration_photos/G21696/G21696-msubeaumonttower01.jpg'
im = imageio.imread(url)

im[10,10,0] = 255
im[10,10,1] = 255
im[10,10,2] = 255

#Show the image
plt.imshow(im);
# -

im[20,20,:] = 255
plt.imshow(im)

cropped = im[0:50,0:50,:]
plt.imshow(cropped)

cropped = im[50:,350:610,:]
plt.imshow(cropped)

red = im[:,:,0]
plt.imshow(red)
plt.colorbar()

# +
#Note python changed slightly since the making of the video.  
# We added the astype funciton to ensure that values are between 0-255
red_only = np.zeros(im.shape).astype(int)
red_only[:,:,0] = red

plt.imshow(red_only)

# +
green_only = np.zeros(im.shape).astype(int)
green_only[:,:,1] = im[:,:,1]

plt.imshow(green_only)

# +
blue_only = np.zeros(im.shape).astype(int)
blue_only[:,:,2] = im[:,:,2]

plt.imshow(blue_only)
# -

# &#9989; **<font color=red>DO THIS:</font>**    Modify the following code to set all of the values in the blue channel to zero using only one simple line of indexing code. 
#

# +
no_blue = im.copy()
#####Start your code here #####

#####End of your code here#####  
plt.imshow(no_blue)
# -

# &#9989; **<font color=red>QUESTION:</font>**   What was the command you use to set all of the values of blue inside no_blue to zero?

# Put your answer to the above question here.

# ----
# <a name="Latex"></a>
#
# ## 5. LaTeX Math
#

# [Direct Link](https://youtu.be/qgSa7n_zQ3A) to the Youtube video.

from IPython.display import YouTubeVideo
YouTubeVideo("qgSa7n_zQ3A",width=640,height=320, cc_load_policy=True)

# Since this is a "Matrix Algebra" course, we need to learn how to do 'matrices' in LaTeX. Double click on the following cell to see the LaTeX code to build a matrix:
#

# Basic matrix notation:
#
# $$ 
# \left[
# \begin{matrix}
#     1   & 0 & 4  \\
#     0   & 2 & -2  \\
#     0   & 1 & 2 
# \end{matrix}
# \right] 
# $$
#
# Augmented matrix notation:
#
# $$ 
# \left[
# \begin{matrix}
#     1   & 0 & 4  \\
#     0   & 2 & -2  \\
#     0   & 1 & 2 
#  \end{matrix}
# ~  \middle\vert ~
# \begin{matrix}
# -10 \\ 3 \\ 1
# \end{matrix}
# \right] 
# $$

# &#9989; **<font color=red>DO THIS:</font>**    Using LaTeX, create an augmented matrix for the following system of equations:
#
# $$~4x + 2y -7z = 3~$$
# $$12x ~~~~~~~~+ ~z = 10$$
# $$-3x -~y + 2z = 30$$
#

# Put your LaTeX code here. (Hint: copy and paste from above)

# &#9989; **<font color=red>QUESTION:</font>**   In LaTeX, what special characters are used to separate elements inside a row?

# Put your answer to the above question here.

# ----

# Written by Dr. Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

# ----

#
#
