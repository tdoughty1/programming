# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 20:11:33 2014

@author: tdoughty1
"""

from datetime import datetime
from CDMSRawFileStream import CDMSRawFileStream
from AdminRecord import AdminRecord
from TriggerRecord import TriggerRecord
from TLBRecord import TLBRecord
from GPSRecord import GPSRecord
from TraceRecord import TraceRecord
from HistoryRecord import HistoryRecord


fName = '/home/tdoughty1/Workspace/data/raw/01120411_1132/01120411_1132_F0003.gz'

startTime = datetime.now()

fgzRawDataPtr = CDMSRawFileStream(fName)


FileHeader = fgzRawDataPtr.ReadWords(4*2)

#print "Endian Check = 0x%x" % FileHeader[0]
#print "File Header = 0x%x" % FileHeader[1]

ConfigHeader = fgzRawDataPtr.ReadWords(4*2)

#print "Config Header = 0x%x" % ConfigHeader[0]
#print "Config Record Length = %d" % ConfigHeader[1]

pos = fgzRawDataPtr.Tell()
Endpos = pos + ConfigHeader[1]

###############################################################################
# Loop through Detector Config Record
###############################################################################
while fgzRawDataPtr.Tell() < Endpos:

    ChannelHeader = fgzRawDataPtr.ReadWords(4*2)

    #print "Channel Header = " + hex(ChannelHeader[0])
    #print "Channel Record Length = " + str(ChannelHeader[1])
    ChanRecord = fgzRawDataPtr.ReadWords(ChannelHeader[1])

    if ChannelHeader[0] == 0x10001:
        #print "Found Phonon Channel"
        continue

    if ChannelHeader[0] == 0x10002:
        #print "Found Charge Channel"
        continue

    print "Found Unknown Channel Type"
    break

###############################################################################
# Instantiate Reader Objects
###############################################################################
AdminPtr = AdminRecord()
TriggerPtr = TriggerRecord()
TLBPtr = TLBRecord()
GPSPtr = GPSRecord()
TracePtr = TraceRecord()
HistoryPtr = HistoryRecord()

###############################################################################
# Loop through Events
###############################################################################
nEvent = 0
while nEvent < 400:

    EventHeader = fgzRawDataPtr.ReadWords(4*2)
    nEvent += 1

    #print "Loading Event Number ", nEvent
    #print "Event Header = 0x%x" % EventHeader[0]
    #print "Event Record Length = %d" % EventHeader[1]

    ###########################################################################
    # Loop through Records in Event
    ###########################################################################
    pos = fgzRawDataPtr.Tell()
    Endpos = pos + EventHeader[1]

    while fgzRawDataPtr.Tell() < Endpos:

        startTime1 = datetime.now()

        LogicalHeader = fgzRawDataPtr.ReadWords(4*2)

        #print "Logical Header = 0x%x" % LogicalHeader[0]
        #print "Logical Record Length = %d" % LogicalHeader[1]

        if LogicalHeader[1] == 0:
            #print "Skipping Empty Record 0x%x" % LogicalHeader[0]
            continue

        if LogicalHeader[0] == 0x2:
            AdminPtr.ReadRecord(fgzRawDataPtr, LogicalHeader[1])
            continue

        if LogicalHeader[0] == 0x80:
            TriggerPtr.ReadRecord(fgzRawDataPtr, LogicalHeader[1])
            continue

        if LogicalHeader[0] == 0x81:
            TLBPtr.ReadRecord(fgzRawDataPtr, LogicalHeader[1])
            continue

        if LogicalHeader[0] == 0x60:
            GPSPtr.ReadRecord(fgzRawDataPtr, LogicalHeader[1])
            continue

        if LogicalHeader[0] == 0x11:
            TracePtr.ReadRecord(fgzRawDataPtr, LogicalHeader[1])
            continue

        if LogicalHeader[0] == 0x21:
            HistoryPtr.ReadRecord(fgzRawDataPtr, LogicalHeader[1])
            continue

        print "Found Unimplemented Record Type 0x%x" % LogicalHeader[0]
        break

endTime = datetime.now()

timeDiff = endTime-startTime

print "Loading File took %d.%d s" % (timeDiff.seconds, timeDiff.microseconds)

fgzRawDataPtr.Close()
