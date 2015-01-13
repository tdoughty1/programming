import GZip

include("/home/tdoughty1/Workspace/programming/julia/cdmsbats/CDMSRawFileStream.jl")

fgzRawDataPtr = CDMSRawFileStream()

fname = "/home/tdoughty1/Workspace/data/raw/01120411_1132/01120411_1132_F0002.gz"

startTime = time()

Open(fgzRawDataPtr, fname, "rb")

mode = convert(Uint32,1)

FileHeader = ReadWords(fgzRawDataPtr,8,mode)

println(hex(FileHeader[1]))
println(hex(FileHeader[2]))

println(typeof(FileHeader))

ConfigHeader = ReadWords(fgzRawDataPtr,8,mode)

println(hex(ConfigHeader[1]))
println(ConfigHeader[2])

endTime = time()
println(string("Loading File took ", endTime-startTime, "s"))

Close(fgzRawDataPtr)
