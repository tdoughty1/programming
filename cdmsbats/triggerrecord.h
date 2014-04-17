#ifndef TRIGGERRECORD_H
#define TRIGGERRECORD_H

#include "datarecord.h"


class TriggerRecord : public DataRecord
{
    public:
        /** Default constructor */
        TriggerRecord();

        /** Default destructor */
        virtual ~TriggerRecord(){};

        void StoreValues(uint32_t*);

        void PrintValues();

    protected:
    private:
        int32_t _TriggerTime;
        int32_t _TriggerMask[6];
};

#endif // TRIGGERRECORD_H
