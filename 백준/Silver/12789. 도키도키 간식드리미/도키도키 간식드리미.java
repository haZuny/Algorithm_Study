// Don't place your source in a package
import java.util.*;
import java.util.stream.Stream;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    
	    int n = Integer.parseInt(br.readLine());
	    int[] arr = Stream.of(br.readLine().split(" ")).mapToInt(e->Integer.parseInt(e)).toArray();
	    
	    int lastNum = 0;
	    Stack<Integer> st = new Stack();
	    
	    int i = 0;
	    
	    while(i < n){
	        if(arr[i] == lastNum+1){
	            lastNum = arr[i];
	            i++;
	        }
	        else if(st.size()>0 && st.peek() == lastNum+1)  lastNum = st.pop();
	        else    st.push(arr[i++]);
	    }
	    
	    while (st.size()>0){
	        if (st.peek() == lastNum+1) lastNum = st.pop();
	        else    break;
	    }
	    
	    if (st.size() > 0)  System.out.println("Sad");
	    else    System.out.println("Nice");
	}
}