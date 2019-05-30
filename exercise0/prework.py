#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Jacqueline Xu
iXperience
23 May 2019
Pre-Work
'''

'''
“Git Can Facilitate Greater Reproducibility And Increased Transparency in Science”

As replicable data is important in all scientific research, software engineering
is no different. In the fast-paced innovative world that we live in, it is
essential that research is reproducible in order to allow existing data to be
validated/refuted or built upon. In computer science, version control does exactly
this by saving previous versions of the code with comments known as commit messages.
As one such Version Control System, Git manages research artifacts such as data,
code, and documents. With this, software engineers leave a trail when they code,
and can therefore see the changes they’ve made over time, as well as revert to
previous versions. 
'''

#%%
'''
Problem 1: Basic Operations

You are at McDonalds and you loved it so much you wanna leave a tip.
Write a function that takes the amount owed and calculates
how much money you pay with an 18% tip.
'''

def calculate_tip(amount):
	return amount * 0.18

#%%
'''
Problem 2: Lists

I have a fortune cookie that says my lucky numbers are:

       [23, 54, 6, 8, 10078, 3]

Write a function that returns 3 lists
   - replace the number 6 with 1
   - the above list in decreasing order
   - all values greater than 15
'''

def replace_6(L):
	return [1 if x==6 else x for x in L]

def decreasing_order(L):
	K = sorted(L, reverse = True)
	return K

def greater_15(L):
	return [i for i in L if i > 15]

#%%
'''
Problem 3: Packages 

You are now getting ready to code some real data science. Write a 
statement that loads the numpy library into the interpreter and gives it an alias of `np`.
'''

import numpy as np

#%%
'''
Problem 4: Numpy

Take a randomly generated numpy array and slice the array to
get the 2nd and 3rd column. Then return the average of that column
using numpy
'''

def numpy_slice(A):
	a = A[:, 2:4]
	return np.mean(a, axis=0)
