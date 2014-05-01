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

    def Train(self, data, trainNode, testNode):

        # Base Case, node only has one class
        if len(unique(data['Class'])) == 1:
            self._left = None
            self._right = None

            trainNode._left = None
            trainNode._right = None

            testNode._left = None
            testNode._right = None

        # Recursive Call Case
        else:
            var, val = GetCut(data, 0, self._num, plot=True, animate=True)
            self.cut = (var, val)
            trainNode.cut = (var, val)
            testNode.cut = (var, val)

            self._left = CutNode()
            self._right = CutNode()

            trainNode._left = TrainingNode()
            trainNode._right = TrainingNode()

            testNode._left = TestingNode()
            testNode._right = TestingNode()

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
