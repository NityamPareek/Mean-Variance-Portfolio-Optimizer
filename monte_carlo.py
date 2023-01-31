#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


def monte_carlo_sim(price_df, number_of_symbols):
    
    log_return = np.log(1 + price_df.pct_change())

    num_of_portfolios = 10000

    all_weights = np.zeros((num_of_portfolios, number_of_symbols))

    ret_arr = np.zeros(num_of_portfolios)

    vol_arr = np.zeros(num_of_portfolios)

    sharpe_arr = np.zeros(num_of_portfolios)

    for ind in range(num_of_portfolios):

        weights = np.array(np.random.random(number_of_symbols))
        weights = weights / np.sum(weights)

        all_weights[ind, :] = weights

        ret_arr[ind] = np.sum((log_return.mean() * weights) * 252)

        vol_arr[ind] = np.sqrt(
            np.dot(weights.T, np.dot(log_return.cov() * 252, weights))
        )

        sharpe_arr[ind] = (ret_arr[ind] - 0.06751)/vol_arr[ind]

    simulations_data = [ret_arr, vol_arr, sharpe_arr, all_weights]

    simulations_df = pd.DataFrame(data=simulations_data).T

    simulations_df.columns = [
        'Returns',
        'Volatility',
        'Sharpe Ratio',
        'Portfolio Weights'
    ]

    simulations_df = simulations_df.infer_objects()
    
    return simulations_df


# In[ ]:




