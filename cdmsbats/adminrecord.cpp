#include "adminrecord.h"

AdminRecord::AdminRecord()
{
    _SeriesNumber = NULL;
    _EventNumber = NULL;
    _EventTime = NULL;
    _LiveTime = NULL;
    _TimeSince = NULL;
}

void AdminRecord::StoreValues(int32_t* Record)
{
    _SeriesNumber = Record[0]*1e4 + Record[1];
    _EventNumber = Record[2];
    _EventTime = Record[3];
    _LiveTime = Record[4];
    _TimeSince = Record[5];
}

void AdminRecord::PrintValues()
{
    cout << "SeriesNumber = " << _SeriesNumber << endl;
    cout << "EventNumber = " << _EventNumber << endl;
    cout << "EventTime = " << _EventTime << endl;
    cout << "LiveTime = " << _LiveTime << endl;
    cout << "TimeSince = " << _TimeSince << endl;
}
