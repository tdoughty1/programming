# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 09:51:13 2013

@author: tdoughty1
"""


class _Node(object):

    def __init__(self):
        self.item = None
        self.next = None


class LinkedQueue(object):

    def __init__(self):
        self._first = None
        self._last = None

    def isEmpty(self):
        return self._first is None

    def enqueue(self, item):
        oldlast = self._last
        self._last = _Node()
        self._last.item = item
        self._last.next = None
        if self._isEmpty():
            self._first = self._last
        oldlast.next = self._last

    def dequeue(self):
        item = self._first.item
        self._first = self._first.next
        if self.isEmpty():
            self._last = None
        return item
