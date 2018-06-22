#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:14:44 2018

@author: tomer.bendavid
"""
import os

import pandas as pd

###############################
## Pandas wide print options ##
###############################

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


import io
import requests


from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

import scipy
print('scipy: %s' % scipy.__version__)

import matplotlib
print('matplotlib: %s' % matplotlib.__version__)

# scikit-learn
import sklearn
print('sklearn: %s' % sklearn.__version__)

import matplotlib.pyplot as plt
import numpy

mystr: str = "555"

conf = SparkConf().setMaster("local").setAppName("WordCount")

sc = SparkContext(conf = conf)

spark = SparkSession.builder.appName('someapp').master("local[*]").getOrCreate()

url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
dataFromURL = requests.get(url).content
# c: pd.DataFrame =pd.read_csv(io.StringIO(s.decode('utf-8')))

data = pd.read_csv('https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv')

print(dataFromURL)

############
## Plots ###
############

# basic line plot
myarray = numpy.array([1, 2, 3])
plt.plot(myarray)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()

# basic scatter plot
import matplotlib.pyplot as plt
import numpy
x = numpy.array([1, 2, 3])
y = numpy.array([2, 4, 6])
plt.scatter(x,y)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()

###################
## Data Analysis ##
###################

url="https://gist.githubusercontent.com/ktisha/c21e73a1bd1700294ef790c56c8aec1f/raw/819b69b5736821ccee93d05b51de0510bea00294/pima-indians-diabetes.csv"
s=requests.get(url).content

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data=pd.read_csv(io.StringIO(s.decode('utf-8')), names = names)
peek = data.head(20)

print(peek)

