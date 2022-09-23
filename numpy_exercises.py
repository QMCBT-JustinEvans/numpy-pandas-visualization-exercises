#!/usr/bin/env python
# coding: utf-8

# ### Numpy Exercises
# 
# In your numpy-pandas-visualization-exercises repo, create a file named numpy_exercises.py for this exercise.
# 
# Use the following code for the questions below:

# In[2]:


import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# 1. How many negative numbers are there?

# In[18]:


print(a[a < 0])
a[a < 0].size


# 2. How many positive numbers are there?

# In[17]:


print(a[a > 0])
a[a > 0].size


# 3. How many even positive numbers are there?

# In[75]:


a_even = a[a % 2 == 0]
print(a_even[a_even > 0])
a_even[a_even > 0].size


# 4. If you were to add 3 to each data point, how many positive numbers would there be?

# In[69]:


add_three = a + 3
print(add_three[add_three >0])
add_three[add_three >0].size


# 5. If you squared each number, what would the new mean and standard deviation be?

# In[86]:


a_sq = a ** 2
print(a)
print(a_sq)
print()
print(f'The mean of the array squared is: {a_sq.mean()}')
print(f'The standard deviation of the array squared is: {a_sq.std()}')


# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link (https://ds.codeup.com/python/intro-to-numpy/#:~:text=data%20set.%20See-,this%20link,-for%20more%20on) for more on centering.

# In[98]:


mean = a.mean()
center = a - mean
center


# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
# 
#     Z = x-μ / σ

# In[ ]:





# 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

# In[ ]:





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
