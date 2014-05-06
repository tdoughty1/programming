# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 09:24:59 2014

@author: tdoughty1
"""

from pandas import DataFrame, HDFStore
from numpy import random, zeros
from Dataset import Create_Dataset

from Tree import DecisionTree

bdt = DecisionTree()

newData = True

store = HDFStore('datafile.h5')
store.open()

if newData:
    tempdata = Create_Dataset()
    rArray = random.rand(len(tempdata))

    df = DataFrame()
    df['x'] = tempdata[:, 0]
    df['y'] = tempdata[:, 1]
    df['Sig'] = tempdata[:, 2] == 1
    df['Bgd'] = tempdata[:, 2] == 0
    df['Train'] = rArray >= .5
    df['Test'] = rArray < .5
    store['Data'] = df
else:
    df = store['Data']

store.close()

df['w0'] = zeros(len(df))
df['w0'][df['Train']] = 1./len(df[df['Train']])

print "Training Events = ", len(df[df['Train']])
print "Training Signal Events = ", len(df[df['Train'] & df['Sig']])
print "Training Background Events = ", len(df[df['Train'] & df['Bgd']])

print "Testing Events = ", len(df[df['Test']])
print "Testing Signal Events = ", len(df[df['Test'] & df['Sig']])
print "Testing Background Events = ", len(df[df['Test'] & df['Bgd']])

bdt.Train(df)
bdt.Score()
bdt.PrintScore()

bdt.Prune(5)
bdt.Score()
bdt.PrintScore()
