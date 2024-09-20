// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    Scanner sc = new Scanner(System.in);
	    
	    // input
	    int n = sc.nextInt();
	    
	    ArrayList<Integer> sizes = new ArrayList();
	    for (int i = 0; i < 6; i++)
	        sizes.add(sc.nextInt());
	    
	    int t = sc.nextInt();
	    int p = sc.nextInt();
	    
	    // output
	    int o1 = 0;
	    for (int size : sizes){
	        o1 += size/t + 1;
	        if (size%t == 0) o1--;
	    }
	    System.out.println(o1);
	    
	    int o2 = 0;
	    System.out.println(n / p + " " + n % p);
	}
}