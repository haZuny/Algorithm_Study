// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    Scanner sc = new Scanner(System.in);
	    
	    // input
	    String i1 = sc.nextLine();
	    String i2 = sc.nextLine();
	    String i3 = sc.nextLine();
	    
	   
	    // solve
	    int o = 1;
	    try{
	        o = Integer.parseInt(i1) + 3;
	    } catch(Exception e){}
	    try{
	        o = Integer.parseInt(i2) + 2;
	    } catch(Exception e){}
	    try{
	        o = Integer.parseInt(i3) + 1;
	    } catch(Exception e){}
	    
	    // output
	    if (o % 3 == 0){
	        if (o % 5 == 0) System.out.println("FizzBuzz");
	       else System.out.println("Fizz");
	    }
	    else if (o % 5 == 0)    System.out.println("Buzz");
	    else System.out.println(o);
	}
}