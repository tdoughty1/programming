#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <zlib.h>
#include <stdint.h>
using namespace std;

int main ()
{
    cout << "START" << endl;

    gzFile fgzRawDataPtr;
    fgzRawDataPtr = gzopen("/home/tdoughty1/Workspace/data/raw/01120411_1132/01120411_1132_F0003.gz","rb");

    if(fgzRawDataPtr == NULL)
    {
        cout << "ERROR: Reading File '/home/tdoughty1/Workspace/data/raw/01120411_1132/01120411_1132_F0003.gz'" << endl;
    }
    else
    {
        cout << "Correctly Read '/home/tdoughty1/Workspace/data/raw/01120411_1132/01120411_1132_F0003.gz'" << endl;
    }

    int nread = 4;
    uint32_t header[nread];

    int readcheck = gzread(fgzRawDataPtr, header, nread*sizeof(int32_t));

    if(readcheck == -1)
    {
        cout << "ERROR: Reading Header Entries";
    }
    else
    {
        cout << setbase(16) << "Endian Check = 0x" << header[0] << endl;
        cout << setbase(16) << "File Header = 0x" << header[1] << endl;
        cout << setbase(16) << "Config Header = 0x" << header[2] << endl;
        cout << setbase(10) << "Config Length = " << header[3] << endl;
    }

    ////////////////////////////////////////////////////////////////////////////////////////////
    // Read Detector Config Info
    ////////////////////////////////////////////////////////////////////////////////////////////
    for(int i=0;i<180;i++)
    {
        uint32_t buffer[2];

        readcheck = gzread(fgzRawDataPtr, buffer, 2*sizeof(int32_t));
        if(readcheck == -1)
        {
            cout << "ERROR: Reading Channel Config Entries";
        }
        else
        {
            cout << "Checking Channel Config Header" << endl;

            if(buffer[0]==65537)
            {
                cout << "Found Phonon Config Settings" << endl;
                cout << setbase(16) << "Phonon Config Header = " << buffer[0] << endl;
                cout << setbase(10) << "Phonon Config Length = " << buffer[1] << endl;

                int32_t pbuffer[buffer[1]];

                readcheck = gzread(fgzRawDataPtr, pbuffer, buffer[1]);
                if(readcheck == -1)
                {
                    cout << "ERROR: Reading Phonon Config Settings" << endl;;
                }
                else
                {
                    cout << "Reading Phonon Config Settings" << endl;
                    cout << setbase(10) << "Detector Code = " << pbuffer[0] << endl;
                    cout << setbase(10) << "Detector Type = " << pbuffer[0]/1000000 << endl;
                    cout << setbase(10) << "Detector Number = " << (pbuffer[0]%1000000)/1000 << endl;
                    cout << setbase(10) << "Channel Number = " << pbuffer[0]%1000 << endl;
                    cout << setbase(10) << "Tower Number = " << pbuffer[1] << endl;
                    cout << setbase(10) << "Driver Gain = " << pbuffer[2]/100 << endl;
                    cout << setbase(10) << "QET bias = " << pbuffer[3]/100 << endl;
                    cout << setbase(10) << "Squid bias = " << pbuffer[4]/100 << endl;
                    cout << setbase(10) << "Squid Lockpoint = " << pbuffer[5]/100 << endl;
                    cout << setbase(10) << "RTF Offset = " << pbuffer[6] << endl;
                    cout << setbase(10) << "Variable Gain = " << pbuffer[7] << endl;
                    cout << setbase(10) << "Delta T = " << pbuffer[8] << endl;
                    cout << setbase(10) << "TO = " << pbuffer[9] << endl;
                    cout << setbase(10) << "Trace Length = " << pbuffer[10] << endl;
                } //Successfully read Phonon Record
            }
            else if(buffer[0] == 65538)
            {
                cout << "Found Charge Config Settings" << endl;
                cout << setbase(16) << "Charge Config Header = " << buffer[0] << endl;
                cout << setbase(10) << "Charge Config Length = " << buffer[1] << endl;

                int32_t qbuffer[buffer[1]];

                int readcheck = gzread(fgzRawDataPtr, qbuffer, buffer[1]);
                if(readcheck == -1)
                {
                    cout << "ERROR: Reading Charge Config Settings" << endl;
                }
                else
                {
                    cout << "Reading Charge Config Settings" << endl;
                    cout << setbase(10) << "Detector Code = " << qbuffer[0] << endl;
                    cout << setbase(10) << "Detector Type = " << qbuffer[0]/1000000 << endl;
                    cout << setbase(10) << "Detector Number = " << (qbuffer[0]%1000000)/1000 << endl;
                    cout << setbase(10) << "Channel Number = " << qbuffer[0]%1000 << endl;
                    cout << setbase(10) << "Tower Number = " << qbuffer[1] << endl;
                    cout << setbase(10) << "Driver Gain = " << qbuffer[2]/100 << endl;
                    cout << setbase(10) << "Voltage bias = " << qbuffer[3]/100 << endl;
                    cout << setbase(10) << "RTF Offset = " << qbuffer[4] << endl;
                    cout << setbase(10) << "Delta T = " << qbuffer[5] << endl;
                    cout << setbase(10) << "TO = " << qbuffer[6] << endl;
                    cout << setbase(10) << "Trace Length = " << qbuffer[7] << endl;
                } // Successfully Read Charge Settings
            }
            else
            {
                cout << "ERROR: Unknown Channel Configuration" << endl;
                cout << setbase(16) << "Value = " << buffer[0];
                exit(1);
            } // Channel Configuration Check
        } // Successfully Read Config Header
    } // Looped over 180 Channels

    ////////////////////////////////////////////////////////////////////////////////////////////
    // Read Event Info
    ////////////////////////////////////////////////////////////////////////////////////////////

    nread = 2;
    uint32_t eheader[nread];

    readcheck = gzread(fgzRawDataPtr, eheader, nread*sizeof(int32_t));

    if(readcheck == -1)
    {
        cout << "ERROR: Reading Event Header" << endl;
    }
    else
    {
        cout << "Event Header Successfully Read" << endl;
        cout << setbase(16) << "Event Header = " << eheader[0] << endl;
        cout << setbase(16) << "Event Tag = " << (eheader[0]>>16) << endl;
        cout << setbase(16) << "Event Class = " << (eheader[0] & 0x0000F000) << endl;
        cout << setbase(16) << "Event Category = " << (eheader[0] & 0x00000F00) << endl;
        cout << setbase(16) << "Event Type = " << (eheader[0] & 0x000000FF) << endl;
        cout << setbase(10) << "Event Length = " << eheader[1] << endl;

        if(eheader[0]>>16 != 0xa980)
        {
            cout << "ERROR in Event Header: Unknown Event Tag" << endl;
        }
        else
        {
            for(int i=0; i<2; i++)
            {

                int nread = 2;
                int32_t lheader[nread];

                int readcheck = gzread(fgzRawDataPtr,lheader,nread*sizeof(int32_t));

                if(readcheck == -1)
                {
                    cout << "ERROR: Reading Logical Header" << endl;
                }
                else
                {
                    cout << "Reading Logical Header" << endl;
                    cout << setbase(16) << "Logical Header ID = " << lheader[0] << endl;
                    cout << setbase(10) << "Logical Header Length = " << lheader[1] << endl;

                    if(lheader[0] == 0x2)
                    {
                        uint32_t abuffer[lheader[1]];

                        int readcheck = gzread(fgzRawDataPtr,abuffer,lheader[1]);

                        if(readcheck == -1)
                        {
                            cout << "Error Reading Admin Record" << endl;
                        }
                        else
                        {
                            cout << "Reading Admin Record" << endl;
                            cout << "Series Number Date = " << abuffer[0] << endl;
                            cout << "Series Number Time = " << abuffer[1] << endl;
                            cout << "Event Number = " << abuffer[2] << endl;
                            cout << "Event Time = " << abuffer[3] << endl;
                            cout << "Time Since Last Event = " << abuffer[4] << endl;
                            cout << "Livetime Since Last Event = " << abuffer[5] << endl;
                        }
                    }
                    else if(lheader[0] == 0x80)
                    {
                        uint32_t tbuffer[lheader[1]];

                        int readcheck = gzread(fgzRawDataPtr,tbuffer,lheader[1]);

                        if(readcheck == -1)
                        {
                            cout << "Error Reading Trigger Record" << endl;
                        }
                        else
                        {
                            cout << "Reading Trigger Record" << endl;
                            cout << "Trigger Time = " << tbuffer[0] << endl;
                            for(int j=1; j<=6; j++)
                            {
                                cout << "Trigger Mask " << setbase(10) << j << " = " << setbase(16) << tbuffer[j] << endl;
                            }
                        }
                    }
                    else
                    {
                        cout << "Unimplemented Logical Record" << endl;
                        exit(1);
                    }
                }
            }
        } // Correctly formatted event header
    }
    gzclose(fgzRawDataPtr);
}
