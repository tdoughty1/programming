# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 18:24:06 2014

@author: tdoughty1
"""

from BDTHelper import GetCut


class Node(object):

    def __init__(self, tree=None, parent=None):

        self._tree = tree
        self._parent = parent
        self._left = None
        self._right = None

        self._num = self.GetNum()

    def StoreData(self, data):

        self._nEv = len(data)
        self._nSig = len(data[data['Sig']])
        self._nBgd = len(data[data['Bgd']])

        if self._nEv > 0:
            self._Purity = float(self._nSig)/self._nEv
        else:
            self._Purity = 1

        self._Gini = (1 - self._Purity)*self._Purity
        self._Info = self._nEv*self._Gini

    def TagNodes(self, testNode):

        if self._nSig > self._nBgd:
            self._EvClass = 'Sig'
            testNode._EvClass = 'Sig'
        elif self._nBgd > self._nSig:
            self._EvClass = 'Bgd'
            testNode._EvClass = 'Bgd'
        else:
            self._EvClass = 'None'
            testNode._EvClass = 'None'

        # Base Case
        if self._left is None and self._right is None:
            pass
        # Otherwise move down tree
        else:
            self._left.TagNodes(testNode._left)
            self._right.TagNodes(testNode._right)

    def ScoreLeaves(self):

        # BaseCase
        if self._left is None and self._right is None:

            if self._EvClass == 'Sig':
                score = (self._nSig, self._nEv)
            elif self._EvClass == 'Bgd':
                score = (self._nBgd, self._nEv)
            else:
                score = (0, self._nEv)

        # Otherwise move down tree
        else:
            scoreL = self._left.ScoreLeaves()
            scoreR = self._right.ScoreLeaves()
            score = (scoreL[0] + scoreR[0], scoreL[1] + scoreR[1])

        return score

    def PruneNodes(self, score, testNode, debug=False):

        Ltree = self._left
        Rtree = self._right

        # Base case, parent to leaf
        if(Ltree._left is None and Ltree._right is None and
           Rtree._left is None and Rtree._right is None):

            # Get information gain from parent to leaf split
            InfoGain = self._Info - self._left._Info - self._right._Info

            # If InfoGain is less than a threshold, then prune leaf
            if InfoGain < score:

                if debug:
                    print "Score Threshold = %.1f" % score
                    print "Pruning Nodes %d & %d" % (Ltree._num, Rtree._num)
                    print "Info Gain = %.2f" % InfoGain

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
                LP = Ltree.PruneNodes(score, testNode._left)

            if Rtree._left is not None and Rtree._right is not None:
                RP = Rtree.PruneNodes(score, testNode._right)

            return (LP or RP)


class CutNode(Node):

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
            self._left = CutNode(self._tree, self)
            self._right = CutNode(self._tree, self)
            trainNode._left = TrainNode(trainNode._tree, trainNode)
            trainNode._right = TrainNode(trainNode._tree, trainNode)
            testNode._left = TestNode(testNode._tree, testNode)
            testNode._right = TestNode(testNode._tree, testNode)

            var = cutTuple[0]
            val = cutTuple[1]

            # Recursive call moves further down tree
            self._left.Train(data[data[var] <= val], trainNode._left,
                             testNode._left, plot=plot, animate=animate)
            self._right.Train(data[data[var] > val], trainNode._right,
                              testNode._right, plot=plot, animate=animate)

    def GetNum(self):
        n = len(self._tree._CutNodes)
        self._tree._CutNodes.append(self)
        return n


class TrainNode(Node):

    def GetNum(self):
        n = len(self._tree._TrainNodes) + len(self._tree._pTrainNodes)
        self._tree._TrainNodes.append(self)
        return n


class TestNode(Node):

    def GetNum(self):
        n = len(self._tree._TestNodes) + len(self._tree._pTestNodes)
        self._tree._TestNodes.append(self)
        return n
