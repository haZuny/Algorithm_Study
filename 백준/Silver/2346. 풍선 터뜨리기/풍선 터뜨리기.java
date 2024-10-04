// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    
	    Scanner sc = new Scanner(System.in);
	    int n = sc.nextInt();
	    
	    // Deq 초기화
	    LinkedList<int[]> ls = new LinkedList();
	    for (int i=1; i<=n; i++){
	        int value = sc.nextInt();
	        int[] arr = {i, value};
	        ls.add(arr);
	    }
	    
	    // 터트린 풍선 위치
	    int idx = 0;
	    
	    while (true){
	        
	        int[] balloon = ls.get(idx);
	        ls.remove(idx);
	        System.out.printf("%d ", balloon[0]);
	        if (ls.size() <= 0) break;
	        
	        // idx에 pop을 했기 때문에, +방향일 경우는 왼쪽으로 한 칸 이동후 계산
	        if (balloon[1] > 0){
	            idx--;
	        }
	        
	        // 한바퀴 이상인 경우 생략
	        int move = balloon[1] % ls.size();
	        
	        // 풍선 이동
	        idx += move;
	        if (idx < 0)    idx = ls.size() + idx;
	        else if (idx >= ls.size())  idx -= ls.size();
	    }
	}
}