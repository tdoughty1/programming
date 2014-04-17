#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <string>
#include <typeinfo>
#include <stdint.h>
#include <time.h>
#include <zlib.h>
#include "histsubrecord.h"

// Primary Function Call for data record
void HistSubRecord::ReadRecord(int32_t* Record, int index, bool debug=false)
{
    int start;

    // Get number of times stored
    _nTimes = Record[index];
    index++;

    // Store number of times
    for(int i=0; i < _nTimes; i++)
    {
        _Times[i] = Record[index];
        index++;
    }

    // Get number of masks stored
    _nMasks = Record[index];
    index++;

    // Store all masks for all times
    for(int i=0; i < _nTimes; i++)
    {
        for(int j=0; i < _nMasks; i++)
        {
            _Masks[i][j] = Record[index];
            index++;
        }
    }
}

void HistSubRecord::PrintValues()
{
    for(int i=0; i < _nTimes; i++)
    {
        cout << "time " << (i+1) << " = " << _Times[i] << endl;

        for(int j=0; j < _nMasks; j++)
        {
            cout << "time " << (i+1) << " - mask " << (j+1);
            cout << " = 0x" << setbase(16) << _Masks[i][j] << endl;
        }
    }
}
