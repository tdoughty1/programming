#ifndef PHONONCHANRECORD_H
#define PHONONCHANRECORD_H

#include "datarecord.h"


class PhononChanRecord : public DataRecord
{
    public:

        void StoreValues(uint32_t*);

        void PrintValues();

    protected:

    private:

        void _InitValues();

        void _PrintLine(){cout << "Found Phonon Channel Record" << endl;}

        int _detCode;
        int _towerNum;
        float _driverGain;
        float _qetBias;
        float _squidBias;
        float _lockPoint;
        float _rtfOffset;
        int _varGain;
        float _deltat;
        float _t0;
        int _traceLength;
};

#endif // PHONONCHANRECORD_H
