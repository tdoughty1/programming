# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 20:11:33 2014

@author: tdoughty1
"""

from datetime import datetime
from CDMSRawFileStream import CDMSRawFileStream
from DetectorConfigRecord import DetectorConfigRecord
from EventRecord import EventRecord

###############################################################################
# Instantiate Reader Objects
###############################################################################
DetectorConfigPtr = DetectorConfigRecord()
EventPtr = EventRecord()

fName = '/home/tdoughty1/Workspace/data/raw/01120411_1132/01120411_1132_F0003.gz'
debug = True

startTime = datetime.now()

fgzRawDataPtr = CDMSRawFileStream(fName)

FileHeader = fgzRawDataPtr.ReadWords(4*2, 'int32')

if debug:
    print "Endian Check = 0x%x" % FileHeader[0]
    print "File Header = 0x%x" % FileHeader[1]

###############################################################################
# Read Detector Config Record
###############################################################################
ConfigHeader = fgzRawDataPtr.ReadWords(4*2)

if debug:
    print "Config Header = 0x%x" % ConfigHeader[0]
    print "Config Record Length = %d" % ConfigHeader[1]

DetectorConfigPtr.ReadRecord(fgzRawDataPtr, ConfigHeader[1], 'uint32', debug)

###############################################################################
# Loop through Events
###############################################################################

nEvent = 0
while nEvent < 500:

    EventHeader = fgzRawDataPtr.ReadWords(4*2, 'uint32')
    nEvent += 1

    if debug:
        print "Loading Event Number %d" % nEvent
        print "Event Header = 0x%x" % EventHeader[0]
        print "Event Record Length = %d" % EventHeader[1]

    EventPtr.ReadRecord(fgzRawDataPtr, EventHeader[1], 'int32', debug)

endTime = datetime.now()

timeDiff = endTime-startTime

print "Loading File took %d.%d s" % (timeDiff.seconds, timeDiff.microseconds)

fgzRawDataPtr.Close()
