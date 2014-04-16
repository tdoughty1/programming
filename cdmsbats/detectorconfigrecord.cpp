#include <iostream>

#include "detectorconfigrecord.h"
#include "phononchanrecord.h"
#include "chargechanrecord.h"

using namespace std;

void DetectorConfigRecord::_InitValues()
{
    _pChanPtr = new PhononChanRecord();
    _qChanPtr = new ChargeChanRecord();
}

void DetectorConfigRecord::_PrintLine()
{
    cout << "Found Detector Config Record" <<  endl;
}

void DetectorConfigRecord::ReadRecord(CDMSRawFileStream* filePtr, int RecordLength, bool debug=false)
{
    uint32_t ChanHeader[4*2];

    int endPos = filePtr->Tell() + RecordLength;

    cout << "End Position = %d" << endPos << endl;

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
            _pChanPtr->ReadRecord(filePtr, ChanHeader[1], debug);
            continue;
        }

        // Timebase Record
        if(ChanHeader[0] == 0x10002)
        {
            _qChanPtr->ReadRecord(filePtr, ChanHeader[1], debug);
            continue;
        }

        cout << "Found unexpected trace header" << endl;
        exit(EXIT_FAILURE);
    }
}

