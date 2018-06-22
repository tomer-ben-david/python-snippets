#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:56:10 2018

@author: tomer.bendavid
"""

import pandas

# https://www.kaggle.com/bittlingmayer/amazonreviews
names = ['score', 'summary', 'detailed']
dataset = pandas.read_csv(
        filepath_or_buffer = '/Users/tomer.bendavid/Downloads/amazon_review_full_csv/train.csv',
        names = names,
        quotechar='"')

pandas.set_option('expand_frame_repr', False) # otherwise will break into newlines according to screen width.
dataset.head()
dataset.shape
dataset.dtypes