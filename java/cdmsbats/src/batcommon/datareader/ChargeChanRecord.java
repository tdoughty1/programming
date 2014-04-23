/**
 * 
 */
package batcommon.datareader;

/**
 * @author tdoughty1
 *
 */
public class ChargeChanRecord extends DataRecord {
	
	private int _detCode;
	private int _towerNum;
	private float _driverGain;
	private float _chanBias;
	private double _rtfOffset;
	private float _deltat;
	private float _t0;
	private int _traceLength;

	public ChargeChanRecord(){
		
		_detCode = -999999;
        _towerNum = -999999;
        _driverGain = -999999;
        _chanBias = -999999;
        _rtfOffset = -999999;
        _deltat = -999999;
        _t0 = -999999;
        _traceLength = -999999;
	}
	
	public void StoreValues(int[] Record){

        _detCode = Record[0];
        _towerNum = Record[1];
        _driverGain = (float)Record[2]/100;
        _chanBias = (float)Record[3]/100;
        _rtfOffset = (float)Record[6]/1e6;
        _deltat = (float)Record[8]/1000;
        _t0 = (float)Record[9]/1000;
        _traceLength = Record[10];
	}
	
	public void PrintValues(){
		
		System.out.printf("Detector Code = %d\n", _detCode);
        System.out.printf("Tower Number = %d\n", _towerNum);
        System.out.printf("Driver Gain = %3.1f\n", _driverGain);
        System.out.printf("Channel Bias = %6.2f pA\n", _chanBias);
        System.out.printf("RTF Offset = %4.2f V\n", _rtfOffset);
        System.out.printf("Delta T = %4.2f us\n", _deltat);
        System.out.printf("t0 = %5.1f us\n", _t0);
        System.out.printf("Trace Length = %d\n", _traceLength);
	}
}
