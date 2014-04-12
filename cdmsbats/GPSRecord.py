# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 12:14:28 2014

@author: tdoughty1
"""

from DataRecord import DataRecord


class GPSRecord(DataRecord):

    def _PrintLine(self):
        print "Found GPS Record"

    def _InitValues(self):
        pass

    def StoreValues(self, Record):

        print "Error in GPSRecord:"
        print "Should not reach this point"
        pass

    def PrintValues(self):
        pass
