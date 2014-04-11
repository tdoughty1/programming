/**
 * 
 */
package readfile;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.zip.GZIPInputStream;
import java.nio.ByteBuffer;
import java.nio.IntBuffer;
import java.nio.ByteOrder;
import java.io.BufferedInputStream;

/**
 * @author tdoughty1
 *
 */

public class ReadFile {

	/**
	 * @param args
	 * 
	 * 
	 */
	
	private static FileInputStream fis;
	private static GZIPInputStream gis;
	private static BufferedInputStream bis;
	private static int filePos;
	
	private static int[] ReadWord(int nWords){
		
		byte[] byteArray = new byte[nWords*4];
		int[] intArray = new int[nWords];
		
		try {
			
			ReadFile.bis.read(byteArray);
			IntBuffer intBuffer = ByteBuffer.wrap(byteArray).order(ByteOrder.LITTLE_ENDIAN).asIntBuffer();
			intBuffer.get(intArray);
			ReadFile.filePos += nWords*4;
			
			return intArray;
		
		} catch (IOException e) {
			System.out.println("IO error trying to read file!");
			e.printStackTrace();
			return intArray;
		}
	}
	
	
	public static void main(String[] args) {

		String gzFile = "/home/tdoughty1/Workspace/data/raw/01120411_1132/01120411_1132_F0002.gz";
		int endPos;
		
		try {
			
			filePos = 0;
			fis = new FileInputStream(gzFile);
			gis = new GZIPInputStream(fis,256*256);
			bis = new BufferedInputStream(gis,256*256);
			
			final long startTime = System.currentTimeMillis();
			
			int[] FileHeader = ReadFile.ReadWord(2);
			
			//System.out.printf("Endian Check = 0x%x\n", FileHeader[0]);
			//System.out.printf("File Header = 0x%x\n", FileHeader[1]);
			//System.out.printf("Current Position = %d\n", filePos);
			
			int[] ConfigHeader = ReadFile.ReadWord(2);
			
			//System.out.printf("Detector Config Header = 0x%x\n", ConfigHeader[0]);
			//System.out.printf("Detector Config Record Length = %d\n", ConfigHeader[1]);
			//System.out.printf("Current Position = %d\n", filePos);
			
			endPos = ReadFile.filePos + ConfigHeader[1];
			
			////////////////////////////////////////////////////////////////////////////////////////////////
			// Loop through all the channels in Detector Config Record
			////////////////////////////////////////////////////////////////////////////////////////////////
			while(ReadFile.filePos < endPos){

				int[] ConfigRecord = ReadWord(2);

				//System.out.printf("Channel Header = 0x%x\n", ConfigRecord[0]);
				//System.out.printf("Channel Record Length = %d\n", ConfigRecord[1]);
				//System.out.printf("Current Position = %d\n", filePos);
				
				int[] ChanRecord = ReadWord(ConfigRecord[1]/4);
				
				if(ConfigRecord[0] == 0x10001){
					//System.out.println("Found Phonon Channel");

					//System.out.printf("First Entry in Record = 0x%x\n", ChanRecord[0]);
					//System.out.printf("Last Entry in Record = 0x%x\n", ChanRecord[ConfigRecord[1]/4 - 1]);					
					//System.out.printf("Current Position = %d\n", filePos);
					continue;
				}
				
				if(ConfigRecord[0] == 0x10002){
					//System.out.println("Found Charge Channel");

					//System.out.printf("First Entry in Record = 0x%x\n", ChanRecord[0]);
					//System.out.printf("Last Entry in Record = 0x%x\n", ChanRecord[ConfigRecord[1]/4 - 1]);
					//System.out.printf("Current Position = %d\n", ReadFile.filePos);
					continue;
				}
				System.out.println("Found Unknown Channel Type");
				break;
			}
			
			System.out.println("Finished Reading Detector Config");
			
			int nEvent = 0;
			
			while(nEvent<500){ //TODO Remove hard coding!
			
				nEvent++;
				//System.out.printf("Reading Event Number %d\n", nEvent);
				
				int[] EventHeader = ReadWord(2);
			
				//System.out.printf("Event Header = 0x%x\n", EventHeader[0]);
				//System.out.printf("Event Record Length = %d\n", EventHeader[1]);
				//System.out.printf("Current Position = %d\n", filePos);
			
				endPos = filePos + EventHeader[1];
			
				while(filePos < endPos){
					
					int[] LogicHeader = ReadWord(2);
			
					//System.out.printf("Logic Header = 0x%x\n", LogicHeader[0]);
					//System.out.printf("Logic Record Length = %d\n", LogicHeader[1]);
					//System.out.printf("Current Position = %d\n", filePos);
				
					if(LogicHeader[1] == 0){
						//System.out.printf("Found Empty Record for 0x%2x\n",LogicHeader[0]);
					}
					if(LogicHeader[0] == 0x02){
						//System.out.println("Found Admin Record");
						int[] AdminRecord = ReadWord(LogicHeader[1]/4);
						continue;
					}
					if(LogicHeader[0] == 0x80){
						//System.out.println("Found Trigger Record");
						int[] TriggerRecord = ReadWord(LogicHeader[1]/4);
						continue;
					}
					if(LogicHeader[0] == 0x81){
						//System.out.println("Found TLB Record");
						int[] TLBRecord = ReadWord(LogicHeader[1]/4);
						continue;
					}
					if(LogicHeader[0] == 0x60){
						//System.out.println("Found GPS Record");
						int[] GPSRecord = ReadWord(LogicHeader[1]/4);
						continue;
					}
					if(LogicHeader[0] == 0x11){
						//System.out.println("Found Trace Record");
						int[] TraceRecord = ReadWord(LogicHeader[1]/4);
						continue;
					}
					if(LogicHeader[0] == 0x21){
						//System.out.println("Found History Buffer Record");
						int[] HistRecord = ReadWord(LogicHeader[1]/4);
						continue;
					}	
					System.out.printf("Unimplemented Record Type 0x%x\n", LogicHeader[0]);
					break;
				}
			}
			
			final long endTime = System.currentTimeMillis();
			
			System.out.printf("Found %d Events in %d ms\n", nEvent, (endTime-startTime));
			
			bis.close();
			fis.close();
			
		} catch (IOException e) {
			System.out.println("IO error trying to read file!");
			e.printStackTrace();
		}	
	}
}
