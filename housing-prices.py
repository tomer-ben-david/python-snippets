#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 09:09:52 2018

@author: tomer.bendavid
"""

#%% show head
# Loading the libraries
from typing import Any, Union

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10.0, 8.0)
import seaborn as sns
from scipy import stats
from scipy.stats import norm

import requests

from io import StringIO

# Load data.
train_data: StringIO = StringIO(requests.get('https://raw.githubusercontent.com/tiwari91/Housing-Prices/master/train.csv').text)
train: pd.DataFrame = pd.read_csv(train_data)

test_data: StringIO = StringIO(requests.get('https://raw.githubusercontent.com/tiwari91/Housing-Prices/master/test.csv').text)
testDF: pd.DataFrame = pd.read_csv(test_data)

train.head()
testDF.head()

print(f'The train data has {train.shape[0]} rows and {train.shape[1]} rows')
print(f'The test data has {testDF.shape[0]} rows and {testDF.shape[1]} rows')

train.info() # alternatively to printing you can also get shape information with info.

print('\n## Checking for missing values... ')
train.columns[train.isnull().any()]

print('\n## Percentage of missing values in these columns... ')
missedPerColumn = train.isnull().sum()/len(train) # Table True/False if cell is null / rows length.
miss = missedPerColumn[missedPerColumn > 0] ## Filter only items that have miss > 0
miss.sort_values(inplace=True)
miss

print('\n## Visualize missing values')
miss = miss.to_frame() # Was probably not a dataframe.
miss.columns = ['count'] # I think adding count column.
miss.index.names = ['Name']
miss['Name'] = miss.index

# miss.plot()
#
sns.set(style='whitegrid', color_codes=True)
sns.barplot(x = "Name", y = "count", data=miss)

plt.xticks(rotation = 90) # labels should be vertical otherwise we don't see them.
plt.show()  # Showing a bar plot based on sns configuration.


print('\n## Plot target variable - the price')
sns.distplot(train['SalePrice'])
plt.show()
#%% show head
