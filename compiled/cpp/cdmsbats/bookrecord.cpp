#include <iostream>
#include <iomanip>

#include "bookrecord.h"

using namespace std;

BookRecord::BookRecord()
{
    _digBaseAddress = NULL;
    _digChannel = NULL;
    _detCode = NULL;
}

void BookRecord::StoreValues(uint32_t* Record)
{
    _digBaseAddress = Record[0];
    _digChannel = Record[1];
    _detCode = Record[2];
}

void BookRecord::PrintValues()
{
    cout << "Digitizer Base Address = 0x" << setbase(16) << _digBaseAddress << endl;
    cout << "Digitizer Channel = " << setbase(10) << _digChannel << endl;
    cout << "Detector Code = " << setbase(10) << _detCode << endl;
}
