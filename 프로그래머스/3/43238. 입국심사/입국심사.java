import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        int length = times.length;
        
        // min, max 얻기
        Arrays.sort(times);
        long min = 1;
        long max = times[length-1]*(long)n;
        
        
        // 이분 탐색
        while(true){
            // mid 시간 동안 처리 가능한 사람의 수 구하기
            long mid = (min+max)/2;
            long n_mid = 0; 
            for(int time:times){
                n_mid += mid/time;
            }
            // min, max가 1 차이 날 경우
            if(max-min == 1 || min==max){
                if (n_mid >= n) return min;
                else return max;
            }
            // min, max 갱신
            if(n_mid >= n){
                max = mid;
            }
            else{
                min = mid;
            }
        }
    }
}