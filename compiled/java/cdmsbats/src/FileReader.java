/**
 * 
 */

import batcommon.datareader.CDMSRawFileStream;
import batcommon.datareader.DetectorConfigRecord;

/**
 * @author tdoughty1
 *
 */
public class FileReader {
	
	public static void main(String[] args) {
		
		String gzFile = "/home/tdoughty1/Workspace/data/raw/01120411_1132/01120411_1132_F0002.gz";
		CDMSRawFileStream fgzRawDataPtr = new CDMSRawFileStream();
		DetectorConfigRecord DetectorConfigPtr = new DetectorConfigRecord();
		boolean debug = true;
		
		final long startTime = System.currentTimeMillis();
		
		fgzRawDataPtr.Open(gzFile, "rb");
		
		int mode = 0;
		int[] FileHeader = fgzRawDataPtr.ReadWords(2, mode);
		
		if(debug) {

			System.out.printf("Endian Check = 0x%x\n", FileHeader[0]);
			System.out.printf("File Header = 0x%x\n", FileHeader[1]);
		}
		
		int[] ConfigHeader = fgzRawDataPtr.ReadWords(2, mode);
		
		if(debug) {
		
			System.out.printf("Config Header = 0x%x\n", ConfigHeader[0]);
			System.out.printf("Config Record Length = %d\n", ConfigHeader[1]);
		}
		
		DetectorConfigPtr.ReadRecord(fgzRawDataPtr, ConfigHeader[1], debug);
		
		fgzRawDataPtr.Close();
		
		final long endTime = System.currentTimeMillis();

		System.out.printf("Read record in %d ms\n", (endTime-startTime));		
	}
}
