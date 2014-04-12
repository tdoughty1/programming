# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 10:57:59 2014

@author: tdoughty1
"""

from DataRecord import DataRecord
from BookRecord import BookRecord
from TimeRecord import TimeRecord


class TraceRecord(DataRecord):

    def _PrintLine(self):
        print "Found Admin Record"

    def _InitValues(self):
        self._BookRecord = BookRecord()
        self._TimeRecord = TimeRecord()
        self._Trace = None

    def ReadRecord(self, filePtr, RecordLength, debug=False):

        endPos = filePtr.Tell()+RecordLength

        while filePtr.Tell() < endPos:
            TraceHeader = filePtr.ReadWords(4*2)

            # Record of No length
            if TraceHeader[1] == 0:
                continue

            # Bookkeeping Record
            if TraceHeader[0] == 0x11:
                self._BookRecord.ReadRecord(filePtr, TraceHeader[1], debug)
                continue

            # Timebase Record
            if TraceHeader[0] == 0x12:
                self._TimeRecord.ReadRecord(filePtr, TraceHeader[1], debug)
                continue

            if TraceHeader[0] == 0x13:
                nSamples = TraceHeader[1]
                self._Trace = filePtr.ReadWords(nSamples/2*4, 'H')
                continue

            print "Found unexpected trace header"
            exit(1)

    def StoreValues(self, Record):
        pass

    def PrintValues(self):
        pass
