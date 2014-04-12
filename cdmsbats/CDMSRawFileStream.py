# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 09:52:34 2014

@author: tdoughty1
"""

from numpy import fromstring
from gzip import open as gzopen


class CDMSRawFileStream:

    def __init__(self, fName=None, mode='r'):

        if fName is None:
            self._FileName = None
            self._FileStream = None
            self._Open = False
        else:
            self.Open(fName, mode)

    def Open(self, fName, mode):

        try:
            self._FileStream = gzopen(fName, mode)
            self._FileName = fName
            self._Open = True
        except:
            print "Error opening file %s" % fName

    def Close(self):

        try:
            self._FileStream.close()
            self._FileName = None
            self._Open = False
        except:
            print "Error closing file %s " % self._FileName

    def Tell(self):

        if self._Open:
            return self._FileStream.tell()
        else:
            print "Error returning position, no opened file."

    def Seek(self, nPos):

        if self._Open:
            self._FileStream.seek(nPos, 0)

        else:
            print "Error seeking position, no opened file."

    def Skip(self, nPos):

        if self._Open:
            self._FileStream.seek(nPos, 1)

        else:
            print "Error seeking position, no opened file."

    def ReadWords(self, nBytes, mode='I'):

        if self._Open:
            return fromstring(self._FileStream.read(nBytes), dtype=mode)
