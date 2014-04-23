/**
 * 
 */

package batcommon.datareader;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.IntBuffer;
import java.nio.ShortBuffer;
import java.util.zip.GZIPInputStream;

/**
 * @author tdoughty1
 * 
 */
public class CDMSRawFileStream {

	private FileInputStream fiStream;
	private GZIPInputStream gziStream;
	private BufferedInputStream _FileStream;
	private String _FileName;
	private int _FilePos;
	private boolean _Open;

	public CDMSRawFileStream() {
		_FileName = null;
		_FileStream = null;
		_Open = false;
		_FilePos = -1;
	}

	public CDMSRawFileStream(String fName, String mode) {
		Open(fName, mode);
	}

	public void Open(String fName, String mode) {

		try {
			fiStream = new FileInputStream(fName);
			gziStream = new GZIPInputStream(fiStream, 256 * 256);
			_FileStream = new BufferedInputStream(gziStream, 256 * 256);
			_FileName = fName;
			_Open = true;
			_FilePos = 0;
		} catch (IOException e) {
			System.out.println("ERROR in ReadFile.OpenFile:");
			System.out.printf("Couldn't Open File %s.\n", fName);
			e.printStackTrace();
		}
	}

	public void Close() {
		try {
			_FileStream.close();
			gziStream.close();
			fiStream.close();
			_FileName = null;
			_Open = false;
			_FilePos = -1;
		} catch (IOException e) {
			System.out.println("ERROR in ReadFile.CloseFile:");
			System.out.println("Could not successfully close file streams.");
			e.printStackTrace();
		}
	}
	
	public int Tell() {
		return _FilePos;
	}

	public int[] ReadWords(int nWords, int mode) {

		byte[] byteArray = new byte[nWords * 4];
		int[] wordArray = new int[nWords];

		try {
			_FileStream.read(byteArray);
			IntBuffer intBuffer = ByteBuffer.wrap(byteArray)
					.order(ByteOrder.LITTLE_ENDIAN).asIntBuffer();
			intBuffer.get(wordArray);
			_FilePos += nWords * 4;

		} catch (IOException e) {
			System.out.println("ERROR in ReadFile.ReadWord:");
			System.out.println("Could not read requested word");
			e.printStackTrace();
		}
		return wordArray;
	}

	public short[] ReadWords(int nVals, short mode) {

		byte[] byteArray = new byte[nVals * 2];
		short[] shortArray = new short[nVals];

		try {
			_FileStream.read(byteArray);
			ShortBuffer shortBuffer = ByteBuffer.wrap(byteArray)
					.order(ByteOrder.LITTLE_ENDIAN).asShortBuffer();
			shortBuffer.get(shortArray);
			_FilePos += nVals * 2;

		} catch (IOException e) {
			System.out.println("ERROR in ReadFile.ReadWord:");
			System.out.println("Could not read requested word");
			e.printStackTrace();
		}
		return shortArray;
	}
}
