// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
    static int n;
    static int m;
    static int ans = Integer.MAX_VALUE;
    static ArrayList <int[]> allChickens = new ArrayList();
    static ArrayList <int[]> selectedChickens = new ArrayList();
    static ArrayList <int[]> houses = new ArrayList();
    
	public static void main (String[] args) throws java.lang.Exception {
	    Scanner in = new Scanner(System.in);
	    n = in.nextInt();
	    m = in.nextInt();
	    
	    for (int i=0; i<n; i++){
	        for (int j=0; j<n; j++){
	          int[] temp = {i,j};
	          int val = in.nextInt();
	          if (val == 1)  houses.add(temp);
	          else if (val == 2)    allChickens.add(temp);
	        } 
	    }
	    
	    back(0, 0);
	    System.out.println(ans);
	}
	
	static void back(int chickenCnt, int idx){
	    // check sum
	    if (chickenCnt == m){
	        int sum = checkSum();
	        ans = Math.min(ans, sum);
	       return;
	    }
	    
	    // end
	    if (idx >= allChickens.size()) return;
	    
	    // search
	    int[] pos = allChickens.get(idx);
	    // unpick
	    back(chickenCnt, idx+1);
	    // pick
	    selectedChickens.add(pos);
	    back(chickenCnt+1, idx+1);
	    
	    selectedChickens.remove(pos);
	}
	
	static int checkSum(){
	    int sum = 0;
	    for (int[] house : houses){
	        int nearDist = Integer.MAX_VALUE;
	        for (int[] chicken : selectedChickens){
	            int dist = Math.abs(house[0] - chicken[0]) + Math.abs(house[1] - chicken[1]);
	            nearDist = Math.min(nearDist, dist);
	        }
	        sum += nearDist;
	    }
	    return sum;
	}
}