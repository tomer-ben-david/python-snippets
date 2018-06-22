#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 20:45:58 2018

@author: tomer.bendavid
"""

import os

import pandas as pd
import io
import requests


from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

import scipy
print('scipy: %s' % scipy.__version__)

mystr: str = "555"

conf = SparkConf().setMaster("local").setAppName("WordCount")

sc = SparkContext(conf = conf)

spark = SparkSession.builder.appName('someapp').master("local[*]").getOrCreate()

url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
dataFromURL = requests.get(url).content
# c: pd.DataFrame =pd.read_csv(io.StringIO(s.decode('utf-8')))

import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv')

print(dataFromURL)

for row in dataFromURL.split('\r'):
    print(row)

ds = sc.createDataFrame([for line in dataFromURL.iter_lines()])

ds.collect()