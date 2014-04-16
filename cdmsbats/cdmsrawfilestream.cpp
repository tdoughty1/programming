#include <string>
#include <iostream>
#include <iomanip>
#include <zlib.h>
#include "cdmsrawfilestream.h"

using namespace std;

CDMSRawFileStream::CDMSRawFileStream(string fName, string mode="rb")
{
    _FileName = fName;


    if(fName.compare("") == 0)
    {
        _FileStream = NULL;
        _Open = false;
    }
    else
    {
        Open(fName,mode);
        _Open = true;
    }
}

CDMSRawFileStream::~CDMSRawFileStream()
{
    Close();
}

int CDMSRawFileStream::Open(string fName, string mode)
{
    _FileStream = gzopen(fName.c_str(),"rb");

    if(_FileStream == NULL)
    {
        cout << "Error opening file " << fName << endl;
        return 1;
    }
    else
    {
        _FileName = fName;
        _Open = true;
        return 0;
    }
}

int CDMSRawFileStream::Close()
{
    if(_Open)
    {

        int close_check = gzclose(_FileStream);

        if(close_check != 0)
        {
            cout << "Error closing file " << _FileName;
            return 1;
        }
        else
        {
            return close_check;
        }
    }
    else
    {
        cout << "Warning in CDMSRawFileStream::Close:" << endl;
        cout << "No current filestream open. No action taken." << endl;
        return 1;
    }
}

int CDMSRawFileStream::Tell()
{
    if(_Open)
    {
        return gztell(_FileStream);
    }
    else
    {
        cout << "Warning in CDMSRawFileStream::Tell:" << endl;
        cout << "No currently opened file in stream." << endl;
        return -1;
    }
}

int CDMSRawFileStream::Seek(int nPos)
{
    if(_Open)
    {
        gzseek(_FileStream, nPos, 0);
        return 0;
    }
    else
    {
        cout << "Warning in CDMSRawFileStream::Seek:" << endl;
        cout << "No currently opened file in stream." << endl;
        return 1;
    }
}

int CDMSRawFileStream::Skip(int nPos)
{
    if(_Open)
    {
        gzseek(_FileStream, nPos, SEEK_CUR);
        return 0;
    }
    else
    {
        cout << "Warning in CDMSRawFileStream::Seek:" << endl;
        cout << "No currently opened file in stream." << endl;
        return 1;
    }
}

//TODO Add Template Metaprogramming

void CDMSRawFileStream::ReadWords(int nBytes, uint32_t* ArrayPtr)
{
    if(_Open)
    {

        int bytesRead = gzread(_FileStream, ArrayPtr, nBytes);

        if(bytesRead == -1)
        {
            cout << "ERROR in CDMSRawFileStream::ReadWords:" << endl;
            cout << "Problem reading from file " << _FileName << endl;
            exit(EXIT_FAILURE);
        }

        return;
    }
    else
    {
        cout << "ERROR in CDMSRawFileStream::ReadWords:" << endl;
        cout << "No open file to read from" << endl;
        exit(EXIT_FAILURE);
    }
}
