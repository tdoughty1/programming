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
        virtual void StoreValues(uint32_t*) {};

        // Dummy Method - should be overloaded by Inheriting Classes
        virtual void PrintValues() {cout << "In Data Record Print Values Method" << endl;};

        // Primary Method Call for data record
        void ReadRecord(CDMSRawFileStream*, int, bool);

    protected:
        // Dummy Method - should be overloaded by Inheriting Classes
        virtual void _InitValues() {};

        // Dummy Method - should be overloaded by Inheriting Classes
        virtual void _PrintLine() {};

    private:
};

#endif // DATARECORD_H
