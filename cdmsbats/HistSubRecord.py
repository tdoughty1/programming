# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 12:27:34 2014

@author: tdoughty1
"""

from numpy import copy

from DataRecord import DataRecord


class HistSubRecord(DataRecord):

    def _InitValues(self):
        self._Masks = []
        self._Times = None

    def _PrintLine(self):
        print "Found History Buffer Sub Record."

    # Primary Function Call for data record
    def ReadRecord(self, Record, index, debug=False):

        # Get number of times stored
        nTimes = Record[index]
        index += 1

        # Store number of times
        start = index + 1
        end = start + nTimes
        self._Times = copy(Record[start:end])
        index += nTimes

        # Get number of masks stored
        nMasks = Record[index]
        index += 1

        # Store all masks for all times
        for i in range(nTimes):
            start = index
            end = start + nMasks
            self._Masks.append(copy(Record[start:end]).astype('uint32'))
            index += nMasks

        if debug:
            self.PrintValues()

        return index

    def StoreValues(self, Record):
        pass

    def PrintValues(self):

        print len(self._Masks)

        nTime = 0
        for time in self._Times:
            nMask = 0
            nTime += 1
            print "time %d = %d" % (nTime, time)
            for mask in self._Masks[nTime-1]:
                nMask += 1
                print "time %d - mask %d = 0x%x" % (nTime, nMask, mask)
