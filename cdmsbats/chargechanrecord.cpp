#include "chargechanrecord.h"
#include "datarecord.h"

void ChargeChanRecord::_InitValues()
{
    _detCode = NULL;
    _towerNum = NULL;
    _driverGain = NULL;
    _chanBias = NULL;
    _rtfOffset = NULL;
    _deltat = NULL;
    _t0 = NULL;
    _traceLength = NULL;
}

void ChargeChanRecord::StoreValues(uint32_t* Record)
{
    _detCode = Record[0];
    _towerNum = Record[1];
    _driverGain = float(Record[2])/100;
    _chanBias = float(Record[3])/1e6;
    _rtfOffset = float(Record[4])/1e6;
    _deltat = float(Record[5])/1000;
    _t0 = float(Record[6])/1000;
    _traceLength = Record[7];
}

void ChargeChanRecord::PrintValues()
{
    cout << "Detector Code = " << _detCode << endl;
    cout << "Tower Number = " << _towerNum << endl;
    cout << "Driver Gain = " << _driverGain << endl;
    cout << "Channel Bias = " << setprecision(3) << _chanBias << " V" << endl;
    cout << "RTF Offset = " << setprecision(3) << _rtfOffset << " V" << endl;
    cout << "Delta T = " << setprecision(2) << _deltat << " us" << endl;
    cout << "t0 = " << setprecision(1) << _t0 << " us" << endl;
    cout << "Trace Length = " << _traceLength << endl;
}
