# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 14:50:16 2014

@author: tdoughty1
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
import pydot

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
    ax.plot(df[col][df['Class']==1], df['Rand'][df['Class']==1],'b.', label='Signal')
    ax.plot(df[col][df['Class']==0], df['Rand'][df['Class']==0],'g.', label='Background')
    ax.set_xlabel(col)
    ax.set_ylabel('Random Variable')
    ax.set_title('Distribution of %s' % col)
    ax.legend()
    f.savefig('figs/%s_dist.png' % col)

tree1 = Tree(df, plots=True)

for i in range(1, 5):
    print "Creating animation animation/var%d.gif" % i

    os.system('convert -delay 10 -loop 0 animation/var%d*.png animation/var%d.gif' % (i, i))
    os.system('rm animation/var%d*.png'  % i)

graph = pydot.Dot(graph_type='digraph')

PlotNodes = []

i = 0
for node in Tree.Objects:
    i += 1
    PlotNodes.append((pydot.Node("%d, B=%d, S=%d" % (i, node._nBgd, node._nSig)), node))

#ok, now we add the nodes to the graph
for gnode in PlotNodes:
    graph.add_node(gnode[0])

for node in PlotNodes:

    treenode = node[1]
    graphnode1 = node[0]

    # If not a final node
    if treenode.left is not None:

        graphnodeL = None
        graphnodeR = None

        # Loop treenodes to find connecting graph node of left and right treenodes
        for node2 in PlotNodes:
            if node2[1] is treenode.left:
                graphnodeL = node2[0]
                print "Found Left Node"
            if node2[1] is treenode.right:
                graphnodeR = node2[0]
                print "Found Right Node"

        print "Left Graph node is ", graphnodeL
        print "Right Graph node is ", graphnodeR

        if graphnodeL is None or graphnodeR is None:
            print "Error finding nodes"
            exit()
        else:
            print type(graphnode1)
            print type(graphnodeL)
            print type(graphnodeR)
            print "Adding Edge"
            print "Adding Edge"
            graph.add_edge(pydot.Edge(graphnode1, graphnodeL))
            graph.add_edge(pydot.Edge(graphnode1, graphnodeR))

    # Otherwise, no need to add edge
    else:
        continue

graph.write_png('example2_graph.png')
