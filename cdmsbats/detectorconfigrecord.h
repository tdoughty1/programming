#ifndef DETECTORCONFIGRECORD_H
#define DETECTORCONFIGRECORD_H

#include "datarecord.h"
#include "phononchanrecord.h"
#include "chargechanrecord.h"

class DetectorConfigRecord : public DataRecord
{
    public:

        void ReadRecord(CDMSRawFileStream*, int, bool);

        void PrintValues(){};

    protected:
    private:

        void _InitValues();

        void _PrintLine();

        PhononChanRecord* _pChanPtr;
        ChargeChanRecord* _qChanPtr;
};

#endif // DETECTORCONFIGRECORD_H
