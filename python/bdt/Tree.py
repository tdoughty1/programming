# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 09:01:58 2014

@author: tdoughty1
"""

from shutil import rmtree
from os.path import isdir

from Node import TrainingNode, TestingNode, CutNode


class Tree(object):

    Counter = 0
    Objects = []

    def __init__(self):
        type(self).Counter += 1
        type(self).Objects.append(self)


class TrainingTree(Tree):

    Counter = 0
    Objects = []

    def __init__(self):
        Tree.__init__(self)
        self._base = TrainingNode()


class TestingTree(Tree):

    Counter = 0
    Objects = []

    def __init__(self):
        self._base = TestingNode()


class CutTree(Tree):

    Counter = 0
    Objects = []

    def __init__(self):
        self._base = CutNode()


class DecisionTree(object):

    Counter = 0
    Objects = []

    def __init__(self):
        self._cuts = CutTree()
        self._train = TrainingTree()
        self._test = TestingTree()

    def Train(self, data, plot=False, animate=False):

        cutNode = self._cuts._base
        trainNode = self._train._base
        testNode = self._test._base

        if plot:
            if isdir('figs'):
                rmtree('figs')

        if animate:
            if isdir('animate'):
                rmtree('animate')

        cutNode.Train(data, trainNode, testNode, plot=plot, animate=animate)
