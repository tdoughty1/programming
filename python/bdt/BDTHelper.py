# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 20:37:55 2014

@author: tdoughty1
"""

from numpy import arange


# Select number of bins based on number of events
def _GetN(nEv):

    if nEv >= 100:
        return 100
    elif nEv >= 25:
        return 25
    else:
        return nEv


def _GetBinning(minVar, maxVar, n):
    print 'minVar = ', minVar
    print 'maxVar = ', maxVar
    diffVar = float(maxVar - minVar)/(n+1)
    print 'diffVar = ', diffVar
    return arange(minVar + diffVar/2, maxVar - diffVar/2, diffVar)


def _Purity(data):
    print 'nTotal = ', len(data)
    print 'nSig = ', sum(data['Class'] == 1)
    print "Purity = ", float(sum(data['Class'] == 1))/len(data)
    return float(sum(data['Class']))/len(data)


def _Gini(data):
    P = _Purity(data)
    print "Gini = ", P*(1-P)
    return P*(1-P)


def _Info(data):
    I = len(data)*_Gini(data)
    print "Info = ", I
    return I


def GetCut(data):

    # Get Number of Events
    nEv = len(data)

    # Select number of bins based on number of events
    n = _GetN(nEv)

    CutVal = -999999
    CutVar = ''
    CutGain = 0

    for var in data.columns:

        if 'var' not in var:
            continue

        minVar = min(data[var])
        maxVar = max(data[var])

        cutVals = _GetBinning(minVar, maxVar, n)

        SG = []

        for val in cutVals:

            left = data[data[var] <= val]
            right = data[data[var] > val]

            SG.append(_Info(data) - _Info(left) - _Info(right))

            if SG[-1] > CutGain:
                CutVal = val
                CutVar = var
                CutGain = SG[-1]

    return (CutVar, CutVal)
