#ifndef ADMINRECORD_H
#define ADMINRECORD_H

#include "datarecord.h"


class AdminRecord : public DataRecord
{
    public:
        /** Default constructor */
        AdminRecord();

        /** Default destructor */
        virtual ~AdminRecord(){};

        void StoreValues(int32_t*){};

        void StoreValues(uint32_t*);

        void PrintValues();

    protected:
    private:

        uint64_t _SeriesNumber;
        uint32_t _EventNumber;
        uint32_t _EventTime;
        uint32_t _LiveTime;
        uint32_t _TimeSince;
};

#endif // ADMINRECORD_H
