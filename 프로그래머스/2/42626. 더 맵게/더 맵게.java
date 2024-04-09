import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        // 모든 스코빌 지수 우선순위 큐에 삽입
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int val:scoville)  pq.add(val);
                
        while (true){
            try{
                int min1 = pq.remove();
                // 가장 맵지 않은 음식의 스코빌지수가 K를 넘으면, 그동안의 횟수 리턴
                if (min1 >= K)   return answer;
                int min2 = pq.remove();
                pq.add(min1+min2*2);
                answer++;
            }
            // 만들 수 없는 경우
            catch(Exception e){
                return -1;
            }
        }
    }
}