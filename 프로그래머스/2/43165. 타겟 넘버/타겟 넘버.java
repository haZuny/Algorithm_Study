import java.util.*;

class Solution {
    int answer = 0;
    int[] numbers;
    int target;
    
    public int solution(int[] numbers, int target) {
        this.numbers = numbers;
        this.target = target;
        
        reculsive(0,0);
        return answer;
    }
    
    void reculsive(int sum, int idx){
        if (idx == numbers.length && sum == target)  answer++;
        else if(idx == numbers.length)   return;
        else{
            reculsive(sum+numbers[idx], idx+1);
            reculsive(sum-numbers[idx], idx+1);
        }
    }
}