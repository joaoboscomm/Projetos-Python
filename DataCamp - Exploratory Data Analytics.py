
# coding: utf-8

# In[4]:


from sklearn import datasets


# In[5]:


import pandas as pd


# In[6]:


import numpy as np


# In[7]:


import matplotlib.pyplot as plt


# In[8]:


plt.style.use('ggplot')


# In[9]:


iris = datasets.load_iris()


# In[10]:


type(iris)


# In[11]:


print(iris.keys())


# In[12]:


type(iris.data), type(iris.target)


# In[13]:


iris.data.shape #150 linhas e 4 colunas, sendo examples em row e features em col


# In[14]:


iris.target_names


# In[18]:


X = iris.data


# In[19]:


y = iris.target


# In[20]:


df = pd.DataFrame(X, columns= iris.feature_names)


# In[21]:


print (df.head())#show 1st 5 rows


# In[22]:


_ = pd.scatter_matrix(df, c = y, figsize = [8,8], s=150, marker = 'D')

