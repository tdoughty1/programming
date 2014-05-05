# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 09:24:59 2014

@author: tdoughty1
"""

from pandas import DataFrame
from numpy import random
from Dataset import Create_Dataset

from Tree import DecisionTree

bdt = DecisionTree()

tempdata = Create_Dataset()
rArray = random.rand(len(tempdata))

df = DataFrame()
df['x'] = tempdata[:, 0]
df['y'] = tempdata[:, 1]
df['Sig'] = tempdata[:, 2] == 1
df['Bgd'] = tempdata[:, 2] == 0
df['Train'] = rArray >= .5
df['Test'] = rArray < .5

print "Training Events = ", len(df[df['Train']])
print "Training Signal Events = ", len(df[df['Train'] & df['Sig']])
print "Training Background Events = ", len(df[df['Train'] & df['Bgd']])

print "Testing Events = ", len(df[df['Test']])
print "Testing Signal Events = ", len(df[df['Test'] & df['Sig']])
print "Testing Background Events = ", len(df[df['Test'] & df['Bgd']])

bdt.Train(df, plot=True, animate=True)
bdt.Score()
bdt.PrintScore()

bdt.Prune(2.5)
bdt.Score()
bdt.PrintScore()
