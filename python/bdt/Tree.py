# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 19:58:28 2014

@author: tdoughty1
"""

import numpy as np
import matplotlib.pylab as plt
from operator import xor
import warnings
import pydot

warnings.filterwarnings("ignore", category=DeprecationWarning, module="pandas")


class Tree(object):

    Counter = 0
    Objects = []

    def __init__(self, df, level=0, debug=False, plots=False, side='top'):

        Tree.Counter += 1
        Tree.Objects.append(self)

        self.left = None
        self.right = None
        self.df = df
        self._nEv = len(df)
        self._level = level + 1
        self._side = side

        self._cSig = df['Class'] == 1
        self._cBgd = df['Class'] == 0

        if len(self._cSig) != self._nEv:
            print 'Unexpected Signal Cut Length: %d' % len(self._cSig)
            exit(1)
        if len(self._cBgd) != self._nEv:
            print 'Unexpected Signal Cut Length: %d' % len(self._cBgd)
            exit(1)

        self._nSig = sum(self._cSig)
        self._nBgd = sum(self._cBgd)

        if debug:
            print "Events in Tree = ", (self._nEv)

        if (self._nSig + self._nBgd) != self._nEv:
            print "Unexpected Event Numbers"
            print "Signal = ", self._nSig
            print "Background = ", self._nBgd
            exit(1)

        self._Purity = float(self._nSig)/(self._nSig+self._nBgd)
        self._Gini = self._Purity*(1-self._Purity)

        if self._nSig > 0 and self._nBgd > 0:

            cutSet = self.FindCut(plots=plots, debug=debug)
            cc = df[cutSet[0]] < cutSet[1]

            if debug:
                print 'Returned Cut %s = %f' % (cutSet)
                print "Filling Left Tree with %d events" % sum(cc)
                print "Filling Right Tree with %d events" % sum(~cc)

            self.left = Tree(self.df[cc], level=self._level, debug=debug, plots=plots, side='left')
            self.right = Tree(self.df[~cc], level=self._level, debug=debug, plots=plots, side='right')

    def FindCut(self, plots=False, debug=False):

        Var_Cut = ''
        Val_Cut = -999999
        SeperationGain = 0

        if self._nEv > 100:
            n = 100
        elif self._nEv > 50:
            n = 25
        else:
            n = self._nEv

        if debug:
            print "In Splitting Data"

        for var in self.df.columns:

            if var == 'Class' or var == 'Rand':
                continue

            if debug:
                print "Current Variable = %s" % var
                print "Number of Events = %d" % len(self.df[var])
                print "Number of Classified Events = %d" % self._nEv

            SG = []

            minVar = min(self.df[var])
            maxVar = max(self.df[var])
            diffVar = (maxVar - minVar)/(n+1)

            cutVals = np.arange(minVar+float(diffVar)/2,
                                maxVar-float(diffVar)/2, diffVar)

            if len(cutVals) != n:
                cutVals = cutVals[0:n]

            for (i, cutVal) in zip(range(n), cutVals):

                nL = sum(self.df[var] <= cutVal)
                nR = sum(self.df[var] > cutVal)

                sL = sum((self.df[var][self._cSig] < cutVal))
                sR = sum((self.df[var][self._cSig] >= cutVal))

                pL = float(sL)/nL
                pR = float(sR)/nR

                gL = pL*(1-pL)
                gR = pR*(1-pR)

                val = self._nEv*self._Gini - nL*gL - nR*gR

                SG.append(val)

                if plots and Tree.Counter == 1:

                    f, axarr = plt.subplots(2, sharex=True)
                    bs = axarr[0].scatter(self.df[var][self._cSig], self.df['Rand'][self._cSig], color='b', marker='.')
                    gs = axarr[0].scatter(self.df[var][self._cBgd], self.df['Rand'][self._cBgd], color='g', marker='.')
                    axarr[0].set_xlim(min(cutVals), max(cutVals))
                    xax = axarr[0].get_xlim()
                    rl, = axarr[0].plot([cutVal]*2, [0, 1], 'r-')
                    axarr[0].set_title('Cutting on %s\nSeperation Gain = %.2f' % (var, val))
                    axarr[0].set_ylabel('Random Variable')
                    axarr[0].legend((bs, gs, rl), ('Signal', 'Background', 'Current Cut'), loc='right')

                    axarr[1].plot(cutVals[0:len(SG)],SG,'r-')
                    axarr[1].set_xlim(xax)
                    axarr[1].set_ylabel('Seperation Gain')
                    axarr[1].set_xlabel(var)

                    f.savefig('animation/%s_%02d.png' % (var, i))
                    plt.close(f)

                if val > SeperationGain:
                    SeperationGain = val
                    Var_Cut = var
                    Val_Cut = cutVal

            if plots and Tree.Counter == 1:
                f, axarr = plt.subplots(2, sharex=True)
                bs = axarr[0].scatter(self.df[var][self._cSig], self.df['Rand'][self._cSig], color='b', marker='.')
                gs = axarr[0].scatter(self.df[var][self._cBgd], self.df['Rand'][self._cBgd], color='g', marker='.')
                axarr[0].set_xlim(min(cutVals), max(cutVals))
                xax = axarr[0].get_xlim()
                rl, = axarr[0].plot([cutVals[np.argmax(SG)]]*2, [0, 1], 'r-', label='Best Cut')
                axarr[0].set_title('Cutting on %s\nSeperation Gain = %.2f' % (var, max(SG)))
                axarr[0].set_ylabel('Random Variable')
                axarr[0].legend((bs, gs, rl), ('Signal', 'Background', 'Best Cut'), loc='right')

                axarr[1].plot(cutVals, SG, 'r-')
                axarr[1].set_xlim(xax)
                axarr[1].set_ylabel('Seperation Gain')
                axarr[1].set_xlabel(var)

                f.savefig('figs/%s.png' % var)
                plt.close(f)

        cutSet = (Var_Cut, Val_Cut)
        if debug:
            print "Returning Cut %s = %f" % cutSet
        return cutSet

    def CountNodes(self):

        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.CountNodes() + 1
        elif self.right is None:
            return self.left.CountNodes() + 1
        else:
            return self.left.CountNodes() + self.right.CountNodes() + 1

    def PrintTree(self):

        if self._level == 1:
            print "Root Tree has %d events: %d Signal, %d Background" % (self._nEv, self._nSig, self._nBgd)
        else:
            print "Tree on the %s of level %d has %d events:  %d Signal, %d Background" % (self._side, self._level, self._nEv, self._nSig, self._nBgd)

        if self.left is not None:
            self.left.PrintTree()

        if self.right is not None:
            self.right.PrintTree()

    def CheckTree(self):

        if xor(self.left is None, self.right is None):
            return False

        if self.left is None and self.right is None:
            return True

        return self.left.CheckTree() and self.right.CheckTree()

    def GraphTree(self):

        graph = pydot.Dot(graph_type='digraph')

        PlotNodes = []

        i = 0
        for node in Tree.Objects:
            i += 1

            # If node is a end leaf
            if node.left is None and node.right is None:

                # If its a signal leaf fill blue
                if node._nSig > node._nBgd:
                    PlotNodes.append((pydot.Node("%d, B=%d, S=%d" % (i, node._nBgd, node._nSig), style="filled", fillcolor="blue"), node))
                # Otherwise fill green
                else:
                    PlotNodes.append((pydot.Node("%d, B=%d, S=%d" % (i, node._nBgd, node._nSig), style="filled", fillcolor="green"), node))

            # Otherwise no fill
            PlotNodes.append((pydot.Node("%d, B=%d, S=%d" % (i, node._nBgd, node._nSig)), node))

        #ok, now we add the nodes to the graph
        for gnode in PlotNodes:
            graph.add_node(gnode[0])

        for node in PlotNodes:

            treenode = node[1]
            graphnode1 = node[0]

            # If not a final node
            if treenode.left is not None:

                graphnodeL = None
                graphnodeR = None

                # Loop treenodes to find connecting graph node of left and right treenodes
                for node2 in PlotNodes:
                    if node2[1] is treenode.left:
                        graphnodeL = node2[0]
                    if node2[1] is treenode.right:
                        graphnodeR = node2[0]

                if graphnodeL is None or graphnodeR is None:
                    print "Error finding nodes"
                    exit()
                else:
                    graph.add_edge(pydot.Edge(graphnode1, graphnodeL))
                    graph.add_edge(pydot.Edge(graphnode1, graphnodeR))

        graph.write_png('figs/treegraph.png')