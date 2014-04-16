#include "phononchanrecord.h"
#include "datarecord.h"

void PhononChanRecord::_InitValues()
{
    _detCode = NULL;
    _towerNum = NULL;
    _driverGain = NULL;
    _qetBias = NULL;
    _squidBias = NULL;
    _lockPoint = NULL;
    _rtfOffset = NULL;
    _varGain = NULL;
    _deltat = NULL;
    _t0 = NULL;
    _traceLength = NULL;
}

void PhononChanRecord::StoreValues(uint32_t* Record)
{
    _detCode = Record[0];
    _towerNum = Record[1];
    _driverGain = float(Record[2])/100;
    _qetBias = float(Record[3])/100
    _squidBias = float(Record[4])/100
    _lockPoint = float(Record[5])/100
    _rtfOffset = float(Record[6])/1e6;
    _varGain = Record[7]
    _deltat = float(Record[8])/1000;
    _t0 = float(Record[9])/1000;
    _traceLength = Record[10];
}

void PhononChanRecord::PrintValues()
{
    cout << "Detector Code = " << _detCode << endl;
    cout << "Tower Number = " << _towerNum << endl;
    cout << "Driver Gain = " << _driverGain << endl;
    cout << "QET Bias = " << setprecision(2) << _qetBias << " pA" << endl;
    cout << "SQUID Bias = " << setprecision(2) << _squidBias << " pA" << endl;
    cout << "SQUID Lock Point = " << setprecision(2) << _lockPoint << " uV" << endl;
    cout << "RTF Offset = " << setprecision(3) << _rtfOffset << " V" << endl;
    cout << "Variable Gain = " << _varGain << endl;
    cout << "Delta T = " << setprecision(2) << _deltat << " us" << endl;
    cout << "t0 = " << setprecision(1) << _t0 << " us" << endl;
    cout << "Trace Length = " << _traceLength << endl;
}
