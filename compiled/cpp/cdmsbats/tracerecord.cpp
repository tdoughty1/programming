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

            // Try First Method
            _Trace.clear();
            _Trace.resize(nSamples);

            uint16_t TempArray[nSamples];
            filePtr->ReadWords(nSamples*2, TempArray);

            for(int i=0; i<nSamples; i++)
            {
                _Trace.at(i) = TempArray[i];
            }

            if(debug)
            {
                cout << "First Element of Trace = " << _Trace.at(0) << endl;
                cout << "Second Element of Trace = " << _Trace.at(1) << endl;
            }

            continue;
        }

        cout << "Found unexpected trace header" << endl;
        exit(EXIT_FAILURE);
    }
}
