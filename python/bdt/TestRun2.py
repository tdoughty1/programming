# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 09:24:59 2014

@author: tdoughty1
"""

from pandas import DataFrame
from numpy import random
from sklearn.datasets import make_classification

from Tree import DecisionTree

bdt = DecisionTree()

nEvent = 100
nClass = 4

varNames = []

for i in range(nClass):
    varNames.append('var' + str(i+1))

tempdata = make_classification(nEvent, nClass)

df = DataFrame(tempdata[0])
df.columns = varNames
df['Rand'] = random.rand(len(df))
df['Sig'] = tempdata[1] == 1
df['Bgd'] = tempdata[1] == 0
df['Train'] = df['Rand'] >= .5
df['Test'] = df['Rand'] < .5

tempdata = make_classification(nEvent, nClass)

bdt.Train(df, animate=True, plot=True)
