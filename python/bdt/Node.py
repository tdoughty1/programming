# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 18:24:06 2014

@author: tdoughty1
"""


class Node:

    def __init__(self):

        self._parent = None
        self._left = None
        self._right = None

    def AddRight(self, right):

        if isinstance(right, Node):
            self._right = right
        else:
            pass
            # Raise Exception

    def AddLeft(self, left):

        if isinstance(left, Node):
            self._left = left
        else:
            pass
            # Raise Exception

    def AddParent(self, parent):

        if isinstance(parent, Node):
            self._parent = parent
        else:
            pass
            # Raise Exception
