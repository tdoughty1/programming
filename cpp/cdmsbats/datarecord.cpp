#include <string>

#include "datarecord.h"

void DataRecord::ReadRecord(CDMSRawFileStream* filePtr, int RecordLength, uint32_t mode, bool debug)
{
    uint32_t *Record;
    Record = new uint32_t[RecordLength/4];

    filePtr->ReadWords(RecordLength, Record);

    StoreValues(Record);

    if(debug)
    {
        PrintValues();
    }
}

void DataRecord::ReadRecord(CDMSRawFileStream* filePtr, int RecordLength, int32_t mode, bool debug)
{
    int32_t *Record;
    Record = new int32_t[RecordLength/4];

    filePtr->ReadWords(RecordLength, Record);

    StoreValues(Record);

    if(debug)
    {
        PrintValues();
    }
}
