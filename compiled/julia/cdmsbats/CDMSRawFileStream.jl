import GZip

module cdmsRawFileStream

type CDMSRawFileStream

    _FileName
    _FileStream
    _Open
    _Pos

    CDMSRawFileStream() = new("", None, false, -1)
end

function Open(filePtr::CDMSRawFileStream, fName::String, mode::String)

    filePtr._FileStream = GZip.open(fName, mode)
    filePtr._FileName = fName
    filePtr._Open = true
    filePtr._Pos = 0
end

function Close(filePtr::CDMSRawFileStream)

    if(filePtr._Open)
        close(filePtr._FileStream)
    else
        println("Warning in CDMSRawFileStream::Close:")
        println("No current filestream open. No action taken.")
        return 1;
    end
end

function Tell(filePtr::CDMSRawFileStream)

    if(filePtr._Open)
        return filePtr._Pos
    else

        println("Warning in CDMSRawFileStream::Tell:")
        println("No currently opened file in stream.")
        return -1;
    end
end

function Seek(filePtr::CDMSRawFileStream, nPos::Int)

    if(filePtr._Open)
        GZip.seek(filePtr._FileStream, nPos, 0);
        return
    else
        println("Warning in CDMSRawFileStream::Seek:")
        println("No currently opened file in stream.")
        return 1;
    end
end

function Skip(filePtr::CDMSRawFileStream, nPos::Int)

    if(filePtr._Open)
        GZip.skip(filePtr._FileStream, nPos);
        return
    else
        println("Warning in CDMSRawFileStream::Skip:")
        println("No currently opened file in stream.")
        return 1;
    end
end

function ReadWords(filePtr::CDMSRawFileStream, nBytes::Int, mode::Int32)

    if(filePtr._Open)
        recArray = Array(Int32,convert(Int,nBytes/4))
        read(filePtr._FileStream,recArray)
        return recArray
    else
        println("ERROR in CDMSRawFileStream::ReadWords:")
        println("No open file to read from")
        exit(1);
    end
end

function ReadWords(filePtr::CDMSRawFileStream, nBytes::Int, mode::Uint32)

    if(filePtr._Open)
        recArray = Array(Uint32,convert(Int,nBytes/4))
        read(filePtr._FileStream,recArray)
        return recArray
    else
        println("ERROR in CDMSRawFileStream::ReadWords:")
        println("No open file to read from")
        exit(1);
    end
end

function ReadWords(filePtr::CDMSRawFileStream, nBytes::Int, mode::Uint16)

    if(filePtr._Open)
        recArray = Array(Uint16,convert(Int,nBytes/2))
        read(filePtr._FileStream,recArray)
        return recArray
    else
        println("ERROR in CDMSRawFileStream::ReadWords:")
        println("No open file to read from")
        exit(1);
    end
end

end
