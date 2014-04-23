include("/home/tdoughty1/Workspace/programming/julia/cdmsbats/DataRecord.jl")

type ChargeChanRecord <: DataRecord

    _detCode
    _towerNum
    _driverGain
    _chanBias
    _rtfOffset
    _deltat
    _t0
    _traceLength

    ChargeChanRecord() = new(None, None, None, None, None, None, None, None)
end

function StoreValues(recPtr::ChargeChanRecord, Record::Array)

    recPtr._detCode = Record[1] & 0xFFFFFFFF
    recPtr._towerNum = Record[2]
    recPtr._driverGain = float(Record[3])/100
    recPtr._qetBias = float(Record[4])/100
    recPtr._rtfOffset = float(Record[5])/1e6
    recPtr._deltat = float(Record[6])/1000
    recPtr._t0 = float(Record[7])/1000
    recPtr._traceLength = Record[8]

end

function PrintValues(recPtr::ChargeChanRecord)

    @printf("Detector Code = %d\n", recPtr._detCode)
    @printf("Tower Number = %d\n", recPtr._towerNum)
    @printf("Driver Gain = %.1f\n", recPtr._driverGain)
    @printf("Channel Bias = %6.2f\n", recPtr._chanBias)
    @printf("RTF Offset = %4.2f pA\n", recPtr._rtfOffset)
    @printf("Delta T = %4.2f us V\n", recPtr._deltat)
    @printf("t0 = %5.1f us\n", recPtr._t0)
    @printf("Trace Length = %d\n", recPtr._traceLength)

end
