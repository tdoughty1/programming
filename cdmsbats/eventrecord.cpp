#include <iostream>
#include <iomanip>

#include "eventrecord.h"

using namespace std;

EventRecord::EventRecord()
{
    _AdminPtr = new AdminRecord();
    _TriggerPtr = new TriggerRecord();
    _TLBPtr = new TLBRecord();
    _GPSPtr = new GPSRecord();
    _TracePtr = new TraceRecord();
    _HistoryPtr = new HistoryRecord();
}

void EventRecord::ReadRecord(CDMSRawFileStream* filePtr, int RecordLength, bool debug=false)
{
    int endPos = filePtr->Tell() + RecordLength;

    while(filePtr->Tell() < endPos)
    {
        int32_t LogicalHeader[2];
        filePtr->ReadWords(2*sizeof(int32_t), LogicalHeader);

        cout << "Location after Reading Logical Header = " << setbase(10) << filePtr->Tell() << endl;

        if(debug)
        {
            cout << "Logical Header = 0x" << setbase(16) << LogicalHeader[0] << endl;
            cout << "Logical Record Length = " << setbase(10) << LogicalHeader[1] << endl;
        }

        if(LogicalHeader[1] == 0)
        {
            if(debug)
            {
                cout << "Skipping Empty Record 0x" << setbase(16) << LogicalHeader[0] << endl;
            }
            continue;
        }

        if(LogicalHeader[0] == 0x2)
        {
            uint32_t mode;
            _AdminPtr->ReadRecord(filePtr, LogicalHeader[1], mode, debug);
            continue;
        }

        if(LogicalHeader[0] == 0x80)
        {
            uint32_t mode;
            _TriggerPtr->ReadRecord(filePtr, LogicalHeader[1], mode, debug);
            continue;
        }

        if(LogicalHeader[0] == 0x81)
        {
            uint32_t mode;
            _TLBPtr->ReadRecord(filePtr, LogicalHeader[1], mode, debug);
            continue;
        }

        if(LogicalHeader[0] == 0x60)
        {
            uint32_t mode;
            _GPSPtr->ReadRecord(filePtr, LogicalHeader[1], mode, debug);
            continue;
        }

        if(LogicalHeader[0] == 0x11)
        {
            _TracePtr->ReadRecord(filePtr, LogicalHeader[1], debug);
            continue;
        }

        if(LogicalHeader[0] == 0x21)
        {
            _HistoryPtr->ReadRecord(filePtr, LogicalHeader[1], debug);
            continue;
        }

        cout << "Found Unimplemented Record Type 0x" << setbase(16) << LogicalHeader[0] << endl;
        break;
    }
}
