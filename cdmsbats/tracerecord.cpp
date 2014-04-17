#include "tracerecord.h"

TraceRecord::TraceRecord()
{
    _BookPtr = new BookRecord();
    _TimePtr = new TimeRecord();
}

void TraceRecord::ReadRecord(CDMSRawFileStream* filePtr, int RecordLength, bool debug=false)
{
    int endPos = filePtr->Tell() + RecordLength;

    while(filePtr->Tell() < endPos)
    {
        int32_t TraceHeader[2];
        filePtr->ReadWords(2*sizeof(int32_t)*2, TraceHeader);

        // Record of No length
        if(TraceHeader[1] == 0)
        {
            continue;
        }

        // Bookkeeping Record
        if(TraceHeader[0] == 0x11)
        {
            _BookPtr->ReadRecord(filePtr, TraceHeader[1], debug);
            continue;
        }

        // Timebase Record
        if(TraceHeader[0] == 0x12)
        {
            _TimePtr->ReadRecord(filePtr, TraceHeader[1], debug);
            continue;
        }

        // Trace Array
        if(TraceHeader[0] == 0x13)
        {
            int nSamples = TraceHeader[1];
            _Trace[nSamples];
            filePtr->ReadWords(nSamples*2, _Trace);
            continue;
        }

        cout << "Found unexpected trace header" << endl;
        exit(EXIT_FAILURE);
    }
}
