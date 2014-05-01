# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 18:24:06 2014

@author: tdoughty1
"""

from numpy import unique

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
        trainNode._nEv = len(train)
        testNode._nEv = len(test)
        trainNode._nSig = len(train[data['Sig']])
        testNode._nSig = len(test[data['Sig']])
        trainNode._nBgd = len(train[data['Bgd']])
        testNode._nBgd = len(test[data['Bgd']])

        # Base Case, node only has one class
        if len(unique(data['Sig'])) == 1:
            self._left = None
            self._right = None

            trainNode._left = None
            trainNode._right = None

            testNode._left = None
            testNode._right = None

        # Recursive Call Case
        else:

            # Get cut used at this node
            var, val = GetCut(data, 0, self._num, plot=plot, animate=animate)

            # Store cut in node for each of the trees
            self.cut = (var, val)
            trainNode.cut = (var, val)
            testNode.cut = (var, val)

            # Link Lower Values
            self._left = CutNode()
            self._right = CutNode()
            trainNode._left = TrainingNode()
            trainNode._right = TrainingNode()
            testNode._left = TestingNode()
            testNode._right = TestingNode()

            # Recursive call moves further down tree
            self._left.Train(data[data[var] <= val],
                             trainNode._left, testNode._left)
            self._right.Train(data[data[var] > val],
                              trainNode._right, testNode._right)


class TrainingNode(Node):

    Objects = []
    Counter = 0


class TestingNode(Node):

    Objects = []
    Counter = 0
