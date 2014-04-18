#ifndef CDMSRAWFILESTREAM_H
#define CDMSRAWFILESTREAM_H

#include <string>

#include <zlib.h>

using namespace std;

class CDMSRawFileStream
{
    public:
        /** Default constructor */
        CDMSRawFileStream();

        /** Constructer with file open */
        CDMSRawFileStream(string, string);

        /** Default destructor */
        virtual ~CDMSRawFileStream();

        int Open(string, string);

        int Close();

        int Tell();

        int Seek(int);

        int Skip(int);

        // Overloaded function
        void ReadWords(int, int32_t*);

        void ReadWords(int, uint32_t*);

        void ReadWords(int, uint16_t*);

    protected:

    private:
        string _FileName = "";
        gzFile _FileStream = NULL;
        bool _Open = false;

};

#endif // CDMSRAWFILESTREAM_H
