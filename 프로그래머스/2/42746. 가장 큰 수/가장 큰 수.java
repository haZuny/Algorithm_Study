import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        // 문자열 배열로 전환
        String[] strArr = new String[numbers.length];
        for (int i = 0; i<numbers.length; i++){
            strArr[i] = Integer.toString(numbers[i]);
        }
        
        // sort, compareTo 사용하여 정렬
        Arrays.sort(strArr, (a, b) -> (b+a).compareTo(a+b) );
        
        // 리턴값이 0인 경우 처리
        if (strArr[0].equals("0")) return "0";
        
        String answer = "";
        for (String num:strArr){
            answer += num;
        }
        return answer;
    }
}