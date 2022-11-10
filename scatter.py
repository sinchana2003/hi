# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 04:00:46 2022

@author: SPTINT-09
"""

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-09/Downloads/tips.csv")
print(data.head(10))
plt.scatter(data['bill'],data['tip'])
plt.colorbar()
plt.title("scatter plot graph")
plt.xlabel('bill')
plt.ylabel('tip')
plt.show()