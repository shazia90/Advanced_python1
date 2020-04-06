#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np


# In[2]:


array_of_zeros = np.zeros((3,4)) #3 rows & 4 columns

array_of_zeros # internal implementations will be off float.


# In[4]:


array_of_ones = np.ones((3,4))

array_of_ones


# In[ ]:


req: how to eliminate this . and get only int.
    
    


# In[5]:


array_of_ones_int = np.ones((3,4), dtype = np.int16)

array_of_ones_int


# In[7]:


array_empty = np.empty((2,3))

array_empty


# In[ ]:





# In[8]:


array_eye = np.eye(3)

array_eye


# In[ ]:





# In[ ]:


my req is to print even numbers from 1 to 20


# In[14]:


e = list(range(2,20,2))

print(e)


# In[ ]:





# In[19]:


array_of_evens = np.arange(2,20,2)

array_of_evens


# In[ ]:





# In[21]:


array_of_floats = np.arange(0,2,0.3)

array_of_floats


# In[ ]:





# In[ ]:


understanding two dimensional arrays


# In[22]:


array_2d = np.array([(2,4,6),(1,3,5)])

array_2d


# In[ ]:





# In[23]:


array_2d.shape #2d matrix 


# In[ ]:





# In[24]:


np.arange(6)


# In[25]:


array_nd = np.arange(6).reshape(3,2) #3rows, 2columns

array_nd


# In[27]:


array_nd = np.arange(6).reshape(4,1)

array_nd


# In[ ]:





# In[ ]:





# In[ ]:




