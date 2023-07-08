#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date
from dateutil.relativedelta import relativedelta

from get_data import get_data
from monte_carlo import monte_carlo_sim

pd.set_option('display.max_colwidth', None)
pd.set_option('expand_frame_repr', False)


# In[2]:


print("="*80)
print("Mean-Variance Portfolio Optimizer")
print("="*80)
print("\nNSE Code of Stocks in your portfolio must be entered in the file named 'stocks.txt'")
print("Number of years of historical data considered is 3")
print("\n\nLoading data...\n\n")

# In[3]:


df, symbols,number_of_symbols = get_data()
print("\n\nUsing monte carlo simulations to compute optimal portfolio...\n\n")
results = monte_carlo_sim(df_clean, number_of_symbols)


# In[4]:


max_sharpe_ratio = results.loc[results['Sharpe Ratio'].idxmax()]
min_volatility = results.loc[results['Volatility'].idxmin()]

optimal_data = [max_sharpe_ratio, min_volatility]
optimal_data_df = pd.DataFrame(data = optimal_data)

optimal_data_df.columns = [
    'Returns',
    'Volatility',
    'Sharpe Ratio',
    'Portfolio Weights'
]

optimal_data_df.reset_index(drop = True, inplace = True)


# In[5]:


print("-"*80)
print(f"1. For optimal market portfolio:\n\nReturns are {optimal_data_df.Returns[0]*100: .2f}%\nVolatility is {optimal_data_df.Volatility[0]*100: .2f}%\n")
print("-"*80)
print("Invest your money in the following ratios:\n")
for i in range(number_of_symbols):
    print(f"{symbols[i]}: {optimal_data_df['Portfolio Weights'][0][i]*100: .3f}%")

print("-"*80)    
print(f"\n2. For least risk market portfolio:\n\nReturns are {optimal_data_df.Returns[1]*100: .2f}%\nVolatility is {optimal_data_df.Volatility[1]*100: .2f}%\n")
print("-"*80)
print("Invest your money in the following ratios:\n")
for i in range(number_of_symbols):
    print(f"{symbols[i]}: {optimal_data_df['Portfolio Weights'][1][i]*100: .3f}%")

