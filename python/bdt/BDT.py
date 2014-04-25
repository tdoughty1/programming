# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 19:58:28 2014

@author: tdoughty1
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification


class Tree(object):

    def __init__(self, data, class_data):

        self.left = None
        self.right = None
        self.data = data
        self.class_data = class_data

        self._nSig = sum(class_data == 1)
        self._nBgd = sum(class_data == 0)

nEvent = 10000
nClass = 4

tempdata = make_classification(nEvent, nClass)

classify = tempdata[1]

data = {}

for i in range(nClass):

    tempArray = []

    for j in range(nEvent):
        tempArray.append(tempdata[0][j][i])

    key = 'var' + str(i+1)
    tempArray = np.array(tempArray)
    data[key] = tempArray

cSig = classify == 1
cBgd = classify == 0

plt.plot(data['var1'][cSig], data['var2'][cSig], 'r.', label='Signal')
plt.plot(data['var1'][cBgd], data['var2'][cBgd], 'b.', label='Background')
plt.xlabel('var1')
plt.ylabel('var2')
plt.show()

plt.plot(data['var1'][cSig], data['var3'][cSig], 'r.', label='Signal')
plt.plot(data['var1'][cBgd], data['var3'][cBgd], 'b.', label='Background')
plt.xlabel('var1')
plt.ylabel('var3')
plt.show()

plt.plot(data['var1'][cSig], data['var4'][cSig], 'r.', label='Signal')
plt.plot(data['var1'][cBgd], data['var4'][cBgd], 'b.', label='Background')
plt.xlabel('var1')
plt.ylabel('var4')
plt.show()

plt.plot(data['var2'][cSig], data['var3'][cSig], 'r.', label='Signal')
plt.plot(data['var2'][cBgd], data['var3'][cBgd], 'b.', label='Background')
plt.xlabel('var2')
plt.ylabel('var3')
plt.show()

plt.plot(data['var2'][cSig], data['var4'][cSig], 'r.', label='Signal')
plt.plot(data['var2'][cBgd], data['var4'][cBgd], 'b.', label='Background')
plt.xlabel('var2')
plt.ylabel('var4')
plt.show()

plt.plot(data['var3'][cSig], data['var4'][cSig], 'r.', label='Signal')
plt.plot(data['var3'][cBgd], data['var4'][cBgd], 'b.', label='Background')
plt.xlabel('var3')
plt.ylabel('var4')
plt.show()

var_list = data.keys()

weights = np.ones(nEvent)

BasePurity = float(sum(cSig))/(sum(cSig) + sum(cBgd))
BaseGini = sum(BasePurity)*(1 - BasePurity)

Gini = {}
Purity = {}
cutVals = {}
cutSet = (0, '')

for var in var_list:

    minVar = min(data[var])
    maxVar = max(data[var])
    diffVar = (maxVar - minVar)/100.

    cutVals[var] = np.arange(minVar+float(diffVar)/2,
                             maxVar-float(diffVar)/2, diffVar)

    tempArray = []

    for (i, cutVal) in zip(range(100), cutVals[var]):

        Bin1_S = np.sum((data[var][cSig] < cutVal))
        Bin1_B = np.sum((data[var][cBgd] < cutVal))
        Bin2_S = np.sum((data[var][cSig] >= cutVal))
        Bin2_B = np.sum((data[var][cBgd] >= cutVal))

        val = (float(Bin1_S)/(Bin1_S + Bin1_B))*(float(Bin2_B)/(Bin2_S + Bin2_B))

        if val > cutSet[0]:
            cutSet = (val, var)

        tempArray.append(val)

    Purity[var] = np.array(tempArray)
    Gini[var] = Purity[var]*(1-Purity[var])

    plt.plot(cutVals[var], Purity[var], 'b-')
    plt.ylabel('Purity')
    plt.xlabel(var)
    plt.show()

    plt.plot(cutVals[var], Gini[var], 'b-')
    plt.ylabel('Gini')
    plt.xlabel(var)
    plt.show()

print cutSet
