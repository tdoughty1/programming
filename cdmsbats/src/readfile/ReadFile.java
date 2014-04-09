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
/**
 * @author tdoughty1
 *
 */

public class ReadFile {

	/**
	 * @param args
	 */
	public static void main(String[] args) {

		String gzFile = "/home/tdoughty1/Workspace/data/raw/01120411_1132/01120411_1132_F0002.gz";
		
		try {
			FileInputStream fis = new FileInputStream(gzFile);
			GZIPInputStream gis = new GZIPInputStream(fis);
			
			byte[] hbb = new byte[8];
			gis.read(hbb);			
			IntBuffer hb = ByteBuffer.wrap(hbb).order(ByteOrder.LITTLE_ENDIAN).asIntBuffer();
			int[] FileHeader = new int[2];
			hb.get(FileHeader);
			
			System.out.println("Endian Check = 0x" + Integer.toHexString(FileHeader[0]));
			System.out.println("File Header = 0x" + Integer.toHexString(FileHeader[1]));
			
			gis.read(hbb);
			hb = ByteBuffer.wrap(hbb).order(ByteOrder.LITTLE_ENDIAN).asIntBuffer();
			int[] ConfigHeader = new int[2];
			hb.get(ConfigHeader);
			
			System.out.println("Detector Config Header = 0x" + Integer.toHexString(ConfigHeader[0]));
			System.out.println("Detector Config Record Length = " + ConfigHeader[1]);
			
			byte[] dcbb = new byte[ConfigHeader[1]];
			gis.read(dcbb);
			IntBuffer dcb = ByteBuffer.wrap(dcbb).order(ByteOrder.LITTLE_ENDIAN).asIntBuffer();
			int[] ConfigRecord = new int[ConfigHeader[1]/4];
			dcb.get(ConfigRecord);
			
			for(int i=0;i<20;i++){
				System.out.println(ConfigRecord[i]);
			}
					
			
			gis.close();
			fis.close();
			
		} catch (IOException e) {
			System.out.println("IO error trying to read file!");
			e.printStackTrace();
		}
	}
}
