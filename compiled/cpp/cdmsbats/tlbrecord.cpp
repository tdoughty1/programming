#include <iostream>
#include <iomanip>

#include "tlbrecord.h"

using namespace std;

TLBRecord::TLBRecord()
{
    _TriggerMask.resize(6);
}

void TLBRecord::StoreValues(uint32_t* Record)
{
    for(int i=0; i<6; i++)
    {
        _TriggerMask[i] = Record[i];
    }
}

void TLBRecord::PrintValues()
{
    for(int i=0; i<6; i++)
    {
        cout << "Tower " << (i+1) << " TLB Mask = 0x" << setbase(16) << _TriggerMask[i] << endl;
    }
}
