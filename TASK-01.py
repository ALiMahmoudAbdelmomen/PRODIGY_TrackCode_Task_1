#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


# In[8]:


df = pd.read_csv("E:\API_SP.POP.TOTL_DS2_en_csv_v2_84031\Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_84031.csv")


# In[9]:


df.head()


# In[10]:


df.info()


# In[12]:


df.shape


# In[13]:


df.describe()


# In[14]:


df.isnull().sum()


# In[ ]:





# In[ ]:





# In[11]:


gender_counts = df ['Region'].value_counts()

bar_width = 0.9

x=range(len(gender_counts.index))

plt.bar(gender_counts.index, gender_counts.values)

plt.xlabel('Region')

plt.ylabel('Count')

plt.title('Distribution of Region')

plt.xticks(x,gender_counts.index, rotation=45)

plt.tight_layout()

plt.show()


# In[ ]:





# In[ ]:




