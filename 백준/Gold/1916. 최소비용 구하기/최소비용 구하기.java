// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Edge{
    int dest;
    int weight;
    
    public Edge(int dest, int weight){
        this.dest = dest;
        this.weight = weight;
    }
}

class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    
	    int n = Integer.parseInt(br.readLine());
	    int m = Integer.parseInt(br.readLine());
	    
	    ArrayList<ArrayList<Edge>> graph = new ArrayList();
	    for (int i=0; i<n+1; i++)   graph.add(new ArrayList());
	    for (int i=0; i<m; i++){
	        String[] temp = br.readLine().split(" ");
	        int start = Integer.parseInt(temp[0]);
	        int end = Integer.parseInt(temp[1]);
	        int weight = Integer.parseInt(temp[2]);
	        graph.get(start).add(new Edge(end, weight));
	    }
	    
	    String[] temp = br.readLine().split(" ");
	    int start = Integer.parseInt(temp[0]);
	    int dest = Integer.parseInt(temp[1]);
	    
	    int[] dijkstra = dijkstra(graph, start, n);
	    
	    System.out.println(dijkstra[dest]);
	}
	
	// dijkstra
	static int[] dijkstra(ArrayList<ArrayList<Edge>> graph, int start, int n){
	    
	    // init dijkstra array
	    int[] dijkstra = new int[n+1];
	    for (int i=0; i<n+1; i++) dijkstra[i] = Integer.MAX_VALUE;
	    dijkstra[start] = 0;
	    
	    // init returned array
	    int[] resultArr = new int[n+1];
	    for (int i=0; i<n+1; i++) resultArr[i] = Integer.MAX_VALUE;
	    
	    Set<Integer> visited = new HashSet();
	    
	    // search
	    for (int i=0; i<n; i++){
	        int s = findMinIdx(dijkstra);
	        
	        for (Edge edge : graph.get(s)){
	            int dest = edge.dest;
	            int weight = edge.weight;
	            if (!visited.contains(dest))
	                dijkstra[dest] = Math.min(dijkstra[dest], dijkstra[s]+weight);
	        }
	        
	        resultArr[s] = dijkstra[s];
	        dijkstra[s] = Integer.MAX_VALUE;
	        visited.add(s);
	    }
	    
	    return resultArr;
	}
	
	// search minimum index
	static int findMinIdx(int[] arr){
	    int minIdx = 0;
	    
	    for (int i=0; i<arr.length; i++){
	        if (arr[i] < arr[minIdx])   minIdx = i;
	    }
	    
	    return minIdx;
	}
}