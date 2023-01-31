#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


def clean_df(df):
    
    price_df = df[['Symbol', 'Close']]

    price_df = price_df.pivot(
        columns='Symbol',
        values='Close'
    )
    
    return price_df


# In[ ]:




