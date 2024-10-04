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
	    
	    int n = Integer.parseInt(br.readLine());
	    String[] qs_type = br.readLine().split(" ");
	    String[] qs_val = br.readLine().split(" ");
	    int m = Integer.parseInt(br.readLine());
	    String[] addVar = br.readLine().split(" ");
	    
	    // 스택은 무시하고 새로운 queue 구성
	    Queue<String> q = new LinkedList();
	    for (int i=n-1; i>=0; i--){
	        if (qs_type[i].equals("0"))   q.add(qs_val[i]);
	    }
	    
	    // 연산 수행
	    for (String cvar : addVar){
	        q.add(cvar);
	        bw.write(q.remove()+" ");
	    }
	    bw.flush();
	    bw.close();
	}
}