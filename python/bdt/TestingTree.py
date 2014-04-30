# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 17:50:07 2014

@author: tdoughty1
"""

from TrainingTree import TrainingTree


class TestingTree:

    Counter = 0
    Objects = []

    def __init__(self, train):

        if not isinstance(train, TrainingTree):
            print "ERROR: in TestingTree.__init__:"
            print "Should input a trained tree."

        train.CreateTestingTree(self)
