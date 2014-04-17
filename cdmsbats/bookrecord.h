#ifndef BOOKRECORD_H
#define BOOKRECORD_H

#include "datarecord.h"


class BookRecord : public DataRecord
{
    public:
        /** Default constructor */
        BookRecord();

        /** Default destructor */
        virtual ~BookRecord(){};

        void StoreValues(int32_t*);

        void PrintValues();

    protected:
    private:

        int _digBaseAddress;
        int _digChannel;
        int _detCode;
};

#endif // BOOKRECORD_H
