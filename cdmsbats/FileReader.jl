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

while !eof(gzFile)

    EventHeader = Array(Uint32,2)
    read(gzFile,EventHeader)

    if EventHeader[1]>>16 != 0xa980
        println("ERROR in Reading Event Record")
        println("Bad Event tag, exiting program")
        exit(1)
    end

    println(string("Event Header Word = 0x", hex(EventHeader[1])))
    println(string("Event Tag = 0x", hex(EventHeader[1]>>16)))
    println(string("Event Class = ", hex((EventHeader[1]&0x0000F000)>>3)))
    println(string("Event Category = ", hex((EventHeader[1]&0x00000F00)>>2)))
    println(string("Event Type = ", hex(EventHeader[1]&0x000000FF)))
    println(string("Event Length = ", EventHeader[2]))

    pos = position(gzFile)
    endpos = pos + EventHeader[2]

    while pos < endpos
        LogicHeader = Array(Uint32,2)
        read(gzFile,LogicHeader)
        println(string("Logic Header = 0x", hex(LogicHeader[1])))
        println(string("Logic Record Length = ", LogicHeader[2]))

        # Admin Record
        if LogicHeader[1] == 0x02

            AdminRecord = Array(Uint32, convert(Int32,LogicHeader[2]/4))
            read(gzFile,AdminRecord)

            println(string("SeriesNumber Date = ", AdminRecord[1]))
            println(string("SeriesNumber Time = ", AdminRecord[2]))
            println(string("Formatted SeriesNumber = ", AdminRecord[1], "_", AdminRecord[2]))
            println(string("EventNumber = ", AdminRecord[3]))
            println(string("EventTime = ", AdminRecord[4]))
            println(string("Time Since Last Event = ", AdminRecord[5]))
            println(string("Livetime since Last Event = ", AdminRecord[6]))
        end

       break
    end


    break
end

close(gzFile)
