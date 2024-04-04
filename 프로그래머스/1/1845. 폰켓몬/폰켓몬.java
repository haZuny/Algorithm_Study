import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        // Set을 사용하여 종류의 갯수를 구함
        HashSet<Integer> set = new HashSet<Integer>();
        for (int num:nums){
            if (!set.contains(num)){
                set.add(num);
                answer++;
            }
        }
        
        // 최대 개수보다 종류가 많을 경우 처리
        if (answer >= nums.length/2){
            answer = nums.length/2;
        }
        return answer;
    }
}