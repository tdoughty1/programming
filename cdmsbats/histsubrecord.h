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

        void ReadRecord(int32_t*, int, bool);

        void StoreValues(int32_t*){};

        void PrintValues();

    protected:
    private:

        vector< vector<uint32_t>> _Masks;
        vector<uint32_t> _Times;
        int _nMasks;
        int _nTimes;
};

#endif // HISTSUBRECORD_H
