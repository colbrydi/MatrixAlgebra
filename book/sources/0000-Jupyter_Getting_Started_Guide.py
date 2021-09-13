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

# [Link to this document's Jupyter Notebook](0000-Jupyter_Getting_Started_Guide.ipynb)

# # Jupyter Getting Started Guide
#
# This guide is designed to help students new to Jupyter notebooks get started.   
#
# <img src="https://jupyter.org/assets/main-logo.svg" width="25%" alt="Jupyter software logo">
#
# > The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.
# From: <a href="https://jupyter.org/">https://jupyter.org/</a>
#
# Jupyter works best as a communication tool.  Notebooks will be used throughout this class as a way for instructors to communicate with students and for students to communicate with instructors. We will use Jupyter notebooks extensively for pre-class assignments, in-class assignments, homework and Exams.  

# ## Getting Jupyter Working
#
# The first thing you will need to do is to get Jupyter running.  There are two basic methods we will be using Jupyter in class. The first is to install it on your computer using Anaconda Python distribution and the second is to use the Web based [JupyterHub](http://jupyterhub.egr.msu.edu) server put together for the class. The following instructions can help you get started.  We recommend learning how to use both methods for class in case there is a problem on one of the systems. 
#
# ### Instructions for downloading Anaconda (Python 3.x.x):
#
# (These instructions are also available via YouTube video: https://youtu.be/3BiLPXAGINA)
#
# 1. Go to the Anaconda Download web page:  https://www.continuum.io/downloads
# 2. Use the “Jump to: Windows | OS X | Linux” to pick your operating system.
# 3. Download the Python 3.x version (64 bit recommended).
# 4. Follow the directions at the bottom of the page to install Python on your specific operating system.
# 5. Open the command line program on your computer
#
#     - On windows, type CMD in the run box in the Start menu.
#     - On Mac, type “terminal” and hit enter in the Finder window
#     - On Linux, open up the console application
#     
# 6. Type ```jupyter notebook``` in the command line and hit enter
#
# If everything goes correctly, a browser window should open up with the Jupyter interface running. If things do not work, do not worry; we will help you get started.
#
# ### Instructions for connecting to the engineering JupyterHub server:
#
# (These instructions are also available via a YouTube video)
#
#
#
# Every student enrolled in this class will be given an engineering computing account. If this is your first time using your Engineering account you will need to activate the account by going to the following website:
#
# https://www.egr.msu.edu/decs/myaccount/?page=activate
#
# Enter your MSU NetID. The initial password will be your APID with an @ on the end (example: A12345678@) and then they have to set a password that meets the requirements listed on the page. Verify the password. Then agree to the terms and Activate.
#
# - Once your account is activated you can access the classroom Jupyterhub server using the following instructions:
#     1. Open up a web browser and go to the following URL: https://jupyterhub.egr.msu.edu
#     2. Type your engineering login name. This will be your MSU NetID.
#     3. Your engineering password.
#
# If everything is working properly you will see the main “Files” windows in the Jupyter interface.
#
#
# ### Instructions for getting Jupyter notebook files into Jupyter:
#
# Once you have Jupyter running you will need a notebook file to try out. Jupyter notebooks (also referred to as iPython notebooks) are files that end with the .ipynb extension.  We will give you these files for all of your assignments, you will edit them and turn in the edited files in using the course website.
#
# You can download the ipynb assignment files from the course website (http://d2l.msu.edu). Once you have an ipynb file you can load it into Jupyter using the “upload” button on the main “Files” tab in the Jupyter web interface. Hitting this button will cause a file browser window to open. Just navigate to your ipynb file, select it and hit the open button.
#
# Once you see your filename in the jupyter window you can just click on that name to start using that file. 

# **&#9989; DO THIS:** This tutorial was originally written as a Jupyter notebook and saved to a pdf.  If you are reading this in a pdf, go to the course webpage and download the file titled "00-Getting-Started-Guide.ipynb" and run it in Jupyter before continuing on to the next section. 

