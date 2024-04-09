import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        // 배포된 횟수 기록
        int[] answer = new int[progresses.length];
        int idx = 0;
        
        // 배포 완료된 작업
        Stack<Integer> st = new Stack<Integer>();
        st.push(-1);
        
        // 배포 완료할때까지 반복
        while(st.size() <= progresses.length){
            int num = 0;            
            for(int i=0; i<progresses.length; i++){
                // 작업 진행
                progresses[i] += speeds[i];
                // 작업 완료되고, 작업이 배포될 순서면 배포
                if (st.peek()+1 == i && progresses[i]>=100){
                    st.push(i);
                    num++;
                }
            }
            // 배포된 기록이 있으면 answer에 추가
            if (num>0)  answer[idx++] = num;
        }
        
        return Arrays.copyOf(answer, idx);
    }
}