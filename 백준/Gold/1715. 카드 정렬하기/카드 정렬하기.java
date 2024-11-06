// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    int n = Integer.parseInt(br.readLine());
	    
	    PriorityQueue<Integer> pq = new PriorityQueue();
	    for (int i=0; i<n; i++) pq.add(Integer.parseInt(br.readLine()));
	    int cnt = 0;
	    while(pq.size() > 1){
	        int n1 = pq.remove();
	        int n2 = pq.remove();
	        cnt += n1+n2;
	        pq.add(n1+n2);
	    }
	    
	    System.out.println(cnt);
	}
}