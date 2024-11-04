// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    Scanner in = new Scanner(System.in);
	    
		String s = in.nextLine();
		
		while (s.length() >= 10){
		    System.out.println(s.substring(0, 10));
		    s = s.substring(10);
		}
		if (!s.equals(""))
		    System.out.println(s);
	}
}