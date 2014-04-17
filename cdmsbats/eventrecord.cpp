#include "eventrecord.h"

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

        if(debug)
        {
            cout << "Logical Header = 0x" << setbase(16) << LogicalHeader[0] << endl;
            cout << "Logical Record Length = " << LogicalHeader[1] << endl;
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
            _AdminPtr->ReadRecord(filePtr, LogicalHeader[1], debug);
            continue;
        }

        if(LogicalHeader[0] == 0x80)
        {
            _TriggerPtr->ReadRecord(filePtr, LogicalHeader[1], debug);
            continue;
        }

        if(LogicalHeader[0] == 0x81)
        {
            _TLBPtr->ReadRecord(filePtr, LogicalHeader[1], debug);
            continue;
        }

        if(LogicalHeader[0] == 0x60)
        {
            _GPSPtr->ReadRecord(filePtr, LogicalHeader[1], debug);
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
