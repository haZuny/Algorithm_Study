// Don't place your source in a package
import java.util.*;
import java.util.stream.*;
import java.lang.*;
import java.io.*;

class Edge {
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
	    
	    // reset graph
	    ArrayList<ArrayList<Edge>> graph = new ArrayList();
	    for (int i=0; i<n+1; i++)   graph.add(new ArrayList()); // idx: 1~n
	    
	    // add link
	    for (int i=0; i<n-1; i++){
	        String[] arr = br.readLine().split(" ");
	        
	        int parent = Integer.parseInt(arr[0]);
	        int child = Integer.parseInt(arr[1]);
	        int weight = Integer.parseInt(arr[2]);
	        
	        graph.get(parent).add(new Edge(child, weight));
	        graph.get(child).add(new Edge(parent, weight));
	    }
	    
	    
	    // dfs1
	    int[] max = new int[2]; // [node, distance]
	    
	    // insert first node(1)
	    Stack<int[]> st = new Stack(); //[(nextNode, distance), ..]
	    HashSet<Integer> visited = new HashSet();
	    int[] first = {1, 0};
	    st.push(first);
	    visited.add(1);
	    
	    while(st.size()>0){
	        // get node
	        int[] node = st.pop();
	       
	       // update max
	        if (node[1] > max[1])   max = node;
	        
	        // search next
	        for (Edge edge : graph.get(node[0])){
	            if (!visited.contains(edge.dest)){
	                int[] temp = {edge.dest, node[1]+edge.weight};
	                st.push(temp);
	                visited.add(edge.dest);
	            }
	        }
	        
	    }
	    
	    
	    
	    // dfs2
	        // search from max
	    int start = max[0];
	    max = new int[2]; // [node, distance]
	    
	    // insert first node(1)
	    st = new Stack(); //[(nextNode, distance), ..]
	    visited = new HashSet();
	    int[] first2 = {start, 0};
	    st.push(first2);
	    visited.add(start);
	    
	    while(st.size()>0){
	        // get node
	        int[] node = st.pop();
	       
	       // update max
	        if (node[1] > max[1])   max = node;
	        
	        // search next
	        for (Edge edge : graph.get(node[0])){
	            if (!visited.contains(edge.dest)){
	                int[] temp = {edge.dest, node[1]+edge.weight};
	                st.push(temp);
	                visited.add(edge.dest);
	            }
	        }
	        
	    }
	    
	    System.out.println(max[1]);
	    
	}
}