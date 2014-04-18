#ifndef DETECTORCONFIGRECORD_H
#define DETECTORCONFIGRECORD_H

#include "datarecord.h"
#include "phononchanrecord.h"
#include "chargechanrecord.h"

class DetectorConfigRecord : public DataRecord
{
    public:

        /** Default constructor */
        DetectorConfigRecord();

        /** Default destructor */
        virtual ~DetectorConfigRecord(){};

        void ReadRecord(CDMSRawFileStream*, int, bool);

        void PrintValues(){};

        void StoreValues(int32_t*){};

        void StoreValues(uint32_t*){};

    protected:
    private:

        void _InitValues();

        PhononChanRecord* _pChanPtr;
        ChargeChanRecord* _qChanPtr;
};

#endif // DETECTORCONFIGRECORD_H
