# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 12:14:28 2014

@author: tdoughty1
"""

from numpy import copy
from DataRecord import DataRecord


class TLBRecord(DataRecord):

    def __init__(self):

        self._TriggerTime = None
        self._TriggerMask = None

    def StoreValues(self, Record):

        self._TriggerTime = Record[0]
        self._TriggerMask = copy(Record[1:7])

    def PrintValues(self):

        print "Trigger Time = %d" % self._TriggerTime
        for i, mask in zip(range(len(self._TriggerMask)), self._TriggerMask):
            print "Tower %d TLB Mask = 0x%x" % (i+1, mask)
