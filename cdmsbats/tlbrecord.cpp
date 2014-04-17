#include "tlbrecord.h"

TLBRecord::TLBRecord()
{
    _TriggerTime = NULL;
}

void TLBRecord::StoreValues(int32_t* Record)
{
    _TriggerTime = Record[0];
    for(int i=0; i<6; i++)
    {
        _TriggerMask[i] = Record[i+1];
    }
}

void TLBRecord::PrintValues()
{
    cout << "Trigger Time = %d" << _TriggerTime << endl;

    for(int i=0; i<6; i++)
    {
        cout << "Trigger Mask " << (i+1) << " = 0x" << setbase(16) << _TriggerMask[i] << endl;
    }
}
