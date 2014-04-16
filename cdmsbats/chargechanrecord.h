#ifndef CHARGECHANRECORD_H
#define CHARGECHANRECORD_H

#include "datarecord.h"


class ChargeChanRecord : public DataRecord
{
    public:

        void StoreValues(uint32_t* Record);

        void PrintValues();

    protected:

    private:

        void _InitValues();

        void _PrintLine(){cout << "Found Charge Channel Record" << endl;}

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
