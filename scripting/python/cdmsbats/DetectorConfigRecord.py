# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 12:27:34 2014

@author: tdoughty1
"""

from DataRecord import DataRecord
from PhononChanRecord import PhononChanRecord
from ChargeChanRecord import ChargeChanRecord


class DetectorConfigRecord(DataRecord):

    def __init__(self):

        self._pChanPtr = PhononChanRecord()
        self._qChanPtr = ChargeChanRecord()

    def ReadRecord(self, filePtr, RecordLength, mode='int32', debug=False):

        endPos = filePtr.Tell() + RecordLength
        while filePtr.Tell() < endPos:
            ChanHeader = filePtr.ReadWords(4*2)

            if(debug):
                print "Channel Header = 0x%x" % ChanHeader[0]
                print "Channel Length = %d" % ChanHeader[1]

            # Record of No length
            if ChanHeader[1] == 0:
                continue

            # Phonon Record Record
            if ChanHeader[0] == 0x10001:
                self._pChanPtr.ReadRecord(filePtr, ChanHeader[1], 'int32', debug)
                continue

            # Charge Record
            if ChanHeader[0] == 0x10002:
                self._qChanPtr.ReadRecord(filePtr, ChanHeader[1], 'int32', debug)
                continue

            print "Found unexpected trace header"
            exit(1)

    def PrintValues(self):
        pass
