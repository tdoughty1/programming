#ifndef TRACERECORD_H
#define TRACERECORD_H

#include <vector>

#include "cdmsrawfilestream.h"
#include "tracerecord.h"
#include "bookrecord.h"
#include "timerecord.h"


class TraceRecord : public DataRecord
{
    public:
        /** Default constructor */
        TraceRecord();

        /** Default destructor */
        virtual ~TraceRecord(){};

        void ReadRecord(CDMSRawFileStream*, int, bool);

        void StoreValues(int32_t*){};

        void PrintValues(){};

    protected:
    private:

        BookRecord* _BookPtr;
        TimeRecord* _TimePtr;
        uint16_t* _Trace[];
};

#endif // TRACERECORD_H
