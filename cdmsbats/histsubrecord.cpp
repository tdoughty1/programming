#include <iostream>
#include <iomanip>

#include "histsubrecord.h"

using namespace std;

// Primary Function Call for data record
void HistSubRecord::ReadRecord(CDMSRawFileStream* filePtr, bool debug=false)
{
    // Get number of times stored
    int32_t nT[1];
    filePtr->ReadWords(4, nT);
    _nTimes = nT[0];

    /////////////////////////////////////////////////////
    // Store times
    /////////////////////////////////////////////////////
    int32_t tempTArray[_nTimes];
    filePtr->ReadWords(_nTimes*4, tempTArray);
    _Times.resize(_nTimes);

    for(int i=0; i<_nTimes; i++)
    {
        _Times.at(i) = tempTArray[i];
    }

    // Get number of masks stored
    int32_t nM[1];
    filePtr->ReadWords(4, nM);
    _nMasks = nM[0];

    /////////////////////////////////////////////////////
    // Store all masks for each time
    /////////////////////////////////////////////////////

    // Define temporary array and vector for convenience
    uint32_t tempMArray[_nMasks];
    vector<uint32_t> tempVec;

    for(int i=0; i < _nTimes; i++)
    {
        // Get array of Masks
        filePtr->ReadWords(_nMasks*4, tempMArray);

        // Store Masks in a vector
        for(int j=0; j < _nMasks; j++)
        {
            tempVec.push_back(tempMArray[j]);
        }
        _Masks.push_back(tempVec);
        tempVec.clear();
    }
}

void HistSubRecord::PrintValues()
{
    for(int i=0; i < _nTimes; i++)
    {
        cout << "time " << setbase(10) << (i+1) << " = " << _Times[i] << endl;

        for(int j=0; j < _nMasks; j++)
        {
            cout << "time " << setbase(10) << (i+1) << " - mask " << (j+1);
            cout << " = 0x" << setbase(16) << _Masks[i][j] << endl;
        }
    }
}
