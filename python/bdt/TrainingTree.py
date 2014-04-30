# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 19:58:28 2014

@author: tdoughty1
"""

import os
import numpy as np
import matplotlib.pylab as plt
from operator import xor
import warnings
import pydot

warnings.filterwarnings("ignore", category=DeprecationWarning, module="pandas")

#from memory_profiler import profile


class TrainingTree(object):

    Counter = 0
    Objects = []

    #@profile
    def __init__(self, df, level=0, debug=False, plots=False, parent=None,
                 side='Top'):

        # Include links to Parent Node and Child Nodes
        self.left = None
        self.right = None
        self.parent = parent

        # Store data and convenient info
        self.df = df
        self._nEv = len(df)
        self._cSig = df['Class'] == 1
        self._cBgd = df['Class'] == 0
        self._nSig = sum(self._cSig)
        self._nBgd = sum(self._cBgd)

        # Store Tree Info
        self._level = level
        self._side = side
        self._num = TrainingTree.Counter

        # Add to Tree Class Counter
        TrainingTree.Counter += 1
        TrainingTree.Objects.append(self)

        # Store Purity/Gini Information
        self._Purity = float(self._nSig)/(self._nSig+self._nBgd)
        self._Gini = self._Purity*(1-self._Purity)
        self._Info = self._nEv*self._Gini

        # If not the root node, store changes
        if self.parent is not None:
            self._PurityGain = self._Purity - self.parent._Purity
            self._GiniGain = self.parent._Gini - self._Gini
            self._InfoGain = self.parent._Info - self._Info
        else:
            self._PurityGain = None
            self._GiniGain = None
            self._InfoGain = None

        if self._nSig > 0 and self._nBgd > 0:

            cutSet = self.FindCut(plots=plots, debug=debug)
            cc = df[cutSet[0]] < cutSet[1]

            if debug:
                print 'Returned Cut %s = %f' % (cutSet)
                print "Filling Left Tree with %d events" % sum(cc)
                print "Filling Right Tree with %d events" % sum(~cc)

            self.left = TrainingTree(self.df[cc], level=self._level,
                                     parent=self, debug=debug, plots=plots,
                                     side='left')
            self.right = TrainingTree(self.df[~cc], level=self._level,
                                      parent=self, debug=debug, plots=plots,
                                      side='right')

    #@profile
    def FindCut(self, plots=False, debug=False):

        Var_Cut = ''
        Val_Cut = -999999
        SeperationGain = 0

        if self._nEv >= 100:
            n = 100
        elif self._nEv >= 50:
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

                if plots and TrainingTree.Counter == 1:
                    self.PlotCuts(var, val, cutVals, cutVal, SG, i)

                if val > SeperationGain:
                    SeperationGain = val
                    Var_Cut = var
                    Val_Cut = cutVal

            if plots and TrainingTree.Counter == 1:
                self.PlotBestCuts(var, val, cutVals, SG)

        cutSet = (Var_Cut, Val_Cut)
        if debug:
            print "Returning Cut %s = %f" % cutSet
        return cutSet

    #@profile
    def CountNodes(self):

        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.CountNodes() + 1
        elif self.right is None:
            return self.left.CountNodes() + 1
        else:
            return self.left.CountNodes() + self.right.CountNodes() + 1

    #@profile
    def PrintTree(self):

        if self._level == 1:
            print "Root Tree has %d events: %d Signal, %d Background" \
                % (self._nEv, self._nSig, self._nBgd)
        else:
            print "Tree on the %s of level %d has %d events:  %d Signal, " \
                "%d Background" % (self._side, self._level, self._nEv,
                                   self._nSig, self._nBgd)

        if self.left is not None:
            self.left.PrintTree()

        if self.right is not None:
            self.right.PrintTree()

    #@profile
    def CheckTree(self):

        if xor(self.left is None, self.right is None):
            return False

        if self.left is None and self.right is None:
            return True

        return self.left.CheckTree() and self.right.CheckTree()

    #@profile
    def GraphTree(self, n):

        graph = pydot.Dot(graph_type='digraph')

        PlotNodes = []

        for node in TrainingTree.Objects:

            # If node is a end leaf
            if node.left is None and node.right is None:

                # If its a signal leaf fill blue
                if node._nSig > node._nBgd:
                    PlotNodes.append((pydot.Node("%d, B=%d, S=%d" %
                                                 (node._num, node._nBgd,
                                                  node._nSig),
                                                 style="filled",
                                                 fillcolor="blue"), node))
                # If node its a background leaf fill blue
                elif node._nSig < node._nBgd:
                    PlotNodes.append((pydot.Node("%d, B=%d, S=%d" %
                                                 (node._num, node._nBgd,
                                                  node._nSig),
                                                 style="filled",
                                                 fillcolor="green"), node))
                # If node its an unknown leaf fill red
                elif node._nSig == node._nBgd:
                    PlotNodes.append((pydot.Node("%d, B=%d, S=%d" %
                                                 (node._num, node._nBgd,
                                                  node._nSig),
                                                 style="filled",
                                                 fillcolor="red"), node))
            # Otherwise no fill
            PlotNodes.append((pydot.Node("%d, B=%d, S=%d" %
                                         (node._num, node._nBgd, node._nSig)),
                              node))

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

                # Loop treenodes to find connecting graph nodes (L & R)
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

        graph.write_png('figs/treegraph%d.png' % n)

    #@profile
    def PlotCuts(self, var, val, cutVals, cutVal, SG, i):

        f, axarr = plt.subplots(2, sharex=True)
        f.set_size_inches((4, 5))
        bs = axarr[0].scatter(self.df[var][self._cSig],
                              self.df['Rand'][self._cSig],
                              color='b', marker='.')
        gs = axarr[0].scatter(self.df[var][self._cBgd],
                              self.df['Rand'][self._cBgd],
                              color='g', marker='.')
        axarr[0].set_xlim(min(cutVals), max(cutVals))
        axarr[0].set_ylim([0, 1.5])
        xax = axarr[0].get_xlim()
        rl, = axarr[0].plot([cutVal]*2, [0, 1.5], 'r-')
        axarr[0].set_title('Cutting on %s\nSeperation Gain = %.2f' % (var,
                                                                      val))
        axarr[0].set_ylabel('Random Variable')
        axarr[0].legend((bs, gs, rl), ('Signal', 'Background', 'Current Cut'),
                        loc=1, fontsize='small')

        axarr[1].plot(cutVals[0:len(SG)], SG, 'r-')
        axarr[1].set_xlim(xax)
        axarr[1].set_ylabel('Seperation Gain')
        axarr[1].set_xlabel(var)

        f.savefig('animation/%s_%02d.png' % (var, i))
        plt.close()

    #@profile
    def PlotBestCuts(self, var, val, cutVals, SG):

        f, axarr = plt.subplots(2, sharex=True)
        f.set_size_inches((8, 10))
        bs = axarr[0].scatter(self.df[var][self._cSig],
                              self.df['Rand'][self._cSig],
                              color='b', marker='.')
        gs = axarr[0].scatter(self.df[var][self._cBgd],
                              self.df['Rand'][self._cBgd],
                              color='g', marker='.')
        axarr[0].set_xlim(min(cutVals), max(cutVals))
        axarr[0].set_ylim([0, 1.5])
        xax = axarr[0].get_xlim()
        rl, = axarr[0].plot([cutVals[np.argmax(SG)]]*2, [0, 1.5],
                            'r-', label='Best Cut')
        axarr[0].set_title('Cutting on %s\nSeperation Gain = %.2f'
                           % (var, max(SG)))
        axarr[0].set_ylabel('Random Variable')
        axarr[0].legend((bs, gs, rl), ('Signal', 'Background', 'Best Cut'),
                        loc=1, fontsize='small')

        axarr[1].plot(cutVals, SG, 'r-')
        axarr[1].set_xlim(xax)
        axarr[1].set_ylabel('Seperation Gain')
        axarr[1].set_xlabel(var)

        f.savefig('figs/%s.png' % var)
        plt.close()

    #@profile
    def AnimateCuts(self):

        folder = 'animation'

        for col in self.df.columns:

            if col == 'Rand' or col == 'Class':
                continue

            print col
            print folder

            print "Creating animation animation/%s.gif" % col
            os.system('convert -delay 10 -loop 0 %s/%s*.png %s/%s.gif'
                      % (folder, col, folder, col))
            os.system('rm %s/%s*.png' % (folder, col))
            os.system('convert %s/%s.gif -fuzz 30%% -layers Optimize %s/%s.gif'
                      % (folder, col, folder, col))

    #@profile
    def PruneTree(self):

        diff = 5

        # Base Case should be parent node to 2 leaves
        if(self.left.left is None and self.left.right is None and
           self.right.left is None and self.right.right is None):

            ptree = self
            ltree = self.left
            rtree = self.right

            #print "Leaf is Node #", ltree._num
            #print "Leaf is Node #", rtree._num
            #print "Total Information Gain = %.2f" % (ltree._InfoGain + rtree._InfoGain)

            #If IG from both nodes is less than diff, remove both base nodes
            if ltree._InfoGain + rtree._InfoGain < diff:
                #print "Pruning Tree #%d & #%d" % (ltree._num, rtree._num)
                Tree.Objects.remove(ltree)
                Tree.Objects.remove(rtree)
                ptree.left = None
                ptree.right = None
                return True
            else:
                return False

        # Otherwise, move down tree, only if node is not a leaf
        else:
            LP = False
            RP = False

            if self.left.left is not None and self.left.right is not None:
                LP = self.left.PruneTree()

            if self.right.left is not None and self.right.right is not None:
                RP = self.right.PruneTree()

            return (LP or RP)

    def ScoreTree(self):

        # Base case is leaf
        if self.left is None and self.right is None:
            if self._nBgd > self._nSig:
                return (self._nBgd, self._nSig)
            elif self._nSig > self._nBgd:
                return (self._nSig, self._nBgd)
            else:
                return (0, self._nEv)

        # Otherwise Score SubTrees and add
        else:
            score_left = self.left.ScoreTree()
            score_right = self.right.ScoreTree()

            return (score_left[0] + score_right[0],
                    score_left[1] + score_right[1])
