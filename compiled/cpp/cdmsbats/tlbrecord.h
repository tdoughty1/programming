#ifndef TLBRECORD_H
#define TLBRECORD_H

#include <vector>

#include "datarecord.h"


class TLBRecord : public DataRecord
{
    public:
        /** Default constructor */
        TLBRecord();

        /** Default destructor */
        virtual ~TLBRecord(){};

        void StoreValues(int32_t*){};

        void StoreValues(uint32_t*);

        void PrintValues();

    protected:
    private:
        vector<int32_t> _TriggerMask;
};

#endif // TLBRECORD_H
