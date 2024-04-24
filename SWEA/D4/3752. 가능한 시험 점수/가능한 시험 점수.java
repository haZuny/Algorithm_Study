import java.util.*;
// dp로 탐색
// 최대 점수만큼의 크기를 가지는 dp 배열 생성
// 1. 한 문제씩 선택
// 2. 해당 문제를 dp배열에 기록
// 3. 지금 까지 기록된 dp배열에 선택된 문제를 더한 값도 dp에 기록
// 4. 계속 문제 선택하면서 진행

class Solution{    
	static public void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        
        for (int test_case = 1; test_case <= T; test_case++){
            // Input
        	int n = sc.nextInt();
            int maxVal = 0;
            int[] arr = new int[n];
            for(int i = 0; i < n; i++){
            	arr[i] = sc.nextInt();
                maxVal += arr[i];
            }
            
            // 탐색
            int[] dp = new int[maxVal+1];
            dp[0] = 1;
            for (int point : arr){
                int[] temp = dp.clone();	// dp 탐색하면서 업데이트 한 값이 반영되지 않도록 임시 배열에서 업데이트
                for (int i = 1; i <= maxVal; i++){
                	if (dp[i] == 1 && i+point <= maxVal){
                        temp[point + i] = 1;
                    }
                }
                dp = temp;
                dp[point] = 1;
            }            
            
            // 갯수 계산
            int answer = 0;
            for (int selected : dp){
            	if (selected == 1)		answer+=1;
            }
            
            // 출력
            System.out.printf("#%d %d\n", test_case, answer);
        }
    }
}