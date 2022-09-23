#!/usr/bin/env python
# coding: utf-8

# ### Numpy Exercises
# 
# In your numpy-pandas-visualization-exercises repo, create a file named numpy_exercises.py for this exercise.
# 
# Use the following code for the questions below:

# In[12]:


import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# 1. How many negative numbers are there?

# In[2]:


print(a[a < 0])
a[a < 0].size


# 2. How many positive numbers are there?

# In[3]:


print(a[a > 0])
a[a > 0].size


# 3. How many even positive numbers are there?

# In[4]:


a_even = a[a % 2 == 0]
print(a_even[a_even > 0])
a_even[a_even > 0].size


# 4. If you were to add 3 to each data point, how many positive numbers would there be?

# In[5]:


add_three = a + 3
print(add_three[add_three >0])
add_three[add_three >0].size


# 5. If you squared each number, what would the new mean and standard deviation be?

# In[6]:


a_sq = a ** 2
print(a)
print(a_sq)
print()
print(f'The mean of the array squared is: {a_sq.mean()}')
print(f'The standard deviation of the array squared is: {a_sq.std()}')


# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link (https://ds.codeup.com/python/intro-to-numpy/#:~:text=data%20set.%20See-,this%20link,-for%20more%20on) for more on centering.

# In[7]:


mean = a.mean()
center = a - mean
center


# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
# 
#     Z = x-μ / σ  
#     where: 
# X is a single raw data value
# μ is the population mean
# σ is the population standard deviation

# In[8]:


import scipy.stats as stats

stats.zscore(a)


# In[10]:


std = a.std()
z_score = (a-mean)/std
z_score


# 8. Copy the setup and exercise directions from More Numpy Practice (https://gist.github.com/ryanorsinger/c4cf5a64ec33c014ff2e56951bc8a42d) into your numpy_exercises.py and add your solutions.

# ## Setup 1

# In[20]:


a2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[21]:


type(a2)


#  ### Use python's built in functionality/operators to determine the following:
#  Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

# In[23]:


sum_of_a2 = sum(a2)
sum_of_a2


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

# In[26]:


min_of_a2 = min(a2)
min_of_a2


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

# In[27]:


max_of_a2 = max(a2)
max_of_a2


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

# In[35]:


import statistics
mean_of_a2 = statistics.mean(a2)
mean_of_a2


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# In[40]:


array_a2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
product_of_a2 = array_a2.prod()
product_of_a2


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

# In[44]:


squares_of_a2 = array_a2 ** 2
squares_of_a2


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

# In[53]:


odds_in_a2 = array_a2 % 2 == 1
print(array_a2)
print(odds_in_a2)
print(array_a2[odds_in_a2])


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

# In[55]:


evens_in_a2 = array_a2 % 2 == 0
print(array_a2[evens_in_a2])


# ## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
# 
# ## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.

# In[57]:


b = [
    [3, 4, 5],
    [6, 7, 8]
]

b


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable.
# ```python
# sum_of_b = 0 for row in b: sum_of_b += sum(row)
# ```
# 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**

# In[67]:


b = np.array(b)

sum_of_b = b.sum()
sum_of_b


# Exercise 2 - refactor the following to use numpy.
# ```python
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
# ```

# In[64]:


min_of_b = b.min()
min_of_b


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# ```python
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
# ```

# In[65]:


max_of_b = b.max()
max_of_b


# Exercise 4 - refactor the following using numpy to find the mean of b
# ```python
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
# ```

# In[66]:


mean_of_b = b.mean()
mean_of_b


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# ```python
# product_of_b = 1 for row in b: for number in row: product_of_b *= number
# ```

# In[68]:


product_of_b = b.prod()
product_of_b


# Exercise 6 - refactor the following to use numpy to find the list of squares 
# ```python
# squares_of_b = [] for row in b: for number in row: squares_of_b.append(number**2)
# ```

# In[69]:


squares_of_b = b ** 2
squares_of_b


# # Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)
# 
# 
# # Exercise 8 - refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)
# 
# # Exercise 9 - print out the shape of the array b.
# 
# # Exercise 10 - transpose the array b.
# 
# # Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
# 
# # Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
# 
# ## Setup 3
# c = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# 
# # HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# # Exercise 1 - Find the min, max, sum, and product of c.
# 
# # Exercise 2 - Determine the standard deviation of c.
# 
# # Exercise 3 - Determine the variance of c.
# 
# # Exercise 4 - Print out the shape of the array c
# 
# # Exercise 5 - Transpose c and print out transposed result.
# 
# # Exercise 6 - Get the dot product of the array c with c. 
# 
# # Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
# 
# # Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
# 
# 
# ## Setup 4
# d = [
#     [90, 30, 45, 0, 120, 180],
#     [45, -90, -30, 270, 90, 0],
#     [60, 45, -45, 90, -45, 180]
# ]
# 
# # Exercise 1 - Find the sine of all the numbers in d
# 
# # Exercise 2 - Find the cosine of all the numbers in d
# 
# # Exercise 3 - Find the tangent of all the numbers in d
# 
# # Exercise 4 - Find all the negative numbers in d
# 
# # Exercise 5 - Find all the positive numbers in d
# 
# # Exercise 6 - Return an array of only the unique numbers in d.
# 
# # Exercise 7 - Determine how many unique numbers there are in d.
# 
# # Exercise 8 - Print out the shape of d.
# 
# # Exercise 9 - Transpose and then print out the shape of d.
# 
# # Exercise 10 - Reshape d into an array of 9 x 2

# ### Awesome Bonus 
# For much more practice with numpy, Go to https://github.com/rougier/numpy-100 and clone the repo down to your laptop. To clone a repository: - Copy the SSH address of the repository - cd ~/codeup-data-science - Then type git clone git@github.com:rougier/numpy-100.git - Now do cd numpy-100 on your terminal. - Type git remote remove origin, so you won't accidentally try to push your work to Rougier's repo.
# 
# Congratulations! You have cloned Rougier's 100 numpy exercises to your computer. Now you need to make a new, blank, repository on GitHub.
# 
# Go to https://github.com/new to make a new repo. Name it numpy-100.
# DO NOT check any check boxes. We need a blank, empty repo.
# Finally, follow the directions to "push an existing repository from the command line" so that you can push up your changes to your own account.
# 
# Now do work, add it, commit it, and push it!
