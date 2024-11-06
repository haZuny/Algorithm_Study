// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    
	    // input
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    int n = Integer.parseInt(br.readLine());
	    String[] arr = new String[n];
	    for (int i=0; i<n; i++) arr[i] = br.readLine();
	    
	    // sort
	    Arrays.sort(arr, new Comparator<String>(){
	        @Override
	        public int compare(String s1, String s2){
	            if (s1.length() > s2.length())  return 1;
	            else if (s1.length() < s2.length()) return -1;
	            else    return s1.compareTo(s2);
	        }
	    });
	    
	    // output
	    String lastStr = "A";
	    for (String s : arr){
	        if (s.equals(lastStr))    continue;
	        lastStr = s;
	        System.out.println(s);
	    }
	}
}