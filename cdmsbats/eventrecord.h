#ifndef EVENTRECORD_H
#define EVENTRECORD_H

#include "datarecord.h"
#include "adminrecord.h"
#include "triggerrecord.h"
#include "tlbrecord.h"
#include "gpsrecord.h"
#include "tracerecord.h"
#include "historyrecord.h"


class EventRecord : public DataRecord
{
    public:
        /** Default constructor */
        EventRecord();

        /** Default destructor */
        virtual ~EventRecord(){};

        void ReadRecord(CDMSRawFileStream*, int, bool);

        void StoreValues(int32_t*){};

        void PrintValues(){};

    protected:
    private:

        AdminRecord* _AdminPtr;
        TriggerRecord* _TriggerPtr;
        TLBRecord* _TLBPtr;
        GPSRecord* _GPSPtr;
        TraceRecord* _TracePtr;
        HistoryRecord* _HistoryPtr;
};

#endif // EVENTRECORD_H
