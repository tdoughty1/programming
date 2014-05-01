# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 20:37:55 2014

@author: tdoughty1
"""

from os import system, makedirs
from os.path import isdir
from numpy import arange, argmax, nonzero
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.pylab import close as mplclose


# Select number of bins based on number of events
def _GetN(nEv):

    if nEv >= 100:
        return 100
    elif nEv >= 25:
        return 25
    else:
        return nEv


def _GetBinning(minVar, maxVar, n, debug=False):

    diffVar = float(maxVar - minVar)/(n+1)

    if debug:
        print 'minVar = ', minVar
        print 'maxVar = ', maxVar
        print 'diffVar = ', diffVar

    return arange(minVar + diffVar/2, maxVar - diffVar/2, diffVar)


def _Purity(data, debug=False):

    if debug:
        print 'nTotal = ', len(data)
        print 'nSig = ', sum(data['Class'] == 1)
        print "Purity = ", float(sum(data['Class'] == 1))/len(data)

    return float(sum(data['Class']))/len(data)


def _Gini(data, debug=False):

    P = _Purity(data, debug)

    if debug:
        print "Gini = ", P*(1-P)

    return P*(1-P)


def _Info(data, debug=False):

    I = len(data)*_Gini(data, debug)

    if debug:
        print "Info = ", I

    return I


def _PlotCut(data, var, cutVals, IG, nTree, nCut):

    # Define a useful quantity
    cutVal = cutVals[argmax(IG)]

    # Create figure with two vertical subplots
    fig = Figure()
    canvas = FigureCanvas(fig)
    fig.set_size_inches(5, 6)
    fig.subplots_adjust(hspace=.05)
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    # First subplot is scatter plot with cut shown
    xdataS = data[var][data['Class'] == 1]
    ydataS = data['Rand'][data['Class'] == 1]
    xdataB = data[var][data['Class'] == 0]
    ydataB = data['Rand'][data['Class'] == 0]
    ax1.plot(xdataS, ydataS, 'b.', label='Signal')
    ax1.plot(xdataB, ydataB, 'g.', label='Background')
    ax1.plot([cutVal]*2, [0, 1.5], 'r-', label='Optimal Cut')
    ax1.legend(numpoints=1, loc=1)
    ax1.set_ylim([0, 1.5])
    ax1.set_ylabel('Arbitrary Value')
    ax1.set_xlim([min(cutVals), max(cutVals)])
    ax1.xaxis.set_ticklabels([])
    ax1.set_title('Optimal Cut for ' + var)

    # Second subplot is line plot of IG
    ax2.plot(cutVals, IG, 'r-')
    ax2.plot(cutVal, max(IG), 'ro', label='Optimal Cut')
    ax2.legend(loc=0)
    ax2.set_ylabel('Information Gain')
    ax2.set_xlim([min(cutVals), max(cutVals)])
    ax2.set_xlabel(var + ' Cut Value')

    # Check if destination folder exists in figs
    dname = 'figs/tree%d/cut%d/' % (nTree, nCut)
    if not isdir(dname):
        makedirs(dname)
    fname = '%s/%s.png' % (dname, var)

    # Save Figure in cut folder and close
    canvas.print_figure(fname)
    ax1.cla()
    ax2.cla()
    fig.clf()
    mplclose(fig)


def _PlotAnimateCut(data, var, val, cutVals, IG, nTree, nCut, i):

    # Create figure with two vertical subplots
    fig = Figure()
    canvas = FigureCanvas(fig)
    fig.set_size_inches(5, 6)
    fig.subplots_adjust(hspace=.05)
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    # First subplot is scatter plot with cut shown
    xdataS = data[var][data['Class'] == 1]
    ydataS = data['Rand'][data['Class'] == 1]
    xdataB = data[var][data['Class'] == 0]
    ydataB = data['Rand'][data['Class'] == 0]
    ax1.plot(xdataS, ydataS, 'b.', label='Signal')
    ax1.plot(xdataB, ydataB, 'g.', label='Background')
    ax1.plot([val]*2, [0, 1.5], 'r-', label='Current Cut')
    ax1.legend(numpoints=1, loc=1)
    ax1.set_ylim([0, 1.5])
    ax1.set_ylabel('Arbitrary Value')
    ax1.set_xlim([min(cutVals), max(cutVals)])
    ax1.xaxis.set_ticklabels([])
    ax1.set_title('Information Gain for ' + var)

    # Second subplot is line plot of IG
    ax2.plot(cutVals[0:len(IG)], IG, 'r-')
    ax2.plot(val, IG[-1], 'ro')
    ax2.set_ylabel('Information Gain')
    ax2.set_xlim([min(cutVals), max(cutVals)])
    ax2.set_xlabel(var + ' Cut Value')

    # Check if destination folder exists in animate
    dname = 'animate/tree%d/cut%d/' % (nTree, nCut)
    if not isdir(dname):
        makedirs(dname)
    fname = '%s/%s_%02d.png' % (dname, var, i)

    # Save Figure and close
    canvas.print_figure(fname)
    ax1.cla()
    ax2.cla()
    fig.clf()
    mplclose(fig)


def _CreateAnimation(var, nTree, nCut):

    folder = 'animate/tree%d/cut%d/' % (nTree, nCut)
    system('convert -delay 10 -loop 0 %s/%s*.png %s/%s.gif'
           % (folder, var, folder, var))
    system('rm %s/%s*.png' % (folder, var))
    system('convert %s/%s.gif -fuzz 30%% -layers Optimize %s/%s.gif'
           % (folder, var, folder, var))


def GetCut(data, nTree, nCut, plot=False, animate=False, debug=False):

    # Get Number of Events
    nEv = len(data)

    # Select number of bins based on number of events
    n = _GetN(nEv)

    CutVal = None
    CutVar = None
    CutGain = None

    # Loop through each variable
    for var in data.columns:

        if 'var' not in var:
            continue

        # Select appropriate binning given the range and number of bins
        minVar = min(data[var])
        maxVar = max(data[var])
        cutVals = _GetBinning(minVar, maxVar, n, debug)

        # Loop through bins to find Information Gain for each value of cut
        IG = []
        for val in cutVals:

            left = data[data[var] <= val]
            right = data[data[var] > val]

            IG.append(_Info(data, debug) -
                      _Info(left, debug) -
                      _Info(right, debug))

            # To animate plots (optional), we first need to save a figure at
            # each step in the checking
            if animate:
                i = nonzero(cutVals == val)[0][0]
                _PlotAnimateCut(data, var, val, cutVals, IG, nTree, nCut, i)

            # If the most recent Information is greater than the current max
            # store new values of cut
            if IG[-1] > CutGain:
                CutVal = val
                CutVar = var
                CutGain = IG[-1]

        # After looping through variable, plot cut for that variable (optional)
        if plot:
            print "Plotting figure for %s in cut %d" % (var, nCut)
            _PlotCut(data, var, cutVals, IG, nTree, nCut)

        # After looping through variable, combine plots into gif using convert
        if animate:
            print "Animating figure for %s in cut %d" % (var, nCut)
            _CreateAnimation(var, nTree, nCut)

    # After looping through all variables, return selected cut (should be max)
    return (CutVar, CutVal)
