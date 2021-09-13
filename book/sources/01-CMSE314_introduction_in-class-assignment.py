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

# # 01 In-Class Assignment: Welcome to Matrix Algebra with computational applications

# What can you solve with $Ax=b$?
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Linear_subspaces_with_shading.svg/650px-Linear_subspaces_with_shading.svg.png" alt="Visual image of three planes intersecting. This is a common image used in linear algebra and will be explained in detail laater in the semester.  It is included here mostly as a visual anchor that can help students when they review their notes. ">
#
# Image from [http://wikipedia.org/](http://wikipedia.org/)
#

from IPython.display import YouTubeVideo
YouTubeVideo("-aiL8iWhQjc",width=640,height=360, cc_load_policy=True)

# ### Agenda for today's class (80 minutes)
#
#
# 1. [(10 minutes) Class Procedures](#Class_Procedures)
# 2. [(10 minutes) Introductions](#Introductions)
# 3. [(10 minutes) Example](#Example)
# 4. [(25 minutes) Syllabus, Schedule and other Procedures](#Syllabus_and_Schedule)
# 5. [(5 minutes) Download and review next pre-class assignment](#Download_and_review_next_pre-class_assignment)

# ---
# <a name="Class_Procedures"></a>
# ## 1. Class Procedures
#
# All in-class assignments are designed such that you can get started as soon as you show up in class. This is highly recommended.  See how far you can get on your own and then you will be ready when it is time for questions.   Here are the basic instructions.

# ### &#9989; Step 1 - Get out your laptop
# > Feel free to grab one of the laptops in the classroom if you do not have your own. 

# ### &#9989; Step 2 - Create a Course Assignment Folder in your home directory
#
#
# > **_HINT_** Store all notebooks in the same folder on your computer. They will work better that way.

# ### &#9989; Step 3 - Download this jupyter notebook
#
# > Download a copy of this notebook (ipynb file which tands for ipython notebook). 
#

# ### &#9989; Step 4 - Open this assignment in Jupyter
#
# > Open the downloaded file inside of jupyter either on your laptop or upload the file to an on-line server and open it there.  
#

# ---
# <a name="Introductions"></a>
# ## 2. Introductions
#
# This course appeals to students from many different backgrounds.  Let us use this time to go around the room and introduce ourselves to each other. 

# ---
# <a name="Example"></a>
# ## 3. Example:
#
# Suppose that we have three objects on a balanced beam. Also suppose we know that one has a mass of 2 kg, and we want to find the two unknown masses. Experimentation with a (assume weightless) meter stick produces these two balances. (diagram not to scale)
#  
# <img src="https://goo.gl/h2cqwE" align="center" width="70%" alt="Image showing two balanced beams, each with three weights. In the top beam is unknown weight A is a distance of 40 to the left of the fulcrum, unknown weight B is a distance of 15 to the left of the fulcrum and a weight of 2 is 50 to the right of the fulcrum. In the bottom beam is the same unknown weights.  Weight A is now a distance of 50 to the right of the fulcrum, weight B is a distance of 25 to the left of the fulcrum and the weight of 2 is a distance of 25 to the right of the fulcrum.">
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
# <img src="https://goo.gl/Rkn178" width="70%" alt="Image showing two balanced beams, each with four weights. In the top beam is unknown weight A which is a distance of 35 to the left of the fulcrum, unknown weight B is a distance of 21 to the left of the fulcrum, unknown weight C is a distance of 11 to the right of the fulcrum and a weight of 2 is 50 to the right of the fulcrum. In the bottom beam is the same unknown weights.  Weight A is now a distance of 10 to the right of the fulcrum, weight B is a distance of 24 to the right of the fulcrum, weight C is a distance of 25 to the left of the fulcrum and the weight of 2 is still at a distance of 50 to the right of the fulcrum.">
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

# ----
# <a name="Syllabus_and_Schedule"></a>
# ## 4. Syllabus, Schedule and other Procedures
# Let us now use the time to review the course Syllabus, schedule and other procedures.  

# ----
# <a name="Download_and_review_next_pre-class_assignment"></a>
# ##  5. Download and review next pre-class assignment
# I will try my best to post each weeks pre-class assignments before the weekend (hopefully on Thursday before class).  Note pre-class assignments are generally due at midnight the day before class.  To get credit for the pre-class assignment you will need to do the readings, answer the questions and submit your answers to the embeded google form.
#
# Here is next Pre-class assignments. 
#
# * [02--Vectors_pre-class-assignment.ipynb](02--Vectors_pre-class-assignment.ipynb)
#

# ----
#
# Written by Dr. Dirk Colbry, Michigan State University
#
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a>
#
# This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
