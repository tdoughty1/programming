#include <iostream>
#include <iomanip>

#include "detectorconfigrecord.h"
#include "phononchanrecord.h"
#include "chargechanrecord.h"

using namespace std;

DetectorConfigRecord::DetectorConfigRecord()
{
    _pChanPtr = new PhononChanRecord();
    _qChanPtr = new ChargeChanRecord();
}

void DetectorConfigRecord::ReadRecord(CDMSRawFileStream* filePtr, int RecordLength, bool debug=false)
{
    int32_t ChanHeader[4*2];

    int endPos = filePtr->Tell() + RecordLength;

    while(filePtr->Tell() < endPos)
    {
        filePtr->ReadWords(4*2, ChanHeader);

        if(debug)
        {
            cout << "Channel Header = 0x" << setbase(16) << ChanHeader[0] << endl;
            cout << "Channel Length = " << setbase(10) << ChanHeader[1] << endl;
        }

        // Record of No length
        if(ChanHeader[1] == 0)
        {
            continue;
        }

        // Bookkeeping Record
        if(ChanHeader[0] == 0x10001)
        {
            int32_t mode;
            _pChanPtr->ReadRecord(filePtr, ChanHeader[1], mode, debug);
            continue;
        }

        // Timebase Record
        if(ChanHeader[0] == 0x10002)
        {
            int32_t mode;
            _qChanPtr->ReadRecord(filePtr, ChanHeader[1], mode, debug);
            continue;
        }

        cout << "Found unexpected trace header" << endl;
        exit(EXIT_FAILURE);
    }
}

