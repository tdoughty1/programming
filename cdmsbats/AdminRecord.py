# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 10:57:59 2014

@author: tdoughty1
"""

from DataRecord import DataRecord


class AdminRecord(DataRecord):

    def _PrintLine(self):
        print "Found Admin Record"

    def _InitValues(self):
        self._SeriesNumber = None
        self._EventNumber = None
        self._EventTime = None
        self._LiveTime = None
        self._TimeSince = None

    def StoreValues(self, Record):

        self._SeriesNumber = Record[0]*10**4 + Record[1]
        self._EventNumber = Record[2]
        self._EventTime = Record[3]
        self._LiveTime = Record[4]
        self._TimeSince = Record[5]

    def PrintValues(self):
        print "SeriesNumber = %d" % self._SeriesNumber
        print "EventNumber = %d" % self._EventNumber
        print "EventTime = %d" % self._EventTime
        print "LiveTime = %d" % self._LiveTime
        print "TimeSince = %d" % self._TimeSince
