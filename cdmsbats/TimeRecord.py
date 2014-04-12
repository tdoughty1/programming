# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 10:57:59 2014

@author: tdoughty1
"""

from DataRecord import DataRecord


class TimeRecord(DataRecord):

    def _PrintLine(self):
        print "Found Time Record"

    def _InitValues(self):
        self._t0 = None
        self._deltat = None
        self._N = None

    def StoreValues(self, Record):
        self._t0 = Record[0]
        self._deltat = Record[1]
        self._N = Record[2]

    def PrintValues(self):
        print "t0 = %d" % self._t0
        print u'\u0394t =  %d' % self._deltat
        print "Number of Points = %d" % self._N
