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
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

#

# ![Image of the planet Jupyter in infrared. Used as a motivation for this textbook](./Cover_horizontal.png)
#
# # Introduction
#
# Matrix Algebra with Computational Applications is a collection of Open Educational Resource (OER) materials designed to introduce students to the use of Linear Algebra to solve real world problems. These materials were developed specifically for students and instructors working in a "flipped classroom" model that emphasizes hands-on problem solving activities during class meetings, with students watching lectures and completing readings and assignments outside of the classroom.
# The materials are organized into a semester long course with "pre-class" and "in-class" assignments. The "pre-class" assignments include readings, video lectures and coding projects (in Python), which students are expected to complete before attending class. The in-class assignments consist of hands-on individual and group activities intended to be completed during class. These in-class activities are supervised by the instructors, who actively answer questions and help guide the students in achieving the learning goals for the course.
#
# To be successful in this course, students need to have strong Python programming skills. Students will leverage these coding skills to write programs that use Linear Algebra to solve science and engineering problems. Although it is important for students to understand the mathematical concepts behind the materials, this course is not intended to teach students how to do mathematical proofs.
#
# These Open Educational Resources (OER) were developed as part of a restructuring of the Michigan State University Matrix Algebra Course (MTH314) in Fall Semester of 2017. All of the OER materials are provided as Jupyter notebooks, which are open source tools that integrate multiple resources (websites, word processors, LaTeX, math, and programming) into a digital “notebook.”
#
# Instructors interested in using these materials are encouraged to reach out to Dr. Dirk Colbry (colbrydi@msu.edu) in advance to gain access to additional materials and examples designed to support teaching and student evaluation.
#
# ## About the Lead Author
#
# Dr. Dirk Colbry is faculty member in the Department of Computational Mathematics, Science and Engineering (CMSE) at Michigan State University (MSU). Dr. Colbry has decades of experience in curriculum development and teaching across a wide range of subjects, including:  numerical linear algebra, parallel programming, microprocessors, artificial intelligence, scientific image analysis, compilers, GPU programming, next generation architectures, tools for computational modeling, algorithm analysis, and professional skills for scientists and engineers.
#
# In addition to teaching and curriculum development, Dr. Colbry is an expert in computer vision and scientific image understanding, and has collaborated on research in fields as diverse as Engineering, Toxicology, Plant and Soil Sciences, Zoology, Mathematics, Statistics, and Biology. Recent projects include research in Image Phenomics; developing a commercially-viable large scale, cloud based image pathology tool; and helping develop methods for measuring the carbon stored inside of soil. In addition to his primary research focus in Scientific Image Understanding and Machine Learning, Dr. Colbry also researches computational education and high-performance computing (HPC). Prior to joining CMSE, Dr. Colbry worked for the MSU Institute for Cyber-Enabled Research (iCER) as a computational consultant and Director of the High Performance Computing Center (HPCC).

# ## Acknowledgments
#
# This textbook is a product of the [Michigan State University Libraries' Open Educational Resource (OER) program](https://openbooks.lib.msu.edu/) led by Regina Gong, OER and Student Success Librarian. The content of this book is a work in progress, with contributions and collaboration from the MTH314 instructors listed below. Individual contributions range from co-authoring specific Jupyter notebooks to testing and providing feedback of the materials.
#
# ### Lead Instructors
# * Dr. Dirk Colbry
# * Dr. Ming Yan 
# * Dr. Matthew Mills 
# * Dr. Paul Speaker 
# * Dr. Zhichao Peng 
# * Dr. Sulin Wang 
# * Dr. Rongrong Wang
#
# ### Graduate Teaching Assistance
# * Shuyang Qin 
# * Cullen Avery Haselby
# * Haoyang Chen
# * Kai Huang  
# * Nathan Brugnone 
# * Yao Li 
# * Thomas Chuna 
#
# ### Undergraduate Learning Assistance
# * Amanda Bowerman 
# * Zachary Matson 
# * Noah Jankowski 
# * Nicholas Mouaikel 
# * Marv Zurek 
# * Ishaan Pathak 
# * Sam Tracht 
# * Dave Yonkers 
# * Heather Noonan 
# * Drew Pype 

# ### Cover Art
#
# Special thanks to Sri Pallay from the MSU Library for developing the cover art, and to Julie Taylor for assistance with branding. The cover is a composite image, derived from data collected by the Jovian Infrared Auroral Mapper (JIRAM) instrument aboard NASA's Juno mission to Jupiter. The image shows the central cyclone at Jupiter's north pole and the eight cyclones that encircle it (NASA).
#
# ![Full Size cover Image](./Cover.jpg)

# Written by Dr. Dirk Colbry, Michigan State University
#
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

# ---

#
#
