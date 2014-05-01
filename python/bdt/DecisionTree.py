# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 09:01:15 2014

@author: tdoughty1
"""

from Tree import Tree
from TrainingTree import TrainingTree
from TestingTree import TestingTree


class DecisionTree(Tree, object):

    def __init__(self, tree1, tree2):

        Tree.__init__(self)

        if type(tree1) is TrainingTree and type(tree2) is TestingTree:
            self._train = tree1
            self._test = tree2
        elif type(tree2) is TrainingTree and type(tree1) is TestingTree:
            self._train = tree2
            self._test = tree1
        else:
            print "Error in DecisionTree.__init__:"
            print "Must be instantiated with a testing and a training tree."
