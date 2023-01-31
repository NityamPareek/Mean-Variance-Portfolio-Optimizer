#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from nsepy import get_history
from datetime import date
from dateutil.relativedelta import relativedelta


# In[3]:


def get_data():

    symbols = []
    
    with open("stocks.txt", mode = "r") as ip:
        for stock in ip:
            symbols.append(stock.strip())

    ip.close()

    end = date.today()
    start = end - relativedelta(years=3)
    df = pd.DataFrame()

    for symbol in symbols:
    
        data = get_history(symbol = symbol, start = start, end = end)
        df = pd.concat([df, data], axis = 0)

    number_of_symbols = len(symbols)
    
    return df, symbols,number_of_symbols


# In[ ]:




