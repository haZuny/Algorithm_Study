import java.util.*;

class Solution {
    public int solution(int[][] triangle) {
        // dp 배열 초기화
        int[][] dp = new int[triangle.length][triangle.length];
        dp[0][0] = triangle[0][0];
        
        for (int i = 1; i < triangle.length; i++){
            for (int j = 0; j < triangle[i].length; j++){
                // left: j-1, right: j
                int right = dp[i-1][j];
                int left;
                if (j-1 < 0)    left = right-1; // idx 에러 방지
                else    left = dp[i-1][j-1];
                // dp 갱신
                dp[i][j] = triangle[i][j] + Math.max(left, right);
            }
        }
        
        // max 탐색
        int max = 0;
        for (int val: dp[triangle.length-1]){
            if (val > max)  max = val;
        }
        return max;
    }
}