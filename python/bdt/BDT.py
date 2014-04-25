# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 19:58:28 2014

@author: tdoughty1
"""

import numpy as np
import matplotlib.pylab as plt
from sklearn.datasets import make_classification


class Tree(object):

    def __init__(self, data, class_data):

        self.left = None
        self.right = None
        self.data = data
        self.class_data = class_data
        self._nEv = len(self.class_data)

        for key in self.data.keys():
            dL = len(data[key])

            if dL != self._nEv:
                print "Data length %d doesn't match classification length %d for %s" % (dL, nE, key)
                pass

        self._cSig = class_data == 1
        self._cBgd = class_data == 0

        if len(self._cSig) != self._nEv:
            print 'Unexpected Signal Cut Length: %d' % len(self._cSig)
        if len(self._cBgd) != self._nEv:
            print 'Unexpected Signal Cut Length: %d' % len(self._cBgd)

        self._nSig = sum(self._cSig)
        self._nBgd = sum(self._cBgd)

        print "Events in Tree = ", (self._nEv)
        if (self._nSig + self._nBgd) != self._nEv:
            print "Unexpected Event Numbers"
            print "Signal = ", self._nSig
            print "Background = ", self._nBgd

        self._Purity = float(self._nSig)/(self._nSig+self._nBgd)
        self._Gini = self._Purity*(1-self._Purity)

        if self._nSig > 10 and self._nBgd > 10:
            cutSet = self.SplitData()
            print 'Returned Cut %s = %f' % (cutSet)

            cc = data[cutSet[0]] < cutSet[1]

            print 'Group 1 = %d' % sum(cc)
            print 'Group 2 = %d' % sum(~cc)

            newdata1 = {}
            newdata2 = {}

            for key in data.keys():
                newdata1[key] = data[key][cc]
                newdata2[key] = data[key][~cc]

            print "Filling Left Tree with %d events" % sum(cc)
            self.left = Tree(newdata1, class_data[cc])
            print "Filling Right Tree with %d events" % sum(~cc)
            self.right = Tree(newdata2, class_data[~cc])

    def SplitData(self):

        Var_Cut = ''
        Val_Cut = -999999
        Purity = 0

        print "In Splitting Data"
        print "Number of Events = %d" % len(self.data['var1'])
        print "Number of Classified Events = %d" % len(self.class_data)

        for var in self.data.keys():

            print "Current Variable = %s" % var
            print "Number of Events = %d" % len(self.data[var])
            print "Number of Classified Events = %d" % len(self.class_data)

            minVar = min(self.data[var])
            maxVar = max(self.data[var])
            diffVar = (maxVar - minVar)/101.

            cutVals = np.arange(minVar+float(diffVar)/2,
                                maxVar-float(diffVar)/2, diffVar)

            #print 'minVar = ', minVar
            #print 'maxVar = ', maxVar
            #print 'diffVar = ', diffVar

            for (i, cutVal) in zip(range(100), cutVals):

                Bin1_S = sum((self.data[var][self._cSig] < cutVal))
                Bin1_B = sum((self.data[var][self._cBgd] < cutVal))
                Bin2_S = sum((self.data[var][self._cSig] >= cutVal))
                Bin2_B = sum((self.data[var][self._cBgd] >= cutVal))

                #print 'Cut Value = ', cutVal

                #print 'Bin 1 Signal = ', Bin1_S
                #print 'Bin 1 Background = ',  Bin1_B
                #print 'Bin 2 Signal = ',  Bin2_S
                #print 'Bin 2 Background = ',  Bin2_B

                if (Bin1_S + Bin1_B) == 0 or (Bin2_S + Bin2_B) == 0:
                    print "Found Empty Bin: %d" % i
                    print cutVal
                    print "minVar = ", minVar
                    print "maxVar = ", maxVar
                    print "Data minimum = ", min(self.data[var])
                    print "Data maximum = ", max(self.data[var])
                    print "Signal minimum = ", min(self.data[var][self._cSig])
                    print "Signal maximum = ", max(self.data[var][self._cSig])
                    print "Signal value = ", np.unique(self.class_data[self._cSig])
                    print "Background minimum = ", min(self.data[var][self._cBgd])
                    print "Background maximum = ", max(self.data[var][self._cBgd])
                    print "Background value = ", np.unique(self.class_data[self._cBgd])
                    print "Total events selected = ", sum(self._cBgd | self._cSig)

                    #print "Minimum occurs at %d", np.argmin(self.)
                    print "Debug Here"

                val = (float(Bin1_S) / (Bin1_S + Bin1_B))*(float(Bin2_B) / (Bin2_S + Bin2_B))

                if val > Purity:
                    Purity = val
                    Var_Cut = var
                    Val_Cut = cutVal

        plt.plot(data[Var_Cut][self._cSig], np.random.rand(sum(self._cSig)),'b.')
        plt.plot(data[Var_Cut][self._cBgd] ,np.random.rand(sum(self._cBgd)),'g.')
        plt.plot([Val_Cut, Val_Cut],[0, 1], 'r-')
        plt.xlabel(Var_Cut)
        plt.title('Purity = ' + str(Purity))
        plt.show()

        cutSet = (Var_Cut, Val_Cut)
        print "Returning Cut %s = %f" % cutSet
        return cutSet

    def CountTrees(self):

        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.CountTrees()
        elif self.right is None:
            return self.left.CountTrees()
        else:
            return self.left.CountTrees() + self.right.CountTrees()

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
