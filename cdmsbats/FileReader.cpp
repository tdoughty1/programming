#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <string>
#include <typeinfo>
#include <stdint.h>
#include <time.h>
#include <zlib.h>

#include "cdmsrawfilestream.h"
#include "detectorconfigrecord.h"
#include "eventrecord.h"

using namespace std;

int main()
{
    DetectorConfigRecord* DetectorConfigPtr = new DetectorConfigRecord();
    EventRecord* EventPtr = new EventRecord();

    string fileName = "/home/tdoughty1/Workspace/data/raw/01120411_1132/01120411_1132_F0003.gz";
    bool debug = true;

    clock_t startTime = clock();

    CDMSRawFileStream* fgzRawDataPtr = new CDMSRawFileStream(fileName, "rb");

    int nread = 2; // FIXME - Remove Hardcoded value?
    uint32_t FileHeader[nread];

    fgzRawDataPtr->ReadWords(nread*sizeof(uint32_t), FileHeader);
    if(debug)
    {
        cout << "Endian Check = 0x" << setbase(16) << FileHeader[0] << endl;
        cout << "File Header = 0x" << setbase(16) << FileHeader[1] << endl;
    }

    uint32_t ConfigHeader[nread];

    fgzRawDataPtr->ReadWords(nread*sizeof(uint32_t), ConfigHeader);
    if(debug)
    {
        cout << setbase(16) << "Config Header = 0x" << ConfigHeader[0] << endl;
        cout << setbase(10) << "Config Record Length = " << ConfigHeader[1] << endl;
    }

    ////////////////////////////////////////////////////////////////////////////////////////////
    // Read Detector Config Info
    ////////////////////////////////////////////////////////////////////////////////////////////
    DetectorConfigPtr->ReadRecord(fgzRawDataPtr, ConfigHeader[1], debug);

    ////////////////////////////////////////////////////////////////////////////////////////////
    // Loop through Events
    ////////////////////////////////////////////////////////////////////////////////////////////
    int nEvent = 0;
    while(nEvent < 500)
    {
        uint32_t EventHeader[nread];
        nEvent++;

        fgzRawDataPtr->ReadWords(nread*sizeof(uint32_t), EventHeader);
        if(debug)
        {
            cout << "Loading Event Number " << nEvent << endl;
            cout << setbase(16) << "Event Header = 0x" << EventHeader[0] << endl;
            cout << setbase(10) << "Event Record Length = " << EventHeader[1] << endl;
        }

        EventPtr->ReadRecord(fgzRawDataPtr, EventHeader[1], debug);
    }

    fgzRawDataPtr->Close();

    clock_t endTime = clock();

    cout << "Loading Data took " << setprecision(2) << (float(endTime-startTime)/CLOCKS_PER_SEC) << endl;

    return 0;
}
