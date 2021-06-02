# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 17:35:09 2021

@author: Takai
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Read input data
train=pd.read_csv("../input/house-prices-advanced-regression-techniques/train.csv")
test=pd.read_csv("../input/house-prices-advanced-regression-techniques/test.csv")
df = pd.concat([train, test], sort=False)
print(len(train),len(test),len(df))
df.info()

#divide dataset into two parts(categorical, contineous)
categorical, numerical = [],[]
for z in df.columns:
    t = df.dtypes[z]
    if t=='object':
        categorical.append(z)
    else:
        numerical.append(z)
print("CategoricaL:\n{}".format(categorical))
print("\nNumericaL:\n{}".format(numerical))

import seaborn as sns
import matplotlib.pyplot as plt

df_corr = df.corr()
sns.heatmap(df_corr, vmax=1, vmin=-1, center=0)