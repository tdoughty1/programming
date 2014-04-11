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
	
	private static int[] ReadInt(int nWords){
		
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
		
		try {
			
			ReadFile.filePos = 0;
			ReadFile.fis = new FileInputStream(gzFile);
			ReadFile.gis = new GZIPInputStream(ReadFile.fis);
			ReadFile.bis = new BufferedInputStream(ReadFile.gis);
			
			int[] FileHeader = ReadFile.ReadInt(2);
			
			System.out.printf("Endian Check = 0x%x\n", FileHeader[0]);
			System.out.printf("File Header = 0x%x\n", FileHeader[1]);
			System.out.printf("Current Position = %d\n", ReadFile.filePos);
			
			int[] ConfigHeader = ReadFile.ReadInt(2);
			
			System.out.printf("Detector Config Header = 0x%x\n", ConfigHeader[0]);
			System.out.printf("Detector Config Record Length = %d\n", ConfigHeader[1]);
			System.out.printf("Current Position = %d\n", ReadFile.filePos);
			
			int endpos = ReadFile.filePos + ConfigHeader[1];
			int chans = 0;
			
			////////////////////////////////////////////////////////////////////////////////////////////////
			// Loop through all the channels in Detector Config Record
			////////////////////////////////////////////////////////////////////////////////////////////////
			while(ReadFile.filePos < endpos){

				int[] ConfigRecord = ReadFile.ReadInt(2);

				System.out.printf("Channel Header = 0x%x\n", ConfigRecord[0]);
				System.out.printf("Channel Record Length = %d\n", ConfigRecord[1]);
				System.out.printf("Current Position = %d\n", ReadFile.filePos);
				
				if(ConfigRecord[0] == 0x10001){
					System.out.println("Found Phonon Channel");
					
					byte[] cbb = new byte[ConfigRecord[1]];
					bis.read(cbb);
					IntBuffer cb = ByteBuffer.wrap(cbb).order(ByteOrder.LITTLE_ENDIAN).asIntBuffer();
					int[] ChanRecord = new int[ConfigRecord[1]/4];
					cb.get(ChanRecord);
					ReadFile.filePos += ConfigRecord[1];
					chans += 1;
					System.out.printf("First Entry in Record = 0x%x\n", ChanRecord[0]);
					System.out.printf("Last Entry in Record = 0x%x\n", ChanRecord[ConfigRecord[1]/4 -1]);					
					System.out.printf("Current Position = %d\n", ReadFile.filePos);
					continue;
				}
				
				if(ConfigRecord[0] == 0x10002){
					System.out.println("Found Charge Channel");
					
					byte[] cbb = new byte[ConfigRecord[1]];
					bis.read(cbb);
					IntBuffer cb = ByteBuffer.wrap(cbb).order(ByteOrder.LITTLE_ENDIAN).asIntBuffer();
					int[] ChanRecord = new int[ConfigRecord[1]/4];
					cb.get(ChanRecord);
					ReadFile.filePos += ConfigRecord[1];
					chans += 1;
					System.out.printf("First Entry in Record = 0x%x\n", ChanRecord[0]);
					System.out.printf("Last Entry in Record = 0x%x\n", ChanRecord[ConfigRecord[1]/4 -1]);
					System.out.printf("Current Position = %d\n", ReadFile.filePos);
					continue;
				}
				System.out.println("Found Unknown Channel Type");
				System.out.printf("Read %d channels\n", chans);
				break;
			}
			
			System.out.println("Finished Reading Detector Config");
			
			bis.close();
			fis.close();
			
		} catch (IOException e) {
			System.out.println("IO error trying to read file!");
			e.printStackTrace();
		}
	}
}
