#ifndef TLBRECORD_H
#define TLBRECORD_H

#include "datarecord.h"


class TLBRecord : public DataRecord
{
    public:
        /** Default constructor */
        TLBRecord();

        /** Default destructor */
        virtual ~TLBRecord(){};

        void StoreValues(uint32_t*);

        void PrintValues();

    protected:
    private:
        int32_t _TriggerTime;
        int32_t _TriggerMask[6];
};

#endif // TRIGGERRECORD_H
