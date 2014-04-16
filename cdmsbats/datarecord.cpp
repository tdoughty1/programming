#include "datarecord.h"

DataRecord::DataRecord()
{
    _InitValues();
}

DataRecord::DataRecord(bool debug=false)
{
    _InitValues();

    if(debug)
    {
        _PrintLine();
    }
}

DataRecord::~DataRecord()
{
    //dtor
}

void DataRecord::ReadRecord(CDMSRawFileStream* filePtr, int RecordLength, bool debug)
{

    cout << "In DataRecord::ReadRecord" << endl;
    cout << "Debug value = " << debug << endl;

    uint32_t *Record;
    Record = new uint32_t[RecordLength/4];

    filePtr->ReadWords(RecordLength, Record);

    StoreValues(Record);

    if(debug)
    {
        PrintValues();
    }
}
