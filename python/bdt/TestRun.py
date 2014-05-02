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

nEvent = 40
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

print df

print "Training Events = ", len(df[df['Train']])
print "Training Signal Events = ", len(df[df['Train'] & df['Sig']])
print "Training Background Events = ", len(df[df['Train'] & df['Bgd']])

print "Testing Events = ", len(df[df['Train']])
print "Testing Signal Events = ", len(df[df['Test'] & df['Sig']])
print "Testing Background Events = ", len(df[df['Test'] & df['Bgd']])

bdt.Train(df)
bdt.Score()
bdt.PrintScore()

bdt.Prune()

bdt.Score()
bdt.PrintScore()