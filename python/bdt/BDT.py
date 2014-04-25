# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 19:58:28 2014

@author: tdoughty1
"""

import numpy as np
import matplotlib.pylab as plt
from sklearn.datasets import make_classification
from operator import xor


class Tree(object):

    def __init__(self, data, class_data, level=0, debug=False, plots=False, side='top'):

        self.left = None
        self.right = None
        self.data = data
        self.class_data = class_data
        self._nEv = len(self.class_data)
        self._level = level + 1
        self._side = side

        for key in self.data.keys():
            dL = len(data[key])

            if dL != self._nEv:
                print "Data length %d doesn't match classification length %d for %s" % (dL, self._nEv, key)
                exit(1)

        self._cSig = class_data == 1
        self._cBgd = class_data == 0

        if len(self._cSig) != self._nEv:
            print 'Unexpected Signal Cut Length: %d' % len(self._cSig)
            exit(1)
        if len(self._cBgd) != self._nEv:
            print 'Unexpected Signal Cut Length: %d' % len(self._cBgd)
            exit(1)

        self._nSig = sum(self._cSig)
        self._nBgd = sum(self._cBgd)

        if debug:
            print "Events in Tree = ", (self._nEv)

        if (self._nSig + self._nBgd) != self._nEv:
            print "Unexpected Event Numbers"
            print "Signal = ", self._nSig
            print "Background = ", self._nBgd
            exit(1)

        self._Purity = float(self._nSig)/(self._nSig+self._nBgd)
        self._Gini = self._Purity*(1-self._Purity)

        if self._nSig > 5 and self._nBgd > 5:

            cutSet = self.SplitData()
            cc = data[cutSet[0]] < cutSet[1]

            if debug:
                print 'Returned Cut %s = %f' % (cutSet)
                print 'Group 1 = %d' % sum(cc)
                print 'Group 2 = %d' % sum(~cc)

            newdata1 = {}
            newdata2 = {}

            for key in data.keys():
                newdata1[key] = data[key][cc]
                newdata2[key] = data[key][~cc]

            if debug:
                print "Filling Left Tree with %d events" % sum(cc)
                print "Filling Right Tree with %d events" % sum(~cc)

            self.left = Tree(newdata1, class_data[cc], level=self._level, debug=debug, plots=plots, side='left')
            self.right = Tree(newdata2, class_data[~cc], level=self._level, debug=debug, plots=plots, side='right')

    def SplitData(self, plots=False, debug=False):

        Var_Cut = ''
        Val_Cut = -999999
        Purity = 0

        if debug:
            print "In Splitting Data"
            print "Number of Events = %d" % len(self.data['var1'])
            print "Number of Classified Events = %d" % len(self.class_data)

        for var in self.data.keys():

            if debug:
                print "Current Variable = %s" % var
                print "Number of Events = %d" % len(self.data[var])
                print "Number of Classified Events = %d" % len(self.class_data)

            minVar = min(self.data[var])
            maxVar = max(self.data[var])
            diffVar = (maxVar - minVar)/101.

            cutVals = np.arange(minVar+float(diffVar)/2,
                                maxVar-float(diffVar)/2, diffVar)

            for (i, cutVal) in zip(range(100), cutVals):

                Bin1_S = sum((self.data[var][self._cSig] < cutVal))
                Bin1_B = sum((self.data[var][self._cBgd] < cutVal))
                Bin2_S = sum((self.data[var][self._cSig] >= cutVal))
                Bin2_B = sum((self.data[var][self._cBgd] >= cutVal))

                val = (float(Bin1_S) / (Bin1_S + Bin1_B))*(float(Bin2_B) / (Bin2_S + Bin2_B))

                if val > Purity:
                    Purity = val
                    Var_Cut = var
                    Val_Cut = cutVal

        if plots:
            plt.plot(data[Var_Cut][self._cSig], np.random.rand(sum(self._cSig)),'b.')
            plt.plot(data[Var_Cut][self._cBgd] ,np.random.rand(sum(self._cBgd)),'g.')
            plt.plot([Val_Cut, Val_Cut],[0, 1], 'r-')
            plt.xlabel(Var_Cut)
            plt.title('Purity = ' + str(Purity))
            plt.show()

        cutSet = (Var_Cut, Val_Cut)
        if debug:
            print "Returning Cut %s = %f" % cutSet
        return cutSet

    def CountNodes(self):

        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.CountNodes()
        elif self.right is None:
            return self.left.CountNodes()
        else:
            return self.left.CountNodes() + self.right.CountNodes()

    def PrintTree(self):

        if self._level == 1:
            print "Root Tree has %d events: %d Signal, %d Background" % (self._nEv, self._nSig, self._nBgd)
        else:
            print "Tree on the %s of level %d has %d events:  %d Signal, %d Background" % (self._side, self._level, self._nEv, self._nSig, self._nBgd)

        if self.left is not None:
            self.left.PrintTree()

        if self.right is not None:
            self.right.PrintTree()

    def CheckTree(self):

        if xor(self.left is None, self.right is None):
            return False

        if self.left is None and self.right is None:
            return True

        return self.left.CheckTree() and self.right.CheckTree()

nEvent = 100
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

tree1 = Tree(data, classify)

tree1.CountNodes()
tree1.PrintTree()
tree1.CheckTree()
