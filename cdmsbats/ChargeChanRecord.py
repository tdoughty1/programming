# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 12:14:28 2014

@author: tdoughty1
"""

from DataRecord import DataRecord


class ChargeChanRecord(DataRecord):

    def _PrintLine(self):
        print "Found Charge Channel Record"

    def _InitValues(self):

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
        self._chanBias = Record[3]
        self._rtfOffset = Record[4]
        self._deltat = Record[5]
        self._t0 = Record[6]
        self._traceLength = Record[7]

    def PrintValues(self):

        print "Detector Code = %d" % self._detCode
        print "Tower Number = %d" % self._towerNum
        print "Driver Gain = %d" % self._driverGain
        print "Channel Bias = %5.3f V" % (float(self._chanBias)/1e6)
        print "RTF Offset = %5.3f V" % (float(self._rtfOffset)/1e6)
        print "Delta T = %4.2f us" % (float(self._deltat)/1000)
        print "t0 = %5.1f us" % (float(self._t0)/1000)
        print "Trace Length = %d" % self._traceLength
