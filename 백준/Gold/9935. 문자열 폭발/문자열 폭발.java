// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    
	    // input
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    String s = br.readLine();
	    char[] s_char = s.toCharArray();
	    String bumb = br.readLine();
	    int bumbLen = bumb.length();
	    
	    // solve
	    char[] stack = new char[s.length()];
	    int idx = 0;
	    for (char ch : s_char){
	        stack[idx] = ch;
	        
	       // check bumb
	       while(idx+1 >= bumbLen && String.valueOf(Arrays.copyOfRange(stack, idx+1-bumbLen, idx+1)).equals(bumb)){
	           idx -= bumbLen;
	       }
	       idx++;
	        
	    }
	    
	    
	    String res = String.valueOf(Arrays.copyOfRange(stack, 0, idx));
	    if (res.equals("")) System.out.println("FRULA");
	    else    System.out.println(res);
	    
	    
	}
}