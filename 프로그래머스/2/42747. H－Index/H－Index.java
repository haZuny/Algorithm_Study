// 0 1 3 5 6
import java.util.*;

class Solution {
    public int solution(int[] citations) {
        // 정렬
        Arrays.sort(citations);
        
        // H-Index 구하기
        int answer = 0;
        for (int i = 1; i<=citations.length; i++){
            if (citations[citations.length-i] >= i) answer = i;
        }
    
        return answer;
    }
}