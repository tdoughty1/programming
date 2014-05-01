# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 09:01:58 2014

@author: tdoughty1
"""

from Node import TrainingNode, TestingNode, CutNode


class Tree(object):

    pass


class TrainingTree(Tree):

    def __init__(self):
        self._base = TrainingNode()


class TestingTree(Tree):

    def __init__(self):
        self._base = TestingNode()


class CutTree(Tree):

    def __init__(self):
        self._base = CutNode()


class DecisionTree(object):

    def __init__(self):
        self._cuts = CutTree()
        self._train = TrainingTree()
        self._test = TestingTree()

    def Train(self, data):

        cutNode = self._cuts._base
        trainNode = self._train._base
        testNode = self._test._base

        cutNode.Train(data, trainNode, testNode)
