include("/home/tdoughty1/Workspace/programming/julia/cdmsbats/CDMSRawFileStream.jl")

abstract DataRecord

function ReadRecord(recPtr::DataRecord, filePtr::CDMSRawFileStream, RecordLength::Int, mode::Int, debug::Bool)

    Record = ReadWords(filePtr, RecordLength, mode)

    StoreValues(Record)

    if(debug)
            PrintValues(recPtr)
    end
end

function ReadRecord(recPtr::DataRecord, filePtr::CDMSRawFileStream, RecordLength::Int, mode::Int)

    Record = ReadWords(filePtr, RecordLength, mode)

    StoreValues(Record)
end
