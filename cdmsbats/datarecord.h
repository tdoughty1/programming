#ifndef DATARECORD_H
#define DATARECORD_H

#include "cdmsrawfilestream.h"

class DataRecord
{
    public:
        /** Default constructor */
        DataRecord();

        /** Standard constructor */
        DataRecord(bool);

        /** Default destructor */
        virtual ~DataRecord();

        // Dummy Method - should be overloaded by Inheriting Classes
        void StoreValues(uint32_t*) {};

        // Dummy Method - should be overloaded by Inheriting Classes
        void PrintValues() {};

        // Primary Method Call for data record
        void ReadRecord(CDMSRawFileStream*, int, bool);

    protected:
        // Dummy Method - should be overloaded by Inheriting Classes
        void _InitValues() {};

        // Dummy Method - should be overloaded by Inheriting Classes
        void _PrintLine() {};

    private:
};

#endif // DATARECORD_H
