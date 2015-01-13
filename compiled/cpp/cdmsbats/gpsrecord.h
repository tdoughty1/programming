#ifndef GPSRECORD_H
#define GPSRECORD_H

#include "datarecord.h"


class GPSRecord : public DataRecord
{
    public:
        /** Default constructor */
        GPSRecord();

        /** Default destructor */
        virtual ~GPSRecord(){};

        void StoreValues(int32_t*);

        void StoreValues(uint32_t*){};

        void PrintValues();

    protected:
    private:

        int _Date;
        int _Time;
        int _SubTime;
};

#endif // GPSRECORD_H
