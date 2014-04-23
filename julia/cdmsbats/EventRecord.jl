type EventRecord

    _AdminPtr::AdminRecord
    _TriggerPtr::TriggerRecord
    _TLBPtr::TLBRecord
    _GPSPtr::GPSRecord
    _TracePtr::TraceRecord
    _HistoryPtr::HistoryRecord

    EventRecord() = new(new AdminRecord(), new TriggerRecord(), new TLBRecord(), new GPSRecord(), new TraceRecord(), new HistoryRecord())

end

ReadRecord(recPtr::EventRecord, filePtr::CDMSRawFileStream, RecordLength::Int, debug::Bool)

    endPos = Tell(filePtr) + RecordLength

    while(Tell(filePtr) < endPos)

        LogicalHeader = Array(Int32,2)
        ReadWords(filePtr, 2*4, LogicalHeader);

        if(debug)
            @printf("Logical Header = 0x%x\n", LogicalHeader[0])
            @printf("Logical Record Length = %d\n", LogicalHeader[1])
        end

        if(LogicalHeader[1] == 0)
            if(debug)
                @printf("Skipping Empty Record 0x%x\n", LogicalHeader[0])
            end
            continue
        end

        if(LogicalHeader[0] == 0x2)
            mode = convert(Uint32,0)
            ReadRecord(recPtr._AdminPtr, filePtr, LogicalHeader[1], mode, debug);
            continue;
        end

        if(LogicalHeader[0] == 0x80)
            mode = convert(Uint32,0)
            ReadRecord(recPtr._TriggerPtr, filePtr, LogicalHeader[1], mode, debug);
            continue;
        end

        if(LogicalHeader[0] == 0x81)
            mode = convert(Uint32,0)
            ReadRecord(recPtr._TLBPtr, filePtr, LogicalHeader[1], mode, debug);
            continue;
        end

        if(LogicalHeader[0] == 0x60)
            mode = convert(Uint32,0)
            ReadRecord(recPtr._GPSPtr, filePtr, LogicalHeader[1], mode, debug);
            continue;
        end

        if(LogicalHeader[0] == 0x11)
            ReadRecord(recPtr._TracePtr, filePtr, LogicalHeader[1], debug);
            continue;
        end

        if(LogicalHeader[0] == 0x21)
            ReadRecord(recPtr._HistoryPtrfilePtr, LogicalHeader[1], debug);
            continue
        end

        @printf("Found Unimplemented Record Type 0x%x", LogicalHeader[0])
        break
    end
end
