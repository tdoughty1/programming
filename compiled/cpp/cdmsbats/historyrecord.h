#ifndef HISTORYRECORD_H
#define HISTORYRECORD_H

#include "datarecord.h"
#include "histsubrecord.h"


class HistoryRecord : public DataRecord
{
    public:
        /** Default constructor */
        HistoryRecord();

        /** Default destructor */
        virtual ~HistoryRecord(){};

        void ReadRecord(CDMSRawFileStream*, int, bool);

        void StoreValues(int32_t*){};

        void StoreValues(uint32_t*){};

        void PrintValues();

    protected:

    private:

        HistSubRecord* _VetoPtr;
        HistSubRecord* _TrigPtr;

};

#endif // HISTORYRECORD_H
