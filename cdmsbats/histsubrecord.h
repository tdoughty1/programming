#ifndef HISTSUBRECORD_H
#define HISTSUBRECORD_H

class HistSubRecord : public DataRecord
{
    public:
        /** Default constructor */
        HistSubRecord();

        /** Default destructor */
        virtual ~HistSubRecord(){};

        void ReadRecord(CDMSRawFileStream*, int, bool);

        void StoreValues(int32_t*){};

        void PrintValues(){};

    protected:
    private:

        BookRecord* _BookPtr;
        TimeRecord* _TimePtr;
        uint* _Trace[];
};

#endif // HISTSUBRECORD_H
