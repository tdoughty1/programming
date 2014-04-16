#ifndef CDMSRAWFILESTREAM_H
#define CDMSRAWFILESTREAM_H

#include <string>
#include <iostream>
#include <iomanip>

#include <zlib.h>

using namespace std;

class CDMSRawFileStream
{
    public:
        /** Default constructor */
        CDMSRawFileStream();

        /** Constructer with file open */
        CDMSRawFileStream(string fname, string mode);

        /** Default destructor */
        virtual ~CDMSRawFileStream();

        int Open(string fName, string mode);

        int Close();

        int Tell();

        int Seek(int nPos);

        int Skip(int nPos);

        int ReadWords(int nBytes, uint32_t* ArrayPtr);

    protected:

    private:
        string _FileName = "";
        gzFile _FileStream = NULL;
        bool _Open = false;

};

#endif // CDMSRAWFILESTREAM_H
