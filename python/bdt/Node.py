# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 18:24:06 2014

@author: tdoughty1
"""

from BDTHelper import GetCut


class Node(object):

    def __init__(self):

        self._parent = None
        self._left = None
        self._right = None

        type(self).Objects.append(self)
        type(self).Counter += 1

        self._num = type(self).Counter


class CutNode(Node):

    Objects = []
    Counter = 0

    def Train(self, data, trainNode, testNode, plot=False, animate=False):

        # Separate into training and testing samples
        train = data[data['Train']]
        test = data[data['Test']]

        # Count Events at this node, store in training and testing trees
        trainNode.StoreData(train)
        testNode.StoreData(test)

        # Base Case, node only has one class
        if len(train[data['Sig']]) == 0 or len(train[data['Bgd']]) == 0:
            self._left = None
            self._right = None

            trainNode._left = None
            trainNode._right = None

            testNode._left = None
            testNode._right = None

        # Recursive Call Case
        else:

            # Get cut used at this node
            cutTuple = GetCut(train, 0, self._num, plot=plot, animate=animate)

            # Store cut in node for each of the trees
            self.cut = cutTuple
            trainNode.cut = cutTuple
            testNode.cut = cutTuple

            # Link Lower Values
            self._left = CutNode()
            self._right = CutNode()
            trainNode._left = TrainingNode()
            trainNode._right = TrainingNode()
            testNode._left = TestingNode()
            testNode._right = TestingNode()

            var = cutTuple[0]
            val = cutTuple[1]

            # Recursive call moves further down tree
            self._left.Train(data[data[var] <= val], trainNode._left,
                             testNode._left, plot=plot, animate=animate)
            self._right.Train(data[data[var] > val], trainNode._right,
                              testNode._right, plot=plot, animate=animate)


class TrainingNode(Node):

    Objects = []
    Counter = 0

    def StoreData(self, data):

        self._nEv = len(data)
        self._nSig = len(data[data['Sig']])
        self._nBgd = len(data[data['Bgd']])
        self._Purity = float(self._nSig)/self._nEv
        self._Gini = (1 - self._Purity)*self._Purity
        self._Info = self._nEv*self._Gini

    def TagLeaves(self):

        # Base Case
        if self._left is None and self._right is None:

            if self._nSig > self._nBgd:
                self._class = 'Sig'
            elif self._nBgd > self._nSig:
                self._class = 'Bgd'
            else:
                self._class = 'None'
        # Otherwise move down tree
        else:
            self._left.TagLeaves()
            self._right.TagLeaves()

    def ScoreLeaves(self):

        # BaseCase
        if self._left is None and self._right is None:

            if self._class == 'Sig':
                score = (self._nSig, self._nEv)
            elif self._class == 'Bgd':
                score = (self._nBgd, self._nEv)
            else:
                score = (0, self._nEv)

        # Otherwise move down tree
        else:
            scoreL = self._left.ScoreLeaves()
            scoreR = self._right.ScoreLeaves()
            score = (scoreL[0] + scoreR[0], scoreL[1] + scoreR[1])

        return score

    def Prune(self, score, testNode):

        Ltree = self._left
        Rtree = self._right

        # Base case, parent to leaf
        if(Ltree._left is None and Ltree._right is None and
           Rtree._left is None and Rtree._right is None):

            # Get information gain from parent to leaf split
            InfoGain = -(self._Info - self._left._Info - self._right._Info)

            # If InfoGain is less than a threshold, then prune leaf
            if InfoGain < score:
                self._left = None
                self._right = None

                testNode._left = None
                testNode._right = None
                return True
            else:
                return False

        # Otherwise move down Tree
        else:
            LP = False
            RP = False

            if Ltree._left is not None and Ltree._right is not None:
                LP = Ltree.Prune(score, testNode._left)

            if Rtree._left is not None and Rtree._right is not None:
                RP = Rtree.Prune(score, testNode._right)

            return (LP or RP)


class TestingNode(Node):

    Objects = []
    Counter = 0

    def StoreData(self, data):

        self._nEv = len(data)

        if self._nEv == 0:
            self._nSig = 0
            self._nBgd = 0
            self._Purity = 0
            self._Gini = 0
            self._Info = 0
        else:
            self._nSig = len(data[data['Sig']])
            self._nBgd = len(data[data['Bgd']])
            self._Purity = float(self._nSig)/self._nEv
            self._Gini = (1 - self._Purity)*self._Purity
            self._Info = self._nEv*self._Gini

    def TagLeaves(self):

        # Base Case
        if self._left is None and self._right is None:

            if self._nSig > self._nBgd:
                self._class = 'Sig'
            elif self._nBgd > self._nSig:
                self._class = 'Bgd'
            else:
                self._class = 'None'
        # Otherwise move down tree
        else:
            self._left.TagLeaves()
            self._right.TagLeaves()

    def ScoreLeaves(self):

        # BaseCase
        if self._left is None and self._right is None:

            if self._class == 'Sig':
                score = (self._nSig, self._nEv)
            elif self._class == 'Bgd':
                score = (self._nBgd, self._nEv)
            else:
                score = (0, self._nEv)

        # Otherwise move down tree
        else:
            scoreL = self._left.ScoreLeaves()
            scoreR = self._right.ScoreLeaves()
            score = (scoreL[0] + scoreR[0], scoreL[1] + scoreR[1])

        return score
