#include "gpsrecord.h"

GPSRecord::GPSRecord()
{
    _Date = NULL;
    _Time = NULL;
    _SubTime = NULL;
}

void GPSRecord::StoreValues(int32_t* Record)
{
    _Date = Record[0];
    _Time = Record[1];
    _SubTime = Record[2];
}

void GPSRecord::PrintValues()
{
    cout << "GPS Date = " << _Date << endl;
    cout << "GPS Time = " << _Time << endl;
    cout << "GPS SubTime = " << _SubTime << endl;
}
