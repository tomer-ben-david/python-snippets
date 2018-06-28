#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:37:20 2018

@author: tomer.bendavid
"""

# logfile

##############################
####### Parse Log File #######
##############################

import urllib.request
url = "http://www.cs.tufts.edu/comp/116/access.log"
accesslog =  urllib.request.urlopen(url).read().decode('utf-8')
print("accesslog: " + accesslog)


# import nltk

# nltk.download()

from nltk.book import text1
from nltk import FreqDist

text1.concordance("monstrous") # find all occurrences

text1.similar("monstrous")

text1.dispersion_plot(["citizens", "democracy"]) # location of words in text.

len(text1) # len in words / tokens.

sorted(set(text1))

len(set(text1)) / len(text1) # lexical richness.

text1.count("sun")

text1[122] # word 122 -> ignorance

text1.index('ignorance') # first index of word. -> 122

text1[122:130] # ['ignorance', ',', 'the', 'letter', 'H', ',', 'which', 'almost']

text1[:3] # ['[', 'Moby', 'Dick']

greekName = 'oedipus' # it's a string
greekName[2:] # 'diphus'

## Simple Statistics

sorted(FreqDist(text1))[0:5] # ['!', '!"', '!"--', "!'", '!\'"']
FreqDist(text1).most_common(5) # [(',', 18713), ('the', 13721), ('.', 6862), ('of', 6536), ('and', 6024)]

FreqDist(text1).plot(50, cumulative=True) # log plot!

FreqDist(text1).hapaxes() # words that appear only once - hapaxes - 'commonalty', 'police', ...

text1.count()

###################################
#### Panda sklearn matplotlib #####
###################################
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Python version

import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names) #name is the above name for columns.

# shape
print(dataset.shape)

# head
print(dataset.head(20))

# descriptions
print(dataset.describe())

# class distribution
print(dataset.groupby('class').size())

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# histograms
dataset.hist()
plt.show()

# scatter plot matrix
scatter_matrix(dataset)
plt.show()