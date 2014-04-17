#ifndef TIMERECORD_H
#define TIMERECORD_H

#include "datarecord.h"


class TimeRecord : public DataRecord
{
    public:
        /** Default constructor */
        TimeRecord();

        /** Default destructor */
        virtual ~TimeRecord(){};

        void StoreValues(int32_t*);

        void PrintValues();

    protected:
    private:

        int _t0;
        int _deltat;
        int _N;
};

#endif // TIMERECORD_H
