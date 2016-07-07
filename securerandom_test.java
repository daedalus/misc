import java.security.SecureRandom;

public class securerandom_test {
	
	final protected static char[] hexArray = "0123456789ABCDEF".toCharArray();
	public static String bytesToHex(byte[] bytes) {
    		char[] hexChars = new char[bytes.length * 2];
    		for ( int j = 0; j < bytes.length; j++ ) {
        		int v = bytes[j] & 0xFF;
        		hexChars[j * 2] = hexArray[v >>> 4];
        		hexChars[j * 2 + 1] = hexArray[v & 0x0F];
    		}
    		return new String(hexChars);
	}


	public static byte[] hexStringToByteArray(String s) {
    		int len = s.length();
    		byte[] data = new byte[len / 2];
    		for (int i = 0; i < len; i += 2) {
        		data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4) + Character.digit(s.charAt(i+1), 16));
    		}
    		return data;
	}

    	public static void main(String[] args) {

		SecureRandom random = new SecureRandom();
		
		String seed_hex = "3c21444f43545950452048544d4c205055424c494320222d2f2f494554462f2f";
		//System.out.println("Seed_hex:" + seed_hex);
 		byte[] seed = hexStringToByteArray(seed_hex);
		//int len = seed.length;
		//String r = String(seed);
		//System.out.println("Seed:" + r);
		
		while(true){
			random.setSeed(seed);
 			byte[] seedR = new byte[32];		
 			random.nextBytes(seedR);	
        		System.out.println(bytesToHex(seedR));
		}
    }

}
