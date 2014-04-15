# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 10:57:59 2014

@author: tdoughty1
"""

from DataRecord import DataRecord
from AdminRecord import AdminRecord
from TriggerRecord import TriggerRecord
from TLBRecord import TLBRecord
from GPSRecord import GPSRecord
from TraceRecord import TraceRecord
from HistoryRecord import HistoryRecord


class EventRecord(DataRecord):

    def _PrintLine(self):
        print "Found Admin Record"

    def _InitValues(self):
        self._AdminPtr = AdminRecord()
        self._TriggerPtr = TriggerRecord()
        self._TLBPtr = TLBRecord()
        self._GPSPtr = GPSRecord()
        self._TracePtr = TraceRecord()
        self._HistoryPtr = HistoryRecord()

    def ReadRecord(self, filePtr, RecordLength, mode='uint32', debug=False):

        endPos = filePtr.Tell() + RecordLength

        while filePtr.Tell() < endPos:

            LogicalHeader = filePtr.ReadWords(4*2)

            if debug:
                print "Logical Header = 0x%x" % LogicalHeader[0]
                print "Logical Record Length = %d" % LogicalHeader[1]

            if LogicalHeader[1] == 0:
                #print "Skipping Empty Record 0x%x" % LogicalHeader[0]
                continue

            if LogicalHeader[0] == 0x2:
                self._AdminPtr.ReadRecord(filePtr, LogicalHeader[1], debug=debug)
                continue

            if LogicalHeader[0] == 0x80:
                self._TriggerPtr.ReadRecord(filePtr, LogicalHeader[1], debug=debug)
                continue

            if LogicalHeader[0] == 0x81:
                self._TLBPtr.ReadRecord(filePtr, LogicalHeader[1], debug=debug)
                continue

            if LogicalHeader[0] == 0x60:
                self._GPSPtr.ReadRecord(filePtr, LogicalHeader[1], debug=debug)
                continue

            if LogicalHeader[0] == 0x11:
                self._TracePtr.ReadRecord(filePtr, LogicalHeader[1], debug=debug)
                continue

            if LogicalHeader[0] == 0x21:
                self._HistoryPtr.ReadRecord(filePtr, LogicalHeader[1], debug=debug)
                continue

            print "Found Unimplemented Record Type 0x%x" % LogicalHeader[0]
            break

    def StoreValues(self, Record):
        pass

    def PrintValues(self):
        pass
