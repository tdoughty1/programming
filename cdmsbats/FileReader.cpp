#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <string>
#include <typeinfo>
#include <stdint.h>
#include <time.h>
#include <zlib.h>

#include "cdmsrawfilestream.h"
#include "detectorconfigrecord.h"
#include "eventrecord.h"

using namespace std;

int main()
{
    DetectorConfigRecord* DetectorConfigPtr = new DetectorConfigRecord();
    EventRecord* EventPtr = new EventRecord();

    string fileName = "/home/tdoughty1/Workspace/data/raw/01120411_1132/01120411_1132_F0003.gz";

    clock_t startTime = clock();

    CDMSRawFileStream* fgzRawDataPtr = new CDMSRawFileStream(fileName, "rb");

    int nread = 2; // FIXME - Remove Hardcoded value?
    int32_t FileHeader[nread];

    fgzRawDataPtr->ReadWords(nread*sizeof(int32_t), FileHeader);
    cout << "Endian Check = 0x" << setbase(16) << FileHeader[0] << endl;
    cout << "File Header = 0x" << setbase(16) << FileHeader[1] << endl;

    int32_t ConfigHeader[nread];

    fgzRawDataPtr->ReadWords(nread*sizeof(int32_t), ConfigHeader);
    cout << setbase(16) << "Config Header = 0x" << ConfigHeader[0] << endl;
    cout << setbase(10) << "Config Length = " << ConfigHeader[1] << endl;

    ////////////////////////////////////////////////////////////////////////////////////////////
    // Read Detector Config Info
    ////////////////////////////////////////////////////////////////////////////////////////////
    DetectorConfigPtr->ReadRecord(fgzRawDataPtr, ConfigHeader[1], false);


    ////////////////////////////////////////////////////////////////////////////////////////////
    // Loop through Events
    ////////////////////////////////////////////////////////////////////////////////////////////

//    int ReadWords = 0;

    //cout << setbase(10) << header[3]/4 << endl;

/**    while(ReadWords < header[3]/4)
    {
        uint32_t buffer[2];

        readcheck = gzread(fgzRawDataPtr, buffer, 2*sizeof(int32_t));
        if(readcheck == -1)
        {
            cout << "ERROR: Reading Channel Config Entries";
            exit(1);
        }
        else
        {
            ReadWords += 2;
            //cout << "Checking Channel Config Header" << endl;

            if(buffer[0]==0x10001) //FIXME - Switch Hardcoded Value to imported constant
            {
                //cout << "Found Phonon Config Settings" << endl;
//                cout << setbase(16) << "Phonon Config Header = " << buffer[0] << endl;
//                cout << setbase(10) << "Phonon Config Length = " << buffer[1] << endl;

                int32_t pbuffer[buffer[1]];
                readcheck = gzread(fgzRawDataPtr, pbuffer, buffer[1]);
                if(readcheck == -1)
                {
                    cout << "ERROR: Reading Phonon Config Settings" << endl;
                    exit(1);
                }
                else
                {
                    ReadWords += buffer[1]/4;
//                    cout << "Reading Phonon Config Settings" << endl;
//                    cout << setbase(10) << "Detector Code = " << pbuffer[0] << endl;
//                    cout << setbase(10) << "Detector Type = " << pbuffer[0]/1000000 << endl;
//                    cout << setbase(10) << "Detector Number = " << (pbuffer[0]%1000000)/1000 << endl;
//                    cout << setbase(10) << "Channel Number = " << pbuffer[0]%1000 << endl;
//                    cout << setbase(10) << "Tower Number = " << pbuffer[1] << endl;
//                    cout << setbase(10) << "Driver Gain = " << pbuffer[2]/100 << endl;
//                    cout << setbase(10) << "QET bias = " << pbuffer[3]/100 << endl;
//                    cout << setbase(10) << "Squid bias = " << pbuffer[4]/100 << endl;
//                    cout << setbase(10) << "Squid Lockpoint = " << pbuffer[5]/100 << endl;
//                    cout << setbase(10) << "RTF Offset = " << pbuffer[6] << endl;
//                    cout << setbase(10) << "Variable Gain = " << pbuffer[7] << endl;
//                    cout << setbase(10) << "Delta T = " << pbuffer[8] << endl;
//                    cout << setbase(10) << "TO = " << pbuffer[9] << endl;
//                    cout << setbase(10) << "Trace Length = " << pbuffer[10] << endl;
                } //Successfully read Phonon Record
            }
            else if(buffer[0] == 0x10002) //FIXME - Switch Hardcoded Value to imported constant
            {
//                cout << "Found Charge Config Settings" << endl;
//                cout << setbase(16) << "Charge Config Header = " << buffer[0] << endl;
//                cout << setbase(10) << "Charge Config Length = " << buffer[1] << endl;

                int32_t qbuffer[buffer[1]];
                int readcheck = gzread(fgzRawDataPtr, qbuffer, buffer[1]);
                if(readcheck == -1)
                {
                    cout << "ERROR: Reading Charge Config Settings" << endl;
                    exit(1);
                }
                else
                {
                    ReadWords += buffer[1]/4;
//                    cout << "Reading Charge Config Settings" << endl;
//                    cout << setbase(10) << "Detector Code = " << qbuffer[0] << endl;
//                    cout << setbase(10) << "Detector Type = " << qbuffer[0]/1000000 << endl;
//                    cout << setbase(10) << "Detector Number = " << (qbuffer[0]%1000000)/1000 << endl;
//                    cout << setbase(10) << "Channel Number = " << qbuffer[0]%1000 << endl;
//                    cout << setbase(10) << "Tower Number = " << qbuffer[1] << endl;
//                    cout << setbase(10) << "Driver Gain = " << qbuffer[2]/100 << endl;
//                    cout << setbase(10) << "Voltage bias = " << qbuffer[3]/100 << endl;
//                    cout << setbase(10) << "RTF Offset = " << qbuffer[4] << endl;
//                    cout << setbase(10) << "Delta T = " << qbuffer[5] << endl;
//                    cout << setbase(10) << "TO = " << qbuffer[6] << endl;
//                    cout << setbase(10) << "Trace Length = " << qbuffer[7] << endl;
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
    int EventNumber = 0;
    while(gzeof(fgzRawDataPtr) == 0)
    {
        nread = 2;
        uint32_t eheader[nread];

        readcheck = gzread(fgzRawDataPtr, eheader, nread*sizeof(int32_t));

        if(readcheck == -1)
        {
            cout << "ERROR: Reading Event Header" << endl;
            exit(1);
        }
        else
        {
            EventNumber++;
            if(gzeof(fgzRawDataPtr) != 0)
            {
                continue;
            }
            //cout << "Reading Event Number " << setbase(10) << EventNumber << endl;
            //cout << "Event Header Successfully Read" << endl;
            //cout << setbase(16) << "Event Header = " << eheader[0] << endl;
            //cout << setbase(16) << "Event Tag = " << (eheader[0]>>16) << endl;
            //cout << setbase(16) << "Event Class = " << (eheader[0] & 0x0000F000) << endl;
            //cout << setbase(16) << "Event Category = " << (eheader[0] & 0x00000F00) << endl;
            //cout << setbase(16) << "Event Type = " << (eheader[0] & 0x000000FF) << endl;
            //cout << setbase(10) << "Event Length = " << eheader[1] << endl;

            if(eheader[0]>>16 != 0xa980) //FIXME - Switch Hardcoded Value to imported constant
            {
                cout << "ERROR in Event Header: Unknown Event Tag" << endl;
                exit(1);
            }
            else
            {
                for(int i=0; i<185; i++) // FIXME - Remove Hardcoded value! Switch to while loop?
                {
                    //cout << "i = " << setbase(10) << i << endl;

                    int nread = 2;
                    int32_t lheader[nread];

                    int readcheck = gzread(fgzRawDataPtr,lheader,nread*sizeof(int32_t));
                    if(readcheck == -1)
                    {
                        cout << "ERROR: Reading Logical Header" << endl;
                        exit(1);
                    }
                    else
                    {
                        //cout << "Reading Logical Header" << endl;
//                        cout << setbase(16) << "Logical Header ID = " << lheader[0] << endl;
//                        cout << setbase(10) << "Logical Header Length = " << lheader[1] << endl;

                        if (lheader[1] == 0)
                        {
                            //cout << setbase(16) << "Skipping Record for Type 0x" << lheader[0] << endl;
                            continue;
                        } // Skip if record length is 0 because not implemented (ie GPS)
                        else if(lheader[0] == 0x2) //FIXME - Switch Hardcoded Value to imported constant
                        {
                            uint32_t abuffer[lheader[1]/4];

                            int readcheck = gzread(fgzRawDataPtr,abuffer,lheader[1]);
                            if(readcheck == -1)
                            {
                                cout << "Error Reading Admin Record" << endl;
                                exit(1);
                            }
                            else
                            {
                                //cout << "Reading Admin Record" << endl;
//                                cout << "Series Number Date = " << abuffer[0] << endl;
//                                cout << "Series Number Time = " << abuffer[1] << endl;
//                                cout << "Event Number = " << abuffer[2] << endl;
//                                cout << "Event Time = " << abuffer[3] << endl;
//                                cout << "Time Since Last Event = " << abuffer[4] << endl;
//                                cout << "Livetime Since Last Event = " << abuffer[5] << endl;
                            }
                        } // End of Admin Record Implementation
                        else if(lheader[0] == 0x80) //FIXME - Switch Hardcoded Value to imported constant
                        {
                            uint32_t tbuffer[lheader[1]/4];

                            int readcheck = gzread(fgzRawDataPtr,tbuffer,lheader[1]);
                            if(readcheck == -1)
                            {
                                cout << "Error Reading Trigger Record" << endl;
                                exit(1);
                            }
                            else
                            {
                                //cout << "Reading Trigger Record" << endl;
//                                cout << "Trigger Time = " << tbuffer[0] << endl;
//                                for(int j=1; j<=6; j++)
//                                {
//                                    cout << "Trigger Mask " << setbase(10) << j << " = " << setbase(16) << tbuffer[j] << endl;
//                                }
                            }
                        } // End of Trigger Record Implementation
                        else if(lheader[0] == 0x81) //FIXME - Switch Hardcoded Value to imported constant
                        {
                            uint32_t tbuffer[lheader[1]/4];

                            int readcheck = gzread(fgzRawDataPtr,tbuffer,lheader[1]);
                            if(readcheck == -1)
                            {
                                cout << "Error Reading Trigger Mask Record" << endl;
                                exit(1);
                            }
                            else
                            {
                                //cout << "Reading Trigger Mask Record" << endl;
                                for(int j=0; j<6; j++)
                                {
                                    cout << "TLB Mask " << setbase(10) << j+1 << " = " << setbase(16) << tbuffer[j] << endl;
                                }
                            }
                        } // End of Trigger Logic Board Record Implementation
                        else if(lheader[0] == 0x60) //FIXME - Switch Hardcoded Value to imported constant
                        {
                            uint32_t gbuffer[lheader[1]/4];

                            int readcheck = gzread(fgzRawDataPtr,gbuffer,lheader[1]);
                            if(readcheck == -1)
                            {
                                cout << "Error Reading GPS Record" << endl;
                                exit(1);
                            }
                            else
                            {10**
                                //cout << "Reading GPS Record" << endl;
//                                cout << "GPS Date = " << setbase(16) << gbuffer[0] << endl;
//                                cout << "GPS Time = " << setbase(16) << gbuffer[2] << endl;
//                                cout << "GPS us = " << setbase(16) << gbuffer[3] << endl;
                            }
                        } // End of GPS Trigger Logic
                        else if(lheader[0] == 0x11) //FIXME - Switch Hardcoded Value to imported constant
                        {
                            uint32_t bhbuffer[2];

                            int readcheck = gzread(fgzRawDataPtr,bhbuffer,2*sizeof(uint32_t));

                            if(readcheck == -1)
                            {
                                cout << "Error Reading Trace Bookkeeping Header" << endl;
                                exit(1);
                            }
                            else
                            {
                                //cout << "Reading Trace Bookkeeping Header" << endl;
//                                cout << "Bookkeeping Header = 0x" << setbase(16) << bhbuffer[0] << endl;
//                                cout << "Bookkeeping Length = " << setbase(10) << bhbuffer[1] << endl;

                                uint32_t bbuffer[bhbuffer[1]/4];

                                int readcheck = gzread(fgzRawDataPtr,bbuffer,bhbuffer[1]);
                                if(readcheck == -1)
                                {
                                    cout << "Error Reading Trace Bookkeeping Record" << endl;
                                    exit(1);
                                }
                                else
                                {
                                    //cout << "Reading Trace Bookkeeping Record" << endl;
                                    cout << "Digitizer Base Address = " << setbase(16) << bbuffer[0] << endl;
//                                    cout << "Digitizer Channel = " << setbase(10) << bbuffer[1] << endl;
//                                    cout << "Detector Code = " << setbase(10) << bbuffer[2] << endl;
                                }
                            } // End of Tracebookkeeping Record

                            uint32_t tbbuffer[2];

                            readcheck = gzread(fgzRawDataPtr,tbbuffer,2*sizeof(uint32_t));

                            if(readcheck == -1)
                            {
                                cout << "Error Reading Timebase Header" << endl;
                                exit(1);
                            }
                            else
                            {
                                //cout << "Reading Timebase Header" << endl;
//                                cout << "Timebase Header = 0x" << setbase(16) << tbbuffer[0] << endl;
//                                cout << "Timebase Length = " << setbase(10) << tbbuffer[1] << endl;

                                uint32_t trbuffer[tbbuffer[1]/4];

                                int readcheck = gzread(fgzRawDataPtr,trbuffer,tbbuffer[1]);
                                if(readcheck == -1)
                                {
                                    cout << "Error Reading Timebase Record" << endl;
                                    exit(1);
                                }
                                else
                                {
                                    //cout << "Reading Timebase Record" << endl;
                                    cout << "t0 = " << setbase(10) << (int32_t) trbuffer[0] << endl;
                                    cout << "delta t = " << setbase(10) << trbuffer[1] << endl;
                                    cout << "nsamples = " << setbase(10) << trbuffer[2] << endl;
                                }
                            } // End of time base

                            uint32_t theader[2];

                            readcheck = gzread(fgzRawDataPtr,theader,2*sizeof(uint32_t));

                            if(readcheck == -1)
                            {
                                cout << "Error Reading Trace Header" << endl;
                                exit(1);
                            }
                            else
                            {
                                //cout << "Reading Trace Header"  << endl;
                                //cout << "Trace Header = 0x" << setbase(16) << theader[0] << endl;
                                //cout << "Number of Samples = " << setbase(10) << theader[1] << endl;

                                int32_t pbuffer[theader[1]/2];

                                int readcheck = gzread(fgzRawDataPtr,pbuffer,theader[1]*2);
                                if(readcheck == -1)
                                {
                                    cout << "Error Reading Pulse" << endl;
                                    exit(1);
                                }
                                else
                                {
                                    //cout << "Reading Pulse" << endl;
                                    //for(int j=0;j<204;j++)
                                    //{
                                    //    cout << "Pulse Record Value = " << pbuffer[j] << endl;
                                    //    cout << "Upper Half (Sample " << (2*j) << ") = " << (pbuffer[j]>>16) << endl;
                                    //    cout << "Lower Half (Sample " << (2*j + 1) << ") = " << (pbuffer[j]&0x0000FFFF) << endl;
                                    //}
                                }
                            }

                        } // End of Trace Record
                        else if(lheader[0] == 0x21) //FIXME - Switch Hardcoded Value to imported constant
                        {
                            uint32_t hbuffer[lheader[1]/4];

                            int readcheck = gzread(fgzRawDataPtr,hbuffer,lheader[1]);
                            if(readcheck == -1)
                            {
                                cout << "Error Reading History Buffer Record" << endl;
                                exit(1);
                            }
                            else
                            {
                                //cout << "Reading History Record" << endl;
                                //cout << "Number of Veto Times = " << hbuffer[0] << endl;
//                                f'''or(int j=1; j<=6; j++)
//                                {
//                                    cout << "Trigger Mask " << setbase(10) << j << " = " << setbase(16) << tbuffer[j] << endl;
//                                }
                            }
                        } // End of History Buffer Record
                        else
                        {
                            cout << "Unimplemented Logical Record = 0x" << setbase(16) << lheader[0] << endl;
                            exit(1);
                        }
                    }
                }
            } // Correctly formatted event header
        }
    }*/
    fgzRawDataPtr->Close();

    clock_t endTime = clock();

    cout << "Loading Data took " << setprecision(2) << (float(endTime-startTime)/CLOCKS_PER_SEC) << endl;

    return 0;
}
