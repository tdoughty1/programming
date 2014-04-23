# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 10:19:38 2013

@author: tdoughty1
"""
import random


def exch(a, i, min_):
    tempi = a[i]
    tempmin = a[min_]

    a[i] = tempmin
    a[min_] = tempi


class Selection(object):
    '''
    Algorithm just runs through the group and checks each value against a
    minimum target.

    Problem - Scales as N^2 - even for sorted arrays
    '''

    def sort(a):
        N = len(a)
        for i in range(N):
            min_ = i
            for j in range(i+1, N):
                if a[j] < a[min_]:
                    min_ = j
            exch(a, i, min_)


class Insertion(object):
    '''
    Algorithm runs through list and moves each value one space until it is
    sorted.  Good for partially sorted array - ~N.

    Problem - Scales as 1/2N ^2 - Better than selection sort, but still slow
    '''

    def sort(a):
        N = len(a)
        for i in range(N):
            for j in range(i, 0, -1):
                if a[j] < a[j-1]:
                    exch(a, j, j-1)
                else:
                    break


class Shell(object):
    '''
    Algorithm uses insertion sort but moves values h len steps each round,
    dropping the value of h each round.

    Method for choosing h values is not entirely clear, but 3*x + 1 is good.
    '''

    def sort(a):
        N = len(a)

        # Find first h (ie step size) of h-sort
        h = 1
        while h < N/3:
            h = 3*h + 1

        # Implement Sort
        while h >= 1:
            for i in range(h, N):
                j = i
                while j >= h and a[j] < a[j-h]:
                    exch(a, j, j - h)
                    j -= h
            h = h/3


class Merge(object):
    '''
    Algorithm divides array into two halves, recursively sorts both halves,
    merges halves (Top Down).

    Problems - Doesn't work for short arrays - fix with cutoff
    '''

    def merge(self, a, aux, lo, mid, hi):

        assert self.isSorted(a, lo, mid)
        assert self.isSorted(a, mid+1, hi)

        for k in range(lo, hi + 1):
            aux[k] = a[k]

        i = lo
        j = mid + 1

        for k in range(lo, hi+1):
            if i > mid:
                a[k] = self._aux[j]
                j += 1
            elif j > hi:
                a[k] = self._aux[i]
                i += 1
            elif aux[j] < aux[i]:
                a[k] = self._aux[j]
                j += 1
            else:
                a[k] = self._aux[i]
                i += 1

        assert self.isSorted(a, lo, hi)

    def _sort(self, a, aux, lo, hi):

        # Added to speed up smallest arrays in recursive sort
        CUTOFF = 7

        if(hi <= lo + CUTOFF - 1):
            Insertion.sort(a, lo, hi)

        mid = lo + (hi - lo)/2
        self.sort(a, self._aux, lo, mid)
        self.sort(a, self._aux, mid+1, hi)
        if not a[mid+1] < a[mid]:
            return
        self.merge(a, self._aux, lo, mid, hi)

    def sort(self, a):

        self._aux = a[:]
        self._sort(a, self._aux, 0, len(a) - 1)

    def isSorted():
        return True


class MergeBU(Merge):

    def sort(self, a):
        N = len(a)
        self._aux = a[:]

        sz = 1
        while sz < N:
            lo = 0
            while lo < N - sz:
                self.merge(a, lo, lo + sz - 1, min(lo + sz + sz - 1, N-1))
                lo += sz + sz
            sz = sz + sz


class Quick(object):
    '''
    Algorithm shuffles the collection randomly.  Chooses first element as
    sorting key

    Problems - Too much overhead for small subarrays
             - Estimate the partitioning element is in the middle

    Solution - CutOff to Insertion sort for ~10 or less, could do w/single pass
             - Median of 3 partitioning (not implemented here)
    '''

    def partition(a, lo, hi):

        i = lo
        j = hi+1

        while True:

            i += 1
            while a[i] < a[lo]:
                if i == hi:
                    break
                i += 1

            j -= 1
            while a[lo] < a[j]:
                if j == lo:
                    break

            if i >= j:
                break

            exch(a, i, j)
            return j

    def sort(self, a):
        StdRandom.shuffle(a)
        self._sort(a, 0, len(a) - 1)

    def _sort(self, a, lo, hi):

        CUTOFF = 10

        if hi <= lo + CUTOFF - 1:
            return

        j = self.partition(a, lo, hi)
        self._sort(a, lo, j-1)
        self._sort(a, j+1, hi)


class StdRandom:

    def shuffle(a):
        N = len(a)
        for i in range(N):
            r = random.randint(0, i)
            exch(a, i, r)


def select(a, k):
    StdRandom.shuffle(a)
    lo = 0
    hi = len(a) - 1

    while hi > lo:

        j = Quick.partition(a, lo, hi)

        if j < k:
            lo = j + 1
        elif j > k:
            hi = j - 1
        else:
            return a[k]

        return a[k]
