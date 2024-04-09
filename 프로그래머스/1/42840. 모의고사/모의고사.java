import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] scores = new int[3];
        int[] ans_1 = {1,2,3,4,5};
        int[] ans_2 = {2,1,2,3,2,4,2,5};
        int[] ans_3 = {3,3,1,1,2,2,4,4,5,5};
        
        // 채점
        for (int i=0; i<answers.length; i++){
            if (answers[i] == ans_1[i%5])   scores[0]++;    // 1번 수포자
            if (answers[i] == ans_2[i%8])   scores[1]++;    // 2번 수포자
            if (answers[i] == ans_3[i%10])  scores[2]++;    // 3번 수포자            
        }
        
        // 가장 많이 맞힌 사람 찾기
        int maxScore = Math.max(Math.max(scores[0], scores[1]), scores[2]);
        int[] answer = {};
        for (int i = 0; i < 3; i++){
            if (maxScore == scores[i]){
                answer = Arrays.copyOf(answer, answer.length+1);
                answer[answer.length-1] = i+1;
            }
        }
        
        return answer;
    }
}