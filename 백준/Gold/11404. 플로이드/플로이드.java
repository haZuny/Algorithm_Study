// Don't place your source in a package
import java.util.*;
import java.util.stream.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    
	   BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	   BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	   
	   // input
	   int n = Integer.parseInt(br.readLine());
	   int m = Integer.parseInt(br.readLine());
	   
	   // init graph
	   int[][] graph = new int[n+1][n+1];
	   for (int[] arr : graph){
	       for (int i=0; i<n+1; i++)    arr[i] = Integer.MAX_VALUE;
	   }
	   
	   // add edge
	   for (int i=0; i<m; i++){
	       String[] line = br.readLine().split(" ");
	       int a = Integer.parseInt(line[0]);
	       int b = Integer.parseInt(line[1]);
	       int c = Integer.parseInt(line[2]);
	       graph[a][b] = Math.min(graph[a][b], c);
	   }
	   
	   // floyd
	   for (int i=1; i<n+1; i++){   // i: 중간 노드
	       for (int j=1; j<n+1; j++){   // j: 출발 노드
	           if (graph[j][i] == Integer.MAX_VALUE)    continue;
	           for (int k=1; k<n+1; k++){   // k: 도착 노드
	               if (j==k)    continue;
	               if (graph[i][k] == Integer.MAX_VALUE)    continue;
	               graph[j][k] = Math.min(graph[j][k], graph[j][i]+graph[i][k]);
	               
	           }
	       }
	   }
	   
	   // print
	   for (int i=1; i<n+1; i++){
	       for (int j=1; j<n+1; j++){
	           if (graph[i][j] == Integer.MAX_VALUE) bw.write("0 ");
	           else bw.write(graph[i][j]+" ");
	       }
	       bw.newLine();
	   }
	   bw.flush();
	   bw.close();
	}
}