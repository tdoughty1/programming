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

        void StoreValues(int32_t*);

        void PrintValues();

    protected:
    private:

        int _SeriesNumber;
        int _EventNumber;
        int _EventTime;
        int _LiveTime;
        int _TimeSince;
};

#endif // ADMINRECORD_H
