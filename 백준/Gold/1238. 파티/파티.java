// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main

class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    
	    String[] temp = br.readLine().split(" ");
	    int n = Integer.parseInt(temp[0]);
	    int m = Integer.parseInt(temp[1]);
	    int x = Integer.parseInt(temp[2]);
	    
	    int[][] graph = new int[n+1][n+1];
	    for (int[] arr : graph){
	        for (int i=0; i<n+1; i++)   arr[i] = Integer.MAX_VALUE;
	    }
	    
	    for (int i=0; i<m; i++){
	        temp = br.readLine().split(" ");
	        int start = Integer.parseInt(temp[0]);
	        int end = Integer.parseInt(temp[1]);
	        int weight = Integer.parseInt(temp[2]);
	        graph[start][end] = weight;
	    }
	    
	    for (int i=1; i<n+1; i++){  // i: 경유지
	        for (int j=1; j<n+1; j++){  // j: start
	            if (graph[j][i] == Integer.MAX_VALUE)   continue;
	            
	            for (int k=1; k<n+1; k++){  // k: dest
	                if (graph[i][k] == Integer.MAX_VALUE)    continue;
	                graph[j][k] = Math.min(graph[j][k], graph[j][i] + graph[i][k]);
	            }
	        }
	    }
	    
	    int maxTime = 0;
	    for (int i=1; i<n+1; i++){
	        if (i != x && maxTime < graph[i][x] + graph[x][i])
	            maxTime = graph[i][x] + graph[x][i];
	        
	    }
	    System.out.println(maxTime);
	    
	}
}