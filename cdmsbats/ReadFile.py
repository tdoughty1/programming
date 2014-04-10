# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 20:11:33 2014

@author: tdoughty1
"""

from numpy import fromstring
import gzip


fName = '/home/tdoughty1/Workspace/data/raw/01120411_1132/01120411_1132_F0003.gz'

fgzRawDataPtr = gzip.open(fName)

FileHeader = fromstring(fgzRawDataPtr.read(4*2), dtype='I')

#print "Endian Check = 0x%x" % FileHeader[0]
#print "File Header = 0x%x" % FileHeader[1]

ConfigHeader = fromstring(fgzRawDataPtr.read(4*2), dtype='I')

#print "Config Header = 0x%x" % ConfigHeader[0]
#print "Config Record Length = %d" % ConfigHeader[1]

pos = fgzRawDataPtr.tell()
Endpos = pos + ConfigHeader[1]

###############################################################################
# Loop through Detector Config Record
###############################################################################
while fgzRawDataPtr.tell() < Endpos:

    ChannelHeader = fromstring(fgzRawDataPtr.read(4*2), dtype='I')

    #print "Channel Header = " + hex(ChannelHeader[0])
    #print "Channel Record Length = " + str(ChannelHeader[1])

    if ChannelHeader[0] == 0x10001:
        #print "Found Phonon Channel"
        PhononRecord = fromstring(fgzRawDataPtr.read(ChannelHeader[1]), dtype='I')
        continue

    if ChannelHeader[0] == 0x10002:
        #print "Found Charge Channel"
        ChargeRecord = fromstring(fgzRawDataPtr.read(ChannelHeader[1]), dtype='I')
        continue

    break

###############################################################################
# Loop through Events
###############################################################################
eof = False

while not eof:

    try:
        EventHeader = fromstring(fgzRawDataPtr.read(4*2), dtype='I')
    except:
        found = True

    if eof:
        continue

    #print "Event Header = 0x%x" % EventHeader[0]
    #print "Event Record Length = %d" % EventHeader[1]

    ###########################################################################
    # Loop through Records in Event
    ###########################################################################
    pos = fgzRawDataPtr.tell()
    Endpos = pos + EventHeader[1]

    while fgzRawDataPtr.tell() < Endpos:

        LogicalHeader = fromstring(fgzRawDataPtr.read(4*2), dtype='I')

        #print "Logical Header = 0x%x" % LogicalHeader[0]
        #print "Logical Record Length = %d" % LogicalHeader[1]

        if LogicalHeader[1] == 0:
            #print "Skipping Empty Record"
            continue

        if LogicalHeader[0] == 0x2:
            #print "Found Admin Record"
            AdminRecord = fromstring(fgzRawDataPtr.read(LogicalHeader[1]), dtype='I')
            continue

        if LogicalHeader[0] == 0x80:
            #print "Found Trigger Record"
            TriggerRecord = fromstring(fgzRawDataPtr.read(LogicalHeader[1]), dtype='I')
            continue

        if LogicalHeader[0] == 0x81:
            #print "Found TLB Trigger Record"
            TLBRecord = fromstring(fgzRawDataPtr.read(LogicalHeader[1]), dtype='I')
            continue

        if LogicalHeader[0] == 0x60:
            #print "Found GPS Record"
            GPSRecord = fromstring(fgzRawDataPtr.read(LogicalHeader[1]), dtype='I')
            continue

        if LogicalHeader[0] == 0x11:
            #print "Found Trace Record"

            BookHeader = fromstring(fgzRawDataPtr.read(4*2), dtype='I')
            #print "Bookkeeping Header = 0x%x" % BookHeader[0]
            #print "Bookkeeping Record Length = %d" % BookHeader[1]

            BookRecord = fromstring(fgzRawDataPtr.read(BookHeader[1]), dtype='I')

            TimeBaseHeader = fromstring(fgzRawDataPtr.read(4*2), dtype='I')
            #print "Timebase Header = 0x%x" % TimeBaseHeader[0]
            #print "Timebase Record Length = %d" % TimeBaseHeader[1]

            TimeBaseRecord = fromstring(fgzRawDataPtr.read(TimeBaseHeader[1]), dtype='I')

            TraceHeader = fromstring(fgzRawDataPtr.read(4*2), dtype='I')
            #print "Trace Header = 0x%x" % TraceHeader[0]
            #print "Trace Sample Number = %d" % TraceHeader[1]

            TraceRecord = fromstring(fgzRawDataPtr.read(TraceHeader[1]*2), dtype='I')
            continue

        if LogicalHeader[0] == 0x21:
            #print "Found History Buffer Record"
            HistRecord = fromstring(fgzRawDataPtr.read(LogicalHeader[1]), dtype='I')
            continue

        print "Found Unimplemented Record Type 0x%x" % LogicalHeader[0]
        break
