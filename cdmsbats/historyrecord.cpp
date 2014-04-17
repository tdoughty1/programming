#include "historyrecord.h"

HistoryRecord::HistoryRecord()
{
    _VetoPtr = new HistSubRecord();
    _TrigPtr = new HistSubRecord();
}

void HistoryRecord::StoreValues(int32_t* Record)
{
    int index = 0;
    _VetoPtr->ReadRecord(Record, index, false);
    _TrigPtr->ReadRecord(Record, index, false);
}

void HistoryRecord::PrintValues()
{
    _VetoPtr->PrintValues();
    _TrigPtr->PrintValues();
}
