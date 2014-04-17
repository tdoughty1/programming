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

        // Dummy Method - should be overloaded by Inheriting Classes
        virtual void StoreValues(int32_t*) = 0;

        // Dummy Method - should be overloaded by Inheriting Classes
        virtual void PrintValues() = 0;

        // Primary Method Call for data record
        void ReadRecord(CDMSRawFileStream*, int, bool);

    protected:

    private:
};

#endif // DATARECORD_H