# ## Example running python code in Jupyter Notebooks
#
# One of the most unique and defining features of Jupyter notebooks is the ability to run code inside of this notebook.  This ability makes Jupyter Notebooks especially useful in classes that teach or use programming concepts.  
#
# Jupyter notebooks are separated into different types of "cells".  The two major types of cells are; Markdown cells and code cells.  Markdown cells (such as this one) consist of formated text, images and equations much like your 
# favorite word processor.  
#
# The following are two code cells written in the Python programming language.  This simple code is a tool to make it easy to search your jupyter notebooks which can be handy if you are looking for something from a previous class. The example searches for an exact string in your notebook files in the current directory and displays links to the files as output. 
#
# To run the code, first select the code cell with your mouse and then hold down the "Shift" key while hitting the "enter" key.  You will have to hit the enter key twice to run both cells.

# +
#Search string
search_string = "rocket"

#Search current directory
directory ='.'

# +
from pathlib import Path
from IPython.core.display import display, HTML

search_string = search_string.lower()
links=[]

folder = Path(directory)

files = folder.glob('*.ipynb')
files = sorted(files)
for file in files:
    fn = str(file)
    with open(fn,'r', encoding='utf-8') as fp:
        for line in fp:
            line = line.lower()
            if search_string in line:
                links.append("<a href="+fn+" target=\"_blank\" >"+fn+"</a></br>")
                break
if links:
    display(HTML(' '.join(links)))
else:
    print('string ('+search_string+') not found.')
            
# -

# ## Video review of Python, IPython, and IPython notebooks
#
# Much of this course will be taught in a "flipped" style. This means we give you notebooks to review outside of class and we use in-class time to work on meaningful problems.  Many of our pre-class assignments notebooks use videos to help communicate ideas (in lieu of lecture time in class). 
#
# The following two cells will embed the lectures in the notebooks. Run the cells using the "Shift-Enter" key combination described above.  Once the video appears just click on the "Play" triangle. 
#
# These videos explain Python and Jupyter in more detail. 
#
# * Direct link to "**Python, iPython, Jupyter**" video: https://youtu.be/L03BzGmLUUE
# * Alternative Link: https://mediaspace.msu.edu/media/t/0_wxpceyi6

# The command below this comment actually displays a specific YouTube video,  
# with a given width and height.  You can watch the video in full-screen (much higher
# resolution) mode by clicking the little box in the bottom-right corner of the video.
from IPython.display import YouTubeVideo
YouTubeVideo("L03BzGmLUUE",width=640,height=360, cc_load_policy=True)

# * Direct link to "**Working with Jupyter and ipynb files**" video: https://youtu.be/5WSQnGmz3IA.  
# * Alternative Link: https://mediaspace.msu.edu/media/t/0_hkqjufix
#
# Note that the download URL in this video is a little out of date.  See the next video or google "Anaconda Python Download"
#

#Python code to display embeded video in jupyter notebook
from IPython.display import YouTubeVideo
YouTubeVideo("5WSQnGmz3IA",width=640,height=360, cc_load_policy=True)

# ## Installing Anaconda Python
# The following video will introduce you to install Anaconda Python on your personal computer. For this class, make sure you install the latest version (the version in the video is probably old). Also the websites may have been updated.  Hopefully that will not be confusing. 
#
# * Direct link to "**Install Anaconda**" video: https://youtu.be/3BiLPXAGINA
# * Alternative Link: 

#Python code to display embeded video in jupyter notebook
from IPython.display import YouTubeVideo
YouTubeVideo("3BiLPXAGINA",width=640,height=360, cc_load_policy=True)

# ## Introduction to the Engineering Jupyter Account
# The following video will introduce you to the Engineering JupyterHub Interface. Please watch this video and answer the questions. Log onto the engineering JupyterHub account using the following link: 
#
#  - http://jupyterhub.egr.msu.edu
#
# * Direct link to "**MSU Engineering Jupyterhub Server**" video: https://youtu.be/l7mhi4ww6tY
# * Alternative Link: https://mediaspace.msu.edu/media/t/0_brafne0e

#Python code to display embeded video in jupyter notebook
from IPython.display import YouTubeVideo
YouTubeVideo("l7mhi4ww6tY",width=640,height=360, cc_load_policy=True)

#
# ## More Information
#
# There are lots of resources on the web for using Python and Jupyter notebooks.  The following are some recommended websites for getting more information.  If these sites do not work consider using your favorite search engine.
#
# - https://software-carpentry.org/lessons/
# - https://docs.python.org/3/tutorial/
# - http://pythontutor.com/
#

# Written by Dirk Colbry, Michigan State University
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

#
#
