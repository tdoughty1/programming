# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 08:45:10 2013

@author: tdoughty1
"""


class _Node(object):

    def __init__(self):
        self.item = None
        self.next = None


class LinkedStack(object):

    def __init__(self):
        self._first = None

    def isEmpty(self):
        return self._first is None

    def push(self, item):
        oldfirst = self._first
        self._first = _Node()
        self._first.item = item
        self._first.next = oldfirst

    def pop(self):
        item = self._first.item
        self._first = self._first.next
        return item


class FixedCapacityStack(object):  # Doesn't really make sense in Python

    # BUGS: Doesn't match __init__ standard API
    #       Can Push/Pop off end of stack

    def __init__(self, capacity):
        self._s = [None]*capacity
        self._N = 0

    def isEmpty(self):
        return self._N == 0

    def push(self, item):
        self._s[self._N] = item
        self._N += 1

    def pop(self):
        self._N -= 1
        item = self._s[self._N]
        self._s[self._N] = None
        return item


class ResizingArrayStack(object):

    def __init__(self):
        self.s = [None]
        self._N = 0

    def isEmpty(self):
        return self._N == 0

    def push(self, item):
        if self._N == len(self._s):
            self.resize(2*len(self._s))
        self._s[self._N] = item
        self._N += 1

    def pop(self):
        self._N -= 1
        item = self._s[self._N]
        self._s[self._N] = None
        if self.N > 0 and self.N == len(self._s)/4:
            self._resize(len(self._s)/2)
        return item

    def _resize(self, capacity):
        copy = [None]*capacity
        copy[0:self._N] = self._s[:]
        self._s = copy
