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
