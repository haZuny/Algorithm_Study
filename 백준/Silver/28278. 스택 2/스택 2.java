// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    
	    // read/write buf
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	    
	    // stank
	    Stack<Integer> st = new Stack();
	    
	    // read n
	    int n = Integer.parseInt(br.readLine());
	    
	    
	    for (int i=0; i<n; i++){
	        String s = br.readLine();
	        String arr[] = s.split(" ");
	        
	        
	        switch(Integer.parseInt(arr[0])){
	            case 1:
	                st.push(Integer.parseInt(arr[1]));
	                break;
	            case 2:
	                if(st.isEmpty())    bw.write("-1");
	                else    bw.write(Integer.toString(st.pop()));
	                bw.newLine();
	                break;
	            case 3:
	                bw.write(Integer.toString(st.size()));
	                bw.newLine();
	                break;
	           case 4:
	               if(st.isEmpty())   bw.write("1");
	               else bw.write("0");
	               bw.newLine();
	               break;
	           case 5:
	               if(st.isEmpty())    bw.write("-1");
	               else    bw.write(Integer.toString(st.peek()));
	               bw.newLine();
	               break;
	           default:
	                break;
	        }
	    }
	    
	    bw.flush();
	    bw.close();
	   
	}
}