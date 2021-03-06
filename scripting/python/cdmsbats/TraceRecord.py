# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 10:57:59 2014

@author: tdoughty1
"""

from DataRecord import DataRecord
from BookRecord import BookRecord
from TimeRecord import TimeRecord


class TraceRecord(DataRecord):

    def __init__(self):

        self._BookPtr = BookRecord()
        self._TimePtr = TimeRecord()
        self._Trace = None

    def ReadRecord(self, filePtr, RecordLength, mode='uint32', debug=False):

        endPos = filePtr.Tell() + RecordLength

        while filePtr.Tell() < endPos:
            TraceHeader = filePtr.ReadWords(4*2)

            if debug:
                print "Trace Header = 0x%x" % TraceHeader[0]
                print "Trace Length Value = %d" % TraceHeader[1]

            # Record of No length
            if TraceHeader[1] == 0:
                continue

            # Bookkeeping Record
            if TraceHeader[0] == 0x11:
                self._BookPtr.ReadRecord(filePtr, TraceHeader[1], mode, debug)
                continue

            # Timebase Record
            if TraceHeader[0] == 0x12:
                self._TimePtr.ReadRecord(filePtr, TraceHeader[1], mode, debug)
                continue

            if TraceHeader[0] == 0x13:
                nSamples = TraceHeader[1]
                self._Trace = filePtr.ReadWords(nSamples/2*4, 'H')

                if debug:
                    print "First Element of Trace = %d" % self._Trace[0]
                    print "Second Element of Trace = %d" % self._Trace[1]

                continue

            print "Found unexpected trace header"
            exit(1)

    def StoreValues(self, Record):
        pass

    def PrintValues(self):
        pass
