# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 10:57:59 2014

@author: tdoughty1
"""

from DataRecord import DataRecord
from HistSubRecord import HistSubRecord


class HistoryRecord(DataRecord):

    def __init__(self):

        self._VetoPtr = HistSubRecord()
        self._TrigPtr = HistSubRecord()

    def StoreValues(self, Record):

        index = self._VetoPtr.ReadRecord(Record, 0)
        index = self._TrigPtr.ReadRecord(Record, index)

    def PrintValues(self):

        self._VetoPtr.PrintValues()
        self._TrigPtr.PrintValues()
