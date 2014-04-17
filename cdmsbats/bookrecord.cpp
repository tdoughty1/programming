#include "bookrecord.h"

BookRecord::BookRecord()
{
    _digBaseAddress = NULL;
    _digChannel = NULL;
    _detCode = NULL;
}

void BookRecord::StoreValues(int32_t* Record)
{
    _digBaseAddress = Record[0];
    _digChannel = Record[1];
    _detCode = Record[2];
}

void BookRecord::PrintValues()
{
    cout << "Digitizer Base Address = 0x" << setbase(16) << _digBaseAddress << endl;
    cout << "Digitizer Channel = " << _digChannel << endl;
    cout << "Detector Code = " << _detCode << endl;
}
