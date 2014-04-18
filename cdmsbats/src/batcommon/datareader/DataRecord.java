/**
 * 
 */
package batcommon.datareader;

import batcommon.datareader.CDMSRawFileStream;

/**
 * @author tdoughty1
 *
 */
public class DataRecord {

	// Primary Function Call for data record
    // Overload to provide optional argument support 
	
	void ReadRecord(CDMSRawFileStream filePtr, int RecordLength){
	
		int mode = 0;
		boolean debug = false;
		
        int[] Record = filePtr.ReadWords(RecordLength, mode);

        this.StoreValues(Record);

        if(debug) {
            this.PrintValues();
        }
	}
	
	void ReadRecord(CDMSRawFileStream filePtr, int RecordLength, int mode){
		
		boolean debug = false;
		
        int[] Record = filePtr.ReadWords(RecordLength, mode);

        this.StoreValues(Record);

        if(debug) {
            this.PrintValues();
        }
	}

	void ReadRecord(CDMSRawFileStream filePtr, int RecordLength, boolean debug){
        
		int mode = 0;
		
        int[] Record = filePtr.ReadWords(RecordLength, mode);

        this.StoreValues(Record);

        if(debug) {
            this.PrintValues();
        }
		
	}
	
	void ReadRecord(CDMSRawFileStream filePtr, int RecordLength, int mode, boolean debug){
		
        int[] Record = filePtr.ReadWords(RecordLength, mode);

        this.StoreValues(Record);

        if(debug) {
            this.PrintValues();
        }
	}
	
	// Dummy Function - should be overloaded by Inheriting Classes
	void StoreValues(int[] Record){
	}
	
	// Dummy Function - should be overloaded by Inheriting Classes
	void PrintValues(){
	}
}
