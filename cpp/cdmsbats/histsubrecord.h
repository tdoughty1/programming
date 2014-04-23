#ifndef HISTSUBRECORD_H
#define HISTSUBRECORD_H

#include <vector>

#include "datarecord.h"

class HistSubRecord : public DataRecord
{
    public:
        /** Default constructor */
        HistSubRecord(){};

        /** Default destructor */
        virtual ~HistSubRecord(){};

        void ReadRecord(CDMSRawFileStream*, bool);

        void StoreValues(int32_t*){};

        void StoreValues(uint32_t*){};

        void PrintValues();

    protected:
    private:

        vector< vector<uint32_t> > _Masks;
        vector<int32_t> _Times;
        int32_t _nMasks;
        int32_t _nTimes;
};

#endif // HISTSUBRECORD_H
