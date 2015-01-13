# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 10:26:36 2013

@author: tdoughty1
"""
import numpy as np


class UnionFind(object):

    def __init__(self, N):
        pass

    def union(self, p, q):
        pass

    def connected(self, p, q):
        pass


class QuickFindUF(object):
    '''
    Algorithm sets array elements for each node to connect.  Value changed so
    one number for each group of nodes.

    Problem - Union require N accesses - scales as N^2
    
    Possible Solutions - QuickUnion - below
    '''

    def __init__(self, N):
        self._id = np.array(range(N))

    def connected(self, p, q):
        return self._id[p] == self._id[q]

    def union(self, p, q):
        pid = self._id[p]
        qid = self._id[q]

        for i in range(len(self._id)):
            if self._id[i] == pid:
                self._id[i] = qid


class QuickUnionUF(object):
    '''
    Algorithm sets array with reference to parent in a tree.  Reference changes
    with union.

    Problem - Could scales as N^2 with large deep trees

    Possible Solutions:
        Weighting (link smaller tree under larger tree)
        Path Compression (move value to point to root)
    '''

    def __init__(self, N):
        self._id = np.array(range(N))

    def _root(self, i):
        while i != self._id[i]:
            i = id[i]
        return i

    def connected(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)
        self._id[i] = j


class WeightedCompressedQuickUnionUF(object):
    '''
    Algorithm is same as QuickUnion, but weights which tree is loaded under.
    And compressed tree by linking each node directly to root (or higher up
    tree).
    '''

    def __init__(self, N):
        self._id = np.array(range(N))
        self._sz = np.one(range(N))

    # Implementing one pass path compression - shortens by one level
    # Also possible to use two pass, point directly to root
    def _root(self, i):
        while i != self._id[i]:
            self._id[i] = self._id[self._id[i]]
            i = id[i]
        return i

    def connected(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)

        # New Weighting Routine
        if self._sz[i] < self._sz[j]:
            self._id[i] = j
            self.sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self.sz[i] += self._sz[j]
