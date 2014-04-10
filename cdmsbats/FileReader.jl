import GZip

gzFile = GZip.open("/home/tdoughty1/Workspace/data/raw/01120411_1132/01120411_1132_F0002.gz","r")

FileHeader = Array(Int32,2)
read(gzFile,FileHeader)

#println(hex(FileHeader[1]))
#println(hex(FileHeader[2]))

DetectorConfigHeader = Array(Int32,2)
read(gzFile,DetectorConfigHeader)

#println(hex(DetectorConfigHeader[1]))
#println(DetectorConfigHeader[2])

pos = position(gzFile)
endpos = pos + DetectorConfigHeader[2]

#println(string("Current Position = ",pos))
#println(string("End of Config Header = ",endpos))

# Read Detector Configuration Record
while pos < endpos

    #println(string("Current Position = ",pos))
    #println(string("End of Config Header = ",endpos))

    ChannelConfigHeader = Array(Int32,2)
    read(gzFile,ChannelConfigHeader)

    if ChannelConfigHeader[1] == 0x10001

        #println(string("Found Phonon Channel (", hex(ChannelConfigHeader[1]), ")"))
        #println(string("Record is ", ChannelConfigHeader[2], " bytes long"))

        PChanConfig = Array(Int32, convert(Int32,ChannelConfigHeader[2]/4))
        read(gzFile,PChanConfig)
        for i = 1:length(PChanConfig)
            #println(PChanConfig[i])
        end

    elseif ChannelConfigHeader[1] == 0x10002

        #println(string("Found Charge Channel (", hex(ChannelConfigHeader[1]), ")"))
        #println(string("Record is ", ChannelConfigHeader[2], " bytes long"))

        QChanConfig = Array(Int32, convert(Int32,ChannelConfigHeader[2]/4))
        read(gzFile,QChanConfig)
        for i = 1:length(QChanConfig)
            #println(QChanConfig[i])
        end

    else
        #println(string("Error Reading Channel Configuration: ", hex(ChannelConfigHeader[1])))
        #println("Unknown Channel Header ID Tag")
        #println("Exiting Program")
        exit(1)
    end

    pos = position(gzFile)
    #println(string("Current Position = ",pos))
end

EventCount = 0

while !eof(gzFile)

    EventHeader = Array(Uint32,2)
    read(gzFile,EventHeader)

    if EventHeader[1]>>16 != 0xa980
        println("ERROR in Reading Event Record")
        println("Bad Event tag, exiting program")
        exit(1)
    end

    EventCount += 1
    println(string("Reading Event ", EventCount))

    #println(string("Event Header Word = 0x", hex(EventHeader[1])))
    #println(string("Event Tag = 0x", hex(EventHeader[1]>>16)))
    #println(string("Event Class = ", hex((EventHeader[1]&0x0000F000)>>3)))
    #println(string("Event Category = ", hex((EventHeader[1]&0x00000F00)>>2)))
    #println(string("Event Type = ", hex(EventHeader[1]&0x000000FF)))
    #println(string("Event Length = ", EventHeader[2]))

    pos = position(gzFile)
    endpos = pos + EventHeader[2]

    while pos < endpos
        LogicHeader = Array(Uint32,2)
        read(gzFile,LogicHeader)
        #println(string("Logic Header = 0x", hex(LogicHeader[1])))
        #println(string("Logic Record Length = ", LogicHeader[2]))

        # Empty Logical Record
        if LogicHeader[2] == 0
            #println(string("Skipping Empty Record for 0x", hex(LogicHeader[1])))
            continue

        # Admin Record
        elseif LogicHeader[1] == 0x02

            AdminRecord = Array(Uint32, convert(Int32,LogicHeader[2]/4))
            read(gzFile,AdminRecord)

            #println(string("SeriesNumber Date = ", AdminRecord[1]))
            #println(string("SeriesNumber Time = ", AdminRecord[2]))
            #println(string("Formatted SeriesNumber = ", AdminRecord[1], "_", AdminRecord[2]))
            #println(string("EventNumber = ", AdminRecord[3]))
            #println(string("EventTime = ", AdminRecord[4]))
            #println(string("Time Since Last Event = ", AdminRecord[5]))
            #println(string("Livetime since Last Event = ", AdminRecord[6]))

        # Trigger Record
        elseif LogicHeader[1] == 0x80
            TriggerRecord = Array(Uint32, convert(Int32,LogicHeader[2]/4))
            read(gzFile,TriggerRecord)

        # TLB Record
        elseif LogicHeader[1] == 0x81
            TLBRecord = Array(Uint32, convert(Int32,LogicHeader[2]/4))
            read(gzFile,TLBRecord)

        # GPS Record
        elseif LogicHeader[1] == 0x60
            GPSRecord = Array(Uint32, convert(Int32,LogicHeader[2]/4))
            read(gzFile,GPSRecord)

        # Trace Record
        elseif LogicHeader[1] == 0x11
            BookHeader = Array(Uint32,2)
            read(gzFile,BookHeader)

            #println(string("Bookkeeping Header = 0x", hex(BookHeader[1])))
            #println(string("Bookkeeping Record Length = ", BookHeader[2]))

            BookRecord = Array(Uint32,convert(Int32,BookHeader[2]/4))
            read(gzFile,BookRecord)

            TimeBaseHeader = Array(Uint32,2)
            read(gzFile,TimeBaseHeader)

            #println(string("TimeBase Header = 0x", hex(TimeBaseHeader[1])))
            #println(string("TimeBase Record Length = ", TimeBaseHeader[2]))

            TimeBaseRecord = Array(Uint32,convert(Int32,TimeBaseHeader[2]/4))
            read(gzFile,TimeBaseRecord)

            TraceHeader = Array(Uint32,2)
            read(gzFile,TraceHeader)

            #println(string("Trace Header = 0x", hex(TraceHeader[1])))
            #println(string("Trace Sample Number = ", TraceHeader[2]))

            TraceRecord = Array(Uint32,convert(Int32,TraceHeader[2]/2))
            read(gzFile,TraceRecord)

        # History Buffer Record
        elseif LogicHeader[1] == 0x21
            HistRecord = Array(Uint32, convert(Int32,LogicHeader[2]/4))
            read(gzFile,HistRecord)

        # Unimplemented Record Type
        else
            println(string("Unimplemented Logic Record Type = 0x", hex(LogicHeader[1])))
            break
        end

        pos = position(gzFile)
    end
end

close(gzFile)
