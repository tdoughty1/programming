# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 10:57:59 2014

@author: tdoughty1
"""

from numpy import copy
from DataRecord import DataRecord


class HistoryRecord(DataRecord):

    def _PrintLine(self):
        print "Found History Record"

    def _InitValues(self):
        self._VetoTimes = None
        self._VetoMasks = []
        self._TrigTimes = None
        self._TrigMasks = []

    def StoreValues(self, Record):
        print "Record Length = %d" % len(Record)
        # Read Number of Veto Times
        ind = 0
        nVetoTimes = Record[ind]
        ind += 1
        print "Number of Veto Times = %d" % nVetoTimes
        print "Index after reading number of Veto Times = %d" % ind

        # Read Veto Times
        start = ind
        end = ind + nVetoTimes
        self._VetoTimes = copy(Record[start:end])
        ind += nVetoTimes
        print "Index after reading Veto Times = %d" % ind

        # Read Number of Veto Masks for each Veto Time
        nVetoMasks = Record[ind]
        ind += 1
        print "Number of Veto Masks = %d" % nVetoMasks
        print "Index after reading number of Veto Masks = %d" % ind

        # Read Veto Masks for each Veto Time
        for i in range(nVetoTimes):
            start = ind + i*nVetoMasks
            end = start + nVetoMasks
            self._VetoMasks.append(copy(Record[start:end]))
            ind += nVetoMasks
        print "Index after Reading Veto Masks = %d" % ind

        # Read Number of Trigger Times
        nTrigTimes = Record[ind]
        ind += 1
        print "Number of Trigger Times = %d" % nTrigTimes
        print "Index after reading number of Trigger Times = %d" % ind

        # Read Trigger Times
        start = ind
        end = ind + nTrigTimes
        self._TrigTimes = copy(Record[start:end])
        ind += nTrigTimes
        print "Index after Reading Trigger Times = %d" % ind

        # Read Number of Trigger Masks for each Trigger Time
        nTrigMasks = Record[ind]
        ind += 1
        print "Number of Trigger Masks = %d" % nTrigMasks
        print "Index after reading number of Trigger Masks = %d" % ind

        # Read Trigger Masks for each Trigger Time
        for i in range(nTrigTimes):
            start = ind + i*nTrigMasks
            end = start + nVetoMasks
            self._TrigMasks.append(copy(Record[start:end]))
            ind += nTrigMasks
        print "Index after reading Trigger Times = %d" % ind

        if ind != len(Record):
            print "Error reading History Buffer"
            print "History record format is not in correct mode"

    def PrintValues(self):
        pass
