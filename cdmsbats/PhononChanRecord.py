# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 12:14:28 2014

@author: tdoughty1
"""

from DataRecord import DataRecord


class PhononChanRecord(DataRecord):

    def _PrintLine(self):
        print "Found Phonon Channel Record"

    def _InitValues(self):

        self._detCode = None
        self._towerNum = None
        self._driverGain = None
        self._qetBias = None
        self._squidBias = None
        self._lockPoint = None
        self._rtfOffset = None
        self._varGain = None
        self._deltat = None
        self._t0 = None
        self._traceLength = None

    def StoreValues(self, Record):

        self._detCode = Record[0]
        self._towerNum = Record[1]
        self._driverGain = float(Record[2])/100
        self._qetBias = float(Record[3])/100
        self._squidBias = float(Record[4])/100
        self._lockPoint = float(Record[5])/100
        self._rtfOffset = float(Record[6])/1e6
        self._varGain = Record[7]
        self._deltat = float(Record[8])/1000
        self._t0 = float(Record[9])/1000
        self._traceLength = Record[10]

    def PrintValues(self):

        print "Detector Code = %d" % self._detCode
        print "Tower Number = %d" % self._towerNum
        print "Driver Gain = %d" % self._driverGain
        print "QET Bias = %6.2f pA" % self._qetBias
        print "SQUID Bias = %6.2f pA" % self._squidBias
        print "SQUID Lock Point = %4.2f uV" % self._lockPoint
        print "RTF Offset = %4.2f V" % self._rtfOffset
        print "Variable Gain = %d" % self._varGain
        print "Delta T = %4.2f us" % self._deltat
        print "t0 = %5.1f us" % self._t0
        print "Trace Length = %d" % self._traceLength
