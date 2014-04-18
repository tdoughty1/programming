#ifndef DATARECORD_H
#define DATARECORD_H

#include "cdmsrawfilestream.h"

class DataRecord
{
    public:
        /** Default constructor */
        DataRecord(){};

        /** Default destructor */
        virtual ~DataRecord(){};

        virtual void StoreValues(int32_t*) = 0;

        virtual void StoreValues(uint32_t*) = 0;

        virtual void PrintValues() = 0;

        // Primary Method Call for data record
        // Overloaded to allow multiple read datatypes
        void ReadRecord(CDMSRawFileStream*, int, uint32_t, bool);

        void ReadRecord(CDMSRawFileStream*, int, int32_t, bool);

    protected:

    private:
};

#endif // DATARECORD_H
