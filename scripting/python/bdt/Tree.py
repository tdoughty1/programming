# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 09:01:58 2014

@author: tdoughty1
"""

from shutil import rmtree
from os.path import isdir

from Node import TrainNode, TestNode, CutNode


class DecisionTree(object):

    def __init__(self):

        # Store Node information in array for convenience in some steps
        self._CutNodes = []
        self._TrainNodes = []
        self._TestNodes = []
        self._pTrainNodes = []
        self._pTestNodes = []

        # Set up nodes as a tree
        self._CutTree = CutNode(tree=self)
        self._TrainTree = TrainNode(tree=self)
        self._TestTree = TestNode(tree=self)

    def Train(self, data, plot=False, animate=False):

        cutRoot = self._CutTree
        trainRoot = self._TrainTree
        testRoot = self._TestTree

        if plot:
            if isdir('figs'):
                rmtree('figs')

        if animate:
            if isdir('animate'):
                rmtree('animate')

        cutRoot.Train(data, trainRoot, testRoot, plot=plot, animate=animate)

        trainRoot.TagNodes(testRoot)

    def Score(self):

        trScoreTuple = self._TrainTree.ScoreLeaves()
        tsScoreTuple = self._TestTree.ScoreLeaves()

        self._TrainScore = float(trScoreTuple[0])/trScoreTuple[1]
        self._TestScore = float(tsScoreTuple[0])/tsScoreTuple[1]

    def Prune(self, score):

        while(self._TrainTree.PruneNodes(score, self._TestTree)):
            pass

    def PrintScore(self):
        print "Training Score = ", self._TrainScore
        print "Testing Score = ", self._TestScore
