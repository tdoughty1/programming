#include <iostream>
#include <iomanip>

#include "chargechanrecord.h"
#include "datarecord.h"

using namespace std;

ChargeChanRecord::ChargeChanRecord()
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

void ChargeChanRecord::StoreValues(int32_t* Record)
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
    cout << "Driver Gain = " << fixed << setprecision(1) << _driverGain << endl;
    cout << "Channel Bias = " << fixed << setw(5) << setprecision(3) << _chanBias << " V" << endl;
    cout << "RTF Offset = " << fixed << setw(5) << setprecision(3) << _rtfOffset << " V" << endl;
    cout << "Delta T = " << fixed << setw(4) << setprecision(2) << _deltat << " us" << endl;
    cout << "t0 = " << fixed << setw(5) << setprecision(1) << _t0 << " us" << endl;
    cout << "Trace Length = " << _traceLength << endl;
}
