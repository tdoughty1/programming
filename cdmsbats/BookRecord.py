# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 10:57:59 2014

@author: tdoughty1
"""

from DataRecord import DataRecord


class BookRecord(DataRecord):

    def __init__(self):

        self._digBaseAddress = None
        self._digChannel = None
        self._detCode = None

    def StoreValues(self, Record):

        self._digBaseAddress = Record[0]
        self._digChannel = Record[1]
        self._detCode = Record[2]

    def PrintValues(self):

        print "Digitizer Base Address = 0x%x" % self._digBaseAddress
        print "Digitizer Channel = %d" % self._digChannel
        print "Detector Code = %d" % self._detCode
