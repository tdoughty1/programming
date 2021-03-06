# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 12:27:34 2014

@author: tdoughty1
"""


class DataRecord:

    # Primary Function Call for data record
    # Responsibility of ReadRecord to return filePtr to starting point
    def ReadRecord(self, filePtr, RecordLength, mode='int32', debug=False):

        Record = filePtr.ReadWords(RecordLength, mode)

        self.StoreValues(Record)

        if debug:
            self.PrintValues()

    # Dummy Function - should be overloaded by Inheriting Classes
    def StoreValues(self, Record):
        pass

    # Dummy Function - should be overloaded by Inheriting Classes
    def PrintValues(self):
        pass
