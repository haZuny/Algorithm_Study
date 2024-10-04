// Don't place your source in a package
import java.util.*;
import java.util.stream.*;
import java.lang.*;
import java.io.*;

// 3:11

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	    
	    int n = Integer.parseInt(br.readLine());
	    
	    Deque<String> deq = new ArrayDeque();
	    
	    for (int i=0; i<n; i++){
	        String[] arr = br.readLine().split(" ");
	        
    	    switch (arr[0]){
    	        case "1":
    	            deq.addFirst(arr[1]);
    	            break;
    	        case "2":
    	            deq.addLast(arr[1]);
    	            break;
    	        case "3":
    	            try{
    	                bw.write(deq.removeFirst());
    	            } catch(Exception e){
    	                bw.write("-1");
    	            }
    	            bw.newLine();
    	            break;
    	        case "4":
    	            try{
    	                bw.write(deq.removeLast());
    	            } catch(Exception e){
    	                bw.write("-1");
    	            }
    	            bw.newLine();
    	            break;
    	        case "5":
    	            bw.write(Integer.toString(deq.size()));
    	            bw.newLine();
    	            break;
    	        case "6":
    	            if (deq.isEmpty()) bw.write("1");
    	            else bw.write("0");
    	            bw.newLine();
    	            break;
    	        case "7":
    	            try{
    	                bw.write(deq.peekFirst());
    	            } catch(Exception e){
    	                bw.write("-1");
    	            }
    	            bw.newLine();
    	            break;
    	        case "8":
    	            try{
    	                bw.write(deq.peekLast());
    	            } catch(Exception e){
    	                bw.write("-1");
    	            }
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