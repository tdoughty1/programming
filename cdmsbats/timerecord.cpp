#include <iostream>
#include <iomanip>

#include "timerecord.h"

using namespace std;

TimeRecord::TimeRecord()
{
    _t0 = NULL;
    _deltat = NULL;
    _N = NULL;
}

void TimeRecord::StoreValues(uint32_t* Record)
{
    int32_t temp = Record[0];

    _t0 = float(temp)/1000.;
    _deltat = float(Record[1])/1000;
    _N = Record[2];
}

void TimeRecord::PrintValues()
{
    cout << "Start Time = " << _t0 << " us" << endl;
    cout << "Delta Time = " << _deltat << " us" << endl;
    cout << "Number of Samples = " << _N << endl;
}
