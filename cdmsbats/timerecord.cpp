#include "timerecord.h"

TimeRecord::TimeRecord()
{
    _t0 = NULL;
    _deltat = NULL;
    _N = NULL;
}

void TimeRecord::StoreValues(int32_t* Record)
{
    _t0 = float(Record[0])/1000;
    _deltat = float(Record[1])/1000;
    _N = Record[2];
}

void TimeRecord::PrintValues()
{
    cout << "Start Time = " << fixed << setw(6) << setprecision(2) << _t0 << endl;
    cout << "Delta Time = " << fixed << setw(3) << setprecision(2) << _deltat << endl;
    cout << "Number of Samples = " << _N << endl;
}
