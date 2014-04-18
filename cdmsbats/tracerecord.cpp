#include <iostream>
#include <iomanip>

#include "tracerecord.h"

using namespace std;

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
        cout << "Location before Reading Trace Header " << filePtr->Tell() << endl;

        int32_t TraceHeader[2];
        filePtr->ReadWords(sizeof(int32_t)*2, TraceHeader);

        if(debug)
        {
            cout << "Trace Header = 0x" << setbase(16) << TraceHeader[0] << endl;
            cout << "Trace Length Value = " << setbase(10) << TraceHeader[1] << endl;
        }

        // Record of No length
        if(TraceHeader[1] == 0)
        {
            continue;
        }

        // Bookkeeping Record
        if(TraceHeader[0] == 0x11)
        {
            uint32_t mode;
            _BookPtr->ReadRecord(filePtr, TraceHeader[1], mode, debug);
            continue;
        }

        // Timebase Record
        if(TraceHeader[0] == 0x12)
        {
            uint32_t mode;
            _TimePtr->ReadRecord(filePtr, TraceHeader[1], mode, debug);
            continue;
        }

        // Trace Array
        if(TraceHeader[0] == 0x13)
        {
            int nSamples = TraceHeader[1];

            uint16_t TempArray[nSamples];

            cout << "Trace Start = " << filePtr->Tell() << endl;
            filePtr->ReadWords(nSamples*2, TempArray);
            cout << "Trace Finish = " << filePtr->Tell() << endl;

            for(int i=0; i<nSamples; i++)
            {
                _Trace.push_back(TempArray[i]);
            }

            break;
        }

        cout << "Found unexpected trace header" << endl;
        exit(EXIT_FAILURE);
    }
}
