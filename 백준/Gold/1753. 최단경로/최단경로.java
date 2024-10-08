// Don't place your source in a package
import java.util.*;
import java.util.stream.*;
import java.lang.*;
import java.io.*;

// 2:17

class Edge{
    int dest;
    int weight;
    
    public Edge(int dest, int weight){
        this. dest = dest;
        this.weight = weight;
    }
}
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	    
	    String[] temp = br.readLine().split(" ");
	    int v = Integer.parseInt(temp[0]);
	    int e = Integer.parseInt(temp[1]);
	    
	    int start = Integer.parseInt(br.readLine());
	    
	    // init graph
	    ArrayList<ArrayList<Edge>> graph = new ArrayList();
	    for (int i=0; i<v+1; i++)   graph.add(new ArrayList());
	    
	    // add edges
	    for (int i=0; i<e; i++){
	        temp = br.readLine().split(" ");
	        int u = Integer.parseInt(temp[0]);
	        int v2 = Integer.parseInt(temp[1]);
	        int w = Integer.parseInt(temp[2]);
	        graph.get(u).add(new Edge(v2, w));
	    }
	    
	    // dijkstra array
	    int[] dijkstra = new int[v+1];
	    int[] answer = new int[v+1];    // 최소값 표시 배열(dijkstra 배열에서 탐색 완료된 배열은 INF 처리하기 때문에 필요)
	    for (int i=0; i<v+1; i++){
	        dijkstra[i] = Integer.MAX_VALUE;
	        answer[i] = Integer.MAX_VALUE;
	    }
	    dijkstra[start] = 0;
	    answer[start] = 0;
	    
	    // dijkstra
	    Set<Integer> visited = new HashSet();
	    
	    for (int ii=0; ii<v; ii++){
	        
	        // search min idx
	        int minVal = dijkstra[0];
	        int minIdx = 0;
	        for (int i=1; i<v+1; i++){
	            if(dijkstra[i]<minVal){
	                minVal = dijkstra[i];
	                minIdx = i;
	            }
	        }
	        
	        // update adjacent node
	        for (Edge edge : graph.get(minIdx)){
	            if (!visited.contains(edge.dest))
	                dijkstra[edge.dest] = Math.min(dijkstra[edge.dest], dijkstra[minIdx]+edge.weight);
	        }
	        
	        // done check
	        answer[minIdx] = Math.min(minVal, answer[minIdx]);
	        dijkstra[minIdx] = Integer.MAX_VALUE;
	        visited.add(minIdx);
	    }
	    
	    
	    // print
	    for (int i=1; i<v+1; i++){
	        if (answer[i] == Integer.MAX_VALUE)   bw.write("INF");
	        else    bw.write(Integer.toString(answer[i]));
	        bw.newLine();
	    }
	    
	    bw.flush();
	    bw.close();
	}
}