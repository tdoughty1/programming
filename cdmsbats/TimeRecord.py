# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 10:57:59 2014

@author: tdoughty1
"""

import ctypes
from DataRecord import DataRecord


class TimeRecord(DataRecord):

    def __init__(self):

        self._t0 = None
        self._deltat = None
        self._N = None

    def StoreValues(self, Record):

        self._t0 = ctypes.c_int32(Record[0]).value
        self._deltat = Record[1]
        self._N = Record[2]

    def PrintValues(self):

        print "t0 = %6.2f us" % (float(self._t0)/1000)
        print u'\u0394t =  %3.2f us' % (float(self._deltat)/1000)
        print "Number of Points = %d" % self._N
