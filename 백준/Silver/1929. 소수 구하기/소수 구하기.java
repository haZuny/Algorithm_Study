// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    Scanner in = new Scanner(System.in);
	    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	    
	    int m = in.nextInt();
	    int n = in.nextInt();
	    
	    if (m == 1) m = 2;
	    
	    boolean[] arr = new boolean[n+1];   // false: 소수, true: !소수
	    
	    for (int i=m; i<=n; i++){
	        
	        // i의 배수 처리
	        for (int j=i*2; j<=n; j += i){
	            arr[j] = true;
	        }
	        
	        // i의 약수가 존재하는 경우
	        if (arr[i]) continue;
	        
	        // i가 소수인지 체크
	        boolean check = false;
	        for (int j=2; j<=Math.sqrt(i); j++){
	            if (i%j == 0)   {
	                check = true;
	                break;
	            }
	        }
	        
	        // i가 소수인 경우 처리
	        if (check)   arr[i] = true;
	    }
	   
	    // 출력
	    for (int i=m; i<=n; i++){
	        if (!arr[i]) bw.write(i + "\n");
	    }
	    
	    bw.flush();
	}
}