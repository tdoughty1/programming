#ifndef DATARECORD_H
#define DATARECORD_H

#include "cdmsrawfilestream.h"

class DataRecord
{
    public:
        /** Default constructor */
        DataRecord();

        /** Standard constructor */
        DataRecord(bool debug);

        /** Default destructor */
        virtual ~DataRecord();

        // Dummy Method - should be overloaded by Inheriting Classes
        void StoreValues(uint32_t* Record) {};

        // Dummy Method - should be overloaded by Inheriting Classes
        int PrintValues() {};

        // Primary Method Call for data record
        void ReadRecord(CDMSRawFileStream* filePtr, int RecordLength, bool debug);

    protected:
        // Dummy Method - should be overloaded by Inheriting Classes
        int _InitValues() {};

        // Dummy Method - should be overloaded by Inheriting Classes
        int _PrintLine() {};

    private:
};

#endif // DATARECORD_H
