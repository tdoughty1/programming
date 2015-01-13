/**
 * 
 */
package batcommon.datareader;

import batcommon.datareader.DataRecord;
import batcommon.datareader.PhononChanRecord;
import batcommon.datareader.ChargeChanRecord;

/**
 * @author tdoughty1
 *
 */
public class DetectorConfigRecord extends DataRecord {

	private PhononChanRecord _pChanPtr;
	private ChargeChanRecord _qChanPtr;
	
	public DetectorConfigRecord(){
		
		_pChanPtr = new PhononChanRecord();
		_qChanPtr = new ChargeChanRecord();
	}
    
	public void ReadRecord(CDMSRawFileStream filePtr, int RecordLength){
		
        int endPos = filePtr.Tell() + RecordLength;
        
        while(filePtr.Tell() < endPos) {

        	int mode = 0;
            int[] ChanHeader = filePtr.ReadWords(4*2, mode);

            // Record of No length
            if(ChanHeader[1] == 0) {
                continue;
            }

            // Phonon Record
            if(ChanHeader[0] == 0x10001) {
                _pChanPtr.ReadRecord(filePtr, ChanHeader[1], mode);
                continue;
            }

            // Charge Record
            if(ChanHeader[0] == 0x10002) {
                _qChanPtr.ReadRecord(filePtr, ChanHeader[1], mode);
                continue;
            }

            System.out.println("Found unexpected trace header");
            System.exit(1);
        }
	}
	
	public void ReadRecord(CDMSRawFileStream filePtr, int RecordLength, boolean debug){
		
        int endPos = filePtr.Tell() + RecordLength;
        
        while(filePtr.Tell() < endPos) {

        	int mode = 0;
            int[] ChanHeader = filePtr.ReadWords(4*2, mode);

            if(debug) {
                System.out.printf("Channel Header = 0x%x\n", ChanHeader[0]);
                System.out.printf("Channel Length = %d\n", ChanHeader[1]);
            }

            // Record of No length
            if(ChanHeader[1] == 0) {
                continue;
            }

            // Phonon Record
            if(ChanHeader[0] == 0x10001) {
                _pChanPtr.ReadRecord(filePtr, ChanHeader[1], mode, debug);
                continue;
            }

            // Charge Record
            if(ChanHeader[0] == 0x10002) {
                _qChanPtr.ReadRecord(filePtr, ChanHeader[1], mode, debug);
                continue;
            }

            System.out.println("Found unexpected trace header");
            System.exit(1);
        }
	}
}

