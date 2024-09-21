// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    
	    // input
	    Scanner sc = new Scanner(System.in);
	    
	    int n = sc.nextInt();
	    int[] arr = new int[n];
	    for (int i=0; i<n; i++) arr[i] = sc.nextInt();
	    
	    // solve
	    HashSet<Integer> set = new HashSet(Arrays.asList());
	    int f1 = -1;
	    int f2 = 0;
	    int max = 0;
	    int cnt_current = 0;
	    int cnt_f2 = 0;
	    
	    for (int f : arr){
	        int temp_f1 = f1;
	        int temp_cnt_f2 = cnt_f2;
	        
	        // f1, f2 update
	        if(f2 != f){
	            f1 = f2;
	            f2 = f;
	            cnt_f2 = 1;
	        }
	        else cnt_f2++;
	        
	        // if set is empty 
	        if (set.size()<2) set.add(f2);
	        
	        // main process
	        if (set.contains(f2))   cnt_current++;
	        else{
	            cnt_current = temp_cnt_f2 + 1;
	            set.remove(temp_f1);
	            set.add(f2);
	        }
	        
	        max = Math.max(max, cnt_current);
	    }
	    
	   // out
	   System.out.println(max);
	}
}