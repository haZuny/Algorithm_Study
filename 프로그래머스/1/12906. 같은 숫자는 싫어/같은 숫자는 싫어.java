import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        Stack<Integer> st = new Stack<Integer>();
        
        int lastNum = -1;
        for (int num:arr){
            if (num != lastNum){
                st.push(num);
                lastNum = num;
            }
        }
        
        int[] answer = new int[st.size()];
        for (int i = st.size()-1; i>=0; i--){
            answer[i] = st.pop();
        }

        return answer;
    }
}