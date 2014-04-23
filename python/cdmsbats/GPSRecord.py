# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 12:14:28 2014

@author: tdoughty1
"""

from DataRecord import DataRecord


class GPSRecord(DataRecord):

    def __init__(self):

        self._Date = None
        self._Time = None
        self._SubTime = None

    def StoreValues(self, Record):

        self._Date = Record[0]
        self._Time = Record[1]
        self._SubTime = Record[2]

    def PrintValues(self):

        print "GPS Date = %d" % self._Date
        print "GPS Time = %d" % self._Time
        print "GPS SubTime = %d" % self._SubTime
