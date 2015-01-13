include("/home/tdoughty1/Workspace/programming/julia/cdmsbats/DataRecord.jl")

using cdmsrawfilestream

type PhononChanRecord <: DataRecord

    _detCode
    _towerNum
    _driverGain
    _qetBias
    _squidBias
    _lockPoint
    _rtfOffset
    _varGain
    _deltat
    _t0
    _traceLength

    PhononChanRecord() = new(None, None, None, None, None, None, None, None, None, None, None)
end

function StoreValues(recPtr::PhononChanRecord, Record::Array)

    recPtr._detCode = (Record[1] & 0xFFFFFFFF)
    recPtr._towerNum = Record[2]
    recPtr._driverGain = float(Record[3])/100
    recPtr._qetBias = float(Record[4])/100
    recPtr._squidBias = float(Record[5])/100
    recPtr._lockPoint = float(Record[6])/100
    recPtr._rtfOffset = float(Record[7])/1e6
    recPtr._varGain = Record[8]
    recPtr._deltat = float(Record[9])/1000
    recPtr._t0 = float(Record[10])/1000
    recPtr._traceLength = Record[11]

end

function PrintValues(recPtr::PhononChanRecord)

    @printf("Detector Code = %d\n", recPtr._detCode)
    @printf("Tower Number = %d\n", recPtr._towerNum)
    @printf("Driver Gain = %.1f\n", recPtr._driverGain)
    @printf("QET Bias = %6.2f pA\n", recPtr._qetBias)
    @printf("SQUID Bias = %6.2f pA\n", recPtr._squidBias)
    @printf("SQUID Lock Point = %4.2f uV \n", recPtr._lockPoint)
    @printf("RTF Offset = %4.2f V\n", recPtr._rtfOffset)
    @printf("Variable Gain = %d\n", recPtr._varGain)
    @printf("Delta T = %4.2f us\n", recPtr._deltat)
    @printf("t0 = %5.1f us\n", recPtr._t0)
    @printf("Trace Length = %d\n", recPtr._traceLength)

end
