# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 14:50:16 2014

@author: tdoughty1
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

from Tree import Tree

datafile = pd.HDFStore('datafile.h5')

newdata = True

df = None

if newdata:
    nEvent = 1000
    nClass = 4

    varNames = []

    for i in range(nClass):
        varNames.append('var' + str(i+1))

    tempdata = make_classification(nEvent, nClass)

    df = pd.DataFrame(tempdata[0])
    df.columns = varNames
    df['Rand'] = np.random.rand(len(df))
    df['Class'] = tempdata[1]

    datafile['df'] = df
else:
    df = datafile['df']

for col in df.columns:

    if col == 'Rand' or col == 'Class':
        continue

    f, ax = plt.subplots(1)
    f.set_size_inches((4, 5))
    bs = ax.scatter(df[col][df['Class'] == 1], df['Rand'][df['Class'] == 1],
                    color='b', marker='.')
    gs = ax.scatter(df[col][df['Class'] == 0], df['Rand'][df['Class'] == 0],
                    color='g', marker='.')
    ax.set_xlabel(col)
    ax.set_ylabel('Random Variable')
    ax.set_ylim([0, 1.5])
    ax.set_title('Distribution of %s' % col)
    ax.legend((bs, gs), ('Signal', 'Background'), loc=1, fontsize='small')
    f.savefig('figs/%s_dist.png' % col)
    plt.close()

tree1 = Tree(df)
tree1.AnimateCuts()
tree1.GraphTree(1)

print tree1.ScoreTree()

print "Before pruning, %d nodes" % len(Tree.Objects)

i = 1
while tree1.PruneTree():
    i += 1
    tree1.GraphTree(i)
    print tree1.ScoreTree()

print "After pruning, %d nodes" % len(Tree.Objects)

datafile.close
