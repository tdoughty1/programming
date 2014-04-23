#include("/home/tdoughty1/Workspace/programming/julia/cdmsbats/DataRecord.jl")
include("/home/tdoughty1/Workspace/programming/julia/cdmsbats/ChargeChanRecord.jl")
include("/home/tdoughty1/Workspace/programming/julia/cdmsbats/PhononChanRecord.jl")

type DetectorConfigRecord <: DataRecord

    _pChanPtr::PhononChanRecord
    _qChanPtr::ChargeChanRecord

    DetectorConfigRecord() = new(PhononChanRecord(), ChargeChanRecord())
end

function ReadRecord(recPtr::DetectorConfigRecord, filePtr::CDMSRawFileStream, RecordLength::Int, debug::Bool)

    endPos = Tell(filePtr) + RecordLength

    while(Tell(filePtr) < endPos)

        ChanHeader = ReadWords(filePtr, 4*2)

        if(debug)
            @printf("Channel Header = 0x%x\n", ChanHeader[1])
            @printf("Channel Length = %d\n",ChanHeader[2])
        end

        # Record of No length
        if(ChanHeader[2] == 0)
            continue;
        end

        # Phonon Config Record
        if(ChanHeader[1] == 0x10001)
            mode = convert(Int32, 0)
            ReadRecord(recPtr._pChanPtr, filePtr, ChanHeader[1], mode, debug);
            continue
        end

        # Charge Config Record
        if(ChanHeader[0] == 0x10002)
            mode = convert(Int32, 0)
            ReadRecord(recPtr._qChanPtr, filePtr, ChanHeader[1], mode, debug);
            continue
        end

        println("Found unexpected trace header")
        exit(EXIT_FAILURE)
    end
end
