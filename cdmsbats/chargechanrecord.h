#ifndef CHARGECHANRECORD_H
#define CHARGECHANRECORD_H

#include "datarecord.h"


class ChargeChanRecord : public DataRecord
{
    public:

        /** Default constructor */
        ChargeChanRecord();

        /** Default destructor */
        virtual ~ChargeChanRecord(){};

        void StoreValues(int32_t*);

        void PrintValues();

    protected:

    private:

        int _detCode;
        int _towerNum;
        float _driverGain;
        float _chanBias;
        float _rtfOffset;
        float _deltat;
        float _t0;
        int _traceLength;
};

#endif // CHARGECHANRECORD_H
