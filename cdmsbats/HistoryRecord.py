# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 10:57:59 2014

@author: tdoughty1
"""

from DataRecord import DataRecord


class HistoryRecord(DataRecord):

    def _PrintLine(self):
        print "Found History Record"

    def _InitValues(self):
        pass

    def StoreValues(self, Record):
        #print "Warning in History Record:"
        #print "Still need to implement logic."
        pass

    def PrintValues(self):
        pass
