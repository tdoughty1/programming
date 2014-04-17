#include "datarecord.h"

void DataRecord::ReadRecord(CDMSRawFileStream* filePtr, int RecordLength, bool debug)
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
