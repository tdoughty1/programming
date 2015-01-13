# -*- coding: utf-8 -*-
"""
Created on Thu May  1 21:03:14 2014

@author: tdoughty1
"""

from numpy import zeros, random
from time import time


def QMerge(array1, array2):

    i = 0
    j = 0
    k = 0

    imax = len(array1)
    jmax = len(array2)
    kmax = imax + jmax

    tempArray = zeros(kmax)

    while k < kmax:

        # At end of first array
        if i == imax:
            tempArray[k:] = array2[j:]
            return tempArray

        # At end of second array
        if j == jmax:
            tempArray[k:] = array1[i:]
            return tempArray

        # Standard Case
        if array1[i] < array2[j]:
            tempArray[k] = array1[i]
            i += 1
            k += 1
        else:
            tempArray[k] = array2[j]
            j += 1
            k += 1


def MergeSort(testArray):

    n = len(testArray)

    if n == 1:
        return testArray

    else:
        array1 = testArray[0:n/2]
        array2 = testArray[n/2:]

        array1 = MergeSort(array1)
        array2 = MergeSort(array2)

        return QMerge(array1, array2)

N = 1000000

testArray = random.rand(N)

start = time()
testArray = MergeSort(testArray)
finish = time()

print "Took %.3f us" % ((finish-start)*1000)
