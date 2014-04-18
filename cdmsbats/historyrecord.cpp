#include <iostream>

#include "historyrecord.h"

using namespace std;

HistoryRecord::HistoryRecord()
{
    _VetoPtr = new HistSubRecord();
    _TrigPtr = new HistSubRecord();
}

void HistoryRecord::ReadRecord(CDMSRawFileStream* filePtr, int RecordLength, bool debug=false)
{
    _VetoPtr->ReadRecord(filePtr, false);
    _TrigPtr->ReadRecord(filePtr, false);

    if(debug)
    {
        PrintValues();
    }
}

void HistoryRecord::PrintValues()
{
    _VetoPtr->PrintValues();
    _TrigPtr->PrintValues();
}
