# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 12:14:28 2014

@author: tdoughty1
"""

from DataRecord import DataRecord


class ChargeChanRecord(DataRecord):

    def __init__(self):

        self._detCode = None
        self._towerNum = None
        self._driverGain = None
        self._chanBias = None
        self._rtfOffset = None
        self._deltat = None
        self._t0 = None
        self._traceLength = None

    def StoreValues(self, Record):

        self._detCode = Record[0]
        self._towerNum = Record[1]
        self._driverGain = float(Record[2])/100
        self._chanBias = float(Record[3])/1e6
        self._rtfOffset = float(Record[4])/1e6
        self._deltat = float(Record[5])/1000
        self._t0 = float(Record[6])/1000
        self._traceLength = Record[7]

    def PrintValues(self):

        print "Detector Code = %d" % self._detCode
        print "Tower Number = %d" % self._towerNum
        print "Driver Gain = %3.1f" % self._driverGain
        print "Channel Bias = %5.3f V" % self._chanBias
        print "RTF Offset = %5.3f V" % self._rtfOffset
        print "Delta T = %4.2f us" % self._deltat
        print "t0 = %5.1f us" % self._t0
        print "Trace Length = %d" % self._traceLength
